# def tt_entails(kb, alpha):
#     """
#     Determine if KB entails alpha using truth table enumeration.
#     """
#     symbols = extract_symbols(kb, alpha)
#     return tt_check_all(kb, alpha, symbols, {})


# def tt_check_all(kb, alpha, symbols, model):
#     """
#     Recursively checks all possible truth assignments.
#     """
#     # Base case: no more symbols to assign
#     if not symbols:
#         if pl_true(kb, model):
#             return pl_true(alpha, model)
#         else:
#             return True  # If KB is false, vacuously true
    
#     # Recursive case: assign truth values to the first symbol
#     p = symbols[0]
#     rest = symbols[1:]
    
#     return (
#         tt_check_all(kb, alpha, rest, {**model, p: True}) and
#         tt_check_all(kb, alpha, rest, {**model, p: False})
#     )


# def pl_true(sentence, model):
#     """
#     Evaluates if a propositional logic sentence is true under a given model.
#     """
#     if isinstance(sentence, str):  # Atomic proposition
#         return model.get(sentence, False)
#     elif isinstance(sentence, tuple):  # Complex sentence
#         operator, *args = sentence
#         if operator == "NOT":
#             return not pl_true(args[0], model)
#         elif operator == "OR":
#             return any(pl_true(arg, model) for arg in args)
#         elif operator == "AND":
#             return all(pl_true(arg, model) for arg in args)
#         elif operator == "IMPLIES":
#             return not pl_true(args[0], model) or pl_true(args[1], model)
#     return False


# def extract_symbols(kb, alpha):
#     """
#     Extract all unique propositional symbols from KB and alpha.
#     """
#     symbols = set()
#     for sentence in kb + [alpha]:
#         symbols.update(find_symbols(sentence))
#     return list(symbols)


# def find_symbols(sentence):
#     """
#     Recursively find all propositional symbols in a sentence.
#     """
#     if isinstance(sentence, str):  # Atomic proposition
#         return {sentence}
#     elif isinstance(sentence, tuple):  # Complex sentence
#         symbols = set()
#         for arg in sentence[1:]:
#             symbols.update(find_symbols(arg))
#         return symbols
#     return set()


# # Example usage:

# # Knowledge base: KB = {P OR Q, NOT P}
# kb = [
#     ("OR", "P", "Q"),
#     ("NOT", "P")
# ]

# # Query: alpha = Q
# alpha = "Q"

# # Check if KB entails alpha
# result = tt_entails(kb, alpha)
# print("KB entails α:", result)
from itertools import product

def pl_true(sentence, model):
    """
    Evaluates if a sentence is true in a given model.
    """
    if isinstance(sentence, str):
        return model.get(sentence, False)
    elif isinstance(sentence, tuple) and len(sentence) == 2:  # NOT operation
        operator, operand = sentence
        if operator == "NOT":
            return not pl_true(operand, model)
    elif isinstance(sentence, tuple) and len(sentence) == 3:
        operator, left, right = sentence
        if operator == "AND":
            return pl_true(left, model) and pl_true(right, model)
        elif operator == "OR":
            return pl_true(left, model) or pl_true(right, model)
        elif operator == "IMPLIES":
            return not pl_true(left, model) or pl_true(right, model)
        elif operator == "IFF":
            return pl_true(left, model) == pl_true(right, model)
    return False

def tt_entails(kb, alpha, symbols):
    """
    Checks if KB entails alpha using truth-table enumeration.
    """
    all_models = product([False, True], repeat=len(symbols))
    valid_models = []

    for values in all_models:
        model = dict(zip(symbols, values))
        kb_value = pl_true(kb, model)
        alpha_value = pl_true(alpha, model)

        if kb_value:  # If KB is true in this model
            if not alpha_value:  # If KB is true but α is not, entailment fails
                return False, None
            else:
                valid_models.append(model)

    return True, valid_models

def print_truth_table(kb, alpha, symbols):
    """
    Generates and prints the truth table for KB and α.
    """
    headers = ["A", "B", "C", "A∨C", "B∨¬C", "KB", "α"]
    print(" | ".join(headers))
    print("-" * (len(headers) * 9))  # Separator line

    # Generate all combinations of truth values
    for values in product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))

        # Evaluate sub-expressions and main expressions
        a_or_c = pl_true(("OR", "A", "C"), model)
        b_or_not_c = pl_true(("OR", "B", ("NOT", "C")), model)
        kb_value = pl_true(kb, model)
        alpha_value = pl_true(alpha, model)

        # Print the truth table row
        row = list(values) + [a_or_c, b_or_not_c, kb_value, alpha_value]
        row_str = " | ".join(str(v).ljust(7) for v in row)

        # Highlight rows where both KB and α are true
        if kb_value and alpha_value:
            print(f"\033[92m{row_str}\033[0m")  # Green color for rows where KB and α are true
        else:
            print(row_str)

# Define the knowledge base and query
symbols = ["A", "B", "C"]
kb = ("AND", ("OR", "A", "C"), ("OR", "B", ("NOT", "C")))
alpha = ("OR", "A", "B")

# Print the truth table
print_truth_table(kb, alpha, symbols)

# Run the truth-table entailment check
entailment, models = tt_entails(kb, alpha, symbols)

# Print the result
print("\nResult:")
if entailment:
    print("KB entails α.")
    print("The values of A, B, C for which KB and α are true:")
    for model in models:
        print(model)
else:
    print("KB does not entail α.")
