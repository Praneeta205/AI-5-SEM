# import math

# # Alpha-Beta Pruning Algorithm
# def alpha_beta_search(depth, index, is_max, values, alpha, beta, target_depth):
#     """Recursive function for Alpha-Beta Pruning."""
#     # Base case: If the target depth is reached, return the leaf node value
#     if depth == target_depth:
#         return values[index]
    
#     if is_max:
#         # Maximizer's turn
#         best = -math.inf
#         for i in range(2):
#             val = alpha_beta_search(depth + 1, index * 2 + i, False, values, alpha, beta, target_depth)
#             best = max(best, val)
#             alpha = max(alpha, best)
#             if beta <= alpha:
#                 break  # Prune remaining branches
#         return best
#     else:
#         # Minimizer's turn
#         best = math.inf
#         for i in range(2):
#             val = alpha_beta_search(depth + 1, index * 2 + i, True, values, alpha, beta, target_depth)
#             best = min(best, val)
#             beta = min(beta, best)
#             if beta <= alpha:
#                 break  # Prune remaining branches
#         return best

# def main():
#     # User Input: Values of leaf nodes
#     print("Enter the values of leaf nodes separated by spaces:")
#     values = list(map(int, input().split()))
    
#     # Calculate depth of the game tree
#     target_depth = math.log2(len(values))
#     if target_depth != int(target_depth):
#         print("Error: The number of leaf nodes must be a power of 2.")
#         return
    
#     target_depth = int(target_depth)
    
#     # Run Alpha-Beta Pruning
#     result = alpha_beta_search(0, 0, True, values, -math.inf, math.inf, target_depth)
    
#     # Display the result
#     print(f"The optimal value determined by Alpha-Beta Pruning is: {result}")

# if __name__ == "__main__":
#     main()
import math

# Alpha-Beta Pruning Algorithm
def alpha_beta_search(depth, index, is_max, values, alpha, beta, target_depth, branch_factor):
    """Recursive function for Alpha-Beta Pruning."""
    # Base case: If the target depth is reached, return the leaf node value
    if depth == target_depth:
        return values[index]
    
    if is_max:
        # Maximizer's turn
        best = -math.inf
        for i in range(branch_factor):  # Iterate over all children
            val = alpha_beta_search(depth + 1, index * branch_factor + i, False, values, alpha, beta, target_depth, branch_factor)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Prune remaining branches
        return best
    else:
        # Minimizer's turn
        best = math.inf
        for i in range(branch_factor):  # Iterate over all children
            val = alpha_beta_search(depth + 1, index * branch_factor + i, True, values, alpha, beta, target_depth, branch_factor)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Prune remaining branches
        return best

def main():
    # User Input: Values of leaf nodes
    print("Enter the values of leaf nodes separated by spaces:")
    values = list(map(int, input().split()))
    
    # User Input: Number of branches per node
    print("Enter the branching factor (number of children per node):")
    branch_factor = int(input())
    
    # Calculate depth of the game tree
    target_depth = math.log(len(values), branch_factor)
    if target_depth != int(target_depth):
        print(f"Error: The number of leaf nodes must be a power of {branch_factor}.")
        return
    
    target_depth = int(target_depth)
    
    # Run Alpha-Beta Pruning
    result = alpha_beta_search(0, 0, True, values, -math.inf, math.inf, target_depth, branch_factor)
    
    # Display the result
    print(f"The optimal value determined by Alpha-Beta Pruning is: {result}")

if __name__ == "__main__":
    main()
