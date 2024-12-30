# import math

# # Utility function to check if a player has won
# def check_winner(board, player):
#     win_conditions = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
#         [0, 4, 8], [2, 4, 6]  # diagonals
#     ]
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
#             return True
#     return False

# # Function to check if the board is full
# def is_board_full(board):
#     return not any(spot == ' ' for spot in board)

# # Evaluate the board
# def evaluate(board):
#     if check_winner(board, 'X'):
#         return 10
#     elif check_winner(board, 'O'):
#         return -10
#     else:
#         return 0

# # Minimax algorithm to find the best move
# def minimax(board, depth, is_maximizing_player):
#     score = evaluate(board)
    
#     # If maximizer wins or minimizer wins
#     if score == 10:
#         return score - depth
#     if score == -10:
#         return score + depth
    
#     # If board is full (draw)
#     if is_board_full(board):
#         return 0
    
#     if is_maximizing_player:
#         best = -math.inf
#         for i in range(9):
#             if board[i] == ' ':
#                 board[i] = 'X'  # Maximizing player (AI)
#                 best = max(best, minimax(board, depth + 1, False))
#                 board[i] = ' '  # Undo move
#         return best
#     else:
#         best = math.inf
#         for i in range(9):
#             if board[i] == ' ':
#                 board[i] = 'O'  # Minimizing player (human)
#                 best = min(best, minimax(board, depth + 1, True))
#                 board[i] = ' '  # Undo move
#         return best

# # Function to find the best move for the AI
# def find_best_move(board):
#     best_val = -math.inf
#     best_move = -1

#     for i in range(9):
#         if board[i] == ' ':
#             board[i] = 'X'  # AI is 'X'
#             move_val = minimax(board, 0, False)
#             board[i] = ' '  # Undo move
#             if move_val > best_val:
#                 best_move = i
#                 best_val = move_val

#     return best_move

# # Function to print the current board
# def print_board(board):
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")

# # Main function to run the game
# def play_game():
#     board = [' '] * 9
#     current_player = 'O'  # 'O' goes first
    
#     while True:
#         print_board(board)
        
#         if current_player == 'O':
#             # Human move (player 'O')
#             try:
#                 move = int(input("Enter your move (1-9): ")) - 1
#                 if board[move] != ' ':
#                     print("Invalid move. Try again.")
#                     continue
#                 board[move] = 'O'
#                 current_player = 'X'
#             except (ValueError, IndexError):
#                 print("Invalid input. Please enter a number between 1 and 9.")
#         else:
#             # AI move (player 'X')
#             print("AI is making its move...")
#             move = find_best_move(board)
#             board[move] = 'X'
#             current_player = 'O'
        
#         # Check if someone has won
#         if check_winner(board, 'X'):
#             print_board(board)
#             print("AI wins!")
#             break
#         elif check_winner(board, 'O'):
#             print_board(board)
#             print("You win!")
#             break
        
#         # Check if board is full (draw)
#         if is_board_full(board):
#             print_board(board)
#             print("It's a draw!")
#             break

# # Start the game
# play_game()
import math

# Utility function to check if a player has won (using the 2D board)
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    
    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    
    return False

# Function to check if the board is full
def is_board_full(board):
    return not any(spot == ' ' for row in board for spot in row)

# Evaluate the board
def evaluate(board):
    if check_winner(board, 'X'):
        return 10
    elif check_winner(board, 'O'):
        return -10
    else:
        return 0

# Minimax algorithm to find the best move
def minimax(board, depth, is_maximizing_player):
    score = evaluate(board)
    
    # If maximizer wins or minimizer wins
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    
    # If board is full (draw)
    if is_board_full(board):
        return 0
    
    if is_maximizing_player:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Maximizing player (AI)
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '  # Undo move
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Minimizing player (human)
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '  # Undo move
        return best

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  # AI is 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '  # Undo move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to print the current board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--+---+--")
        
# Main function to run the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize a 3x3 board
    current_player = 'O'  # 'O' goes first
    
    while True:
        print_board(board)
        
        if current_player == 'O':
            # Human move (player 'O')
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] != ' ':
                    print("Invalid move. Try again.")
                    continue
                board[row][col] = 'O'
                current_player = 'X'
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            # AI move (player 'X')
            print("AI is making its move...")
            row, col = find_best_move(board)
            board[row][col] = 'X'
            current_player = 'O'
        
        # Check if someone has won
        if check_winner(board, 'X'):
            print_board(board)
            print("AI wins!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("You win!")
            break
        
        # Check if board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
play_game()
