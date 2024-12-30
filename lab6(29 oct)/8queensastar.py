# import heapq
# import random

# # Heuristic function: Count the number of conflicts in the current state
# def calculate_cost(state):
#     cost = 0
#     n = len(state)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
#                 cost += 1
#     return cost

# # Generate all possible neighbors (states) by moving a queen in its column
# def get_neighbors(state):
#     neighbors = []
#     n = len(state)
#     for col in range(n):
#         for row in range(n):
#             if state[col] != row:  # Move the queen in column `col` to a different row
#                 new_state = list(state)
#                 new_state[col] = row
#                 neighbors.append(new_state)
#     return neighbors

# # A* algorithm for the 8-Queens problem
# def a_star(n=8, max_iterations=1000):
#     initial_state = [random.randint(0, n-1) for _ in range(n)]
#     initial_cost = calculate_cost(initial_state)
#     # The priority queue stores elements in the form (f_score, state, g_score)
#     open_list = []
#     heapq.heappush(open_list, (initial_cost, initial_state, 0))  # f_score = g_score + h_score, where g_score is the path cost (depth)
#     closed_list = set()
    
#     while open_list:
#         # Get the state with the lowest f_score
#         f_score, current_state, g_score = heapq.heappop(open_list)
        
#         if f_score == 0:  # Goal state found
#             return current_state
        
#         # Add current state to closed list
#         closed_list.add(tuple(current_state))
        
#         # Generate neighbors and calculate their f_score
#         neighbors = get_neighbors(current_state)
#         for neighbor in neighbors:
#             if tuple(neighbor) in closed_list:
#                 continue  # Skip if the state is already visited
            
#             h_score = calculate_cost(neighbor)  # Heuristic cost (number of conflicts)
#             new_g_score = g_score + 1  # The path cost (depth)
#             new_f_score = new_g_score + h_score  # f_score = g_score + h_score
            
#             # Add the new state to the open list
#             heapq.heappush(open_list, (new_f_score, neighbor, new_g_score))
    
#     print(f"Max iterations reached without finding a solution.")
#     return None

# # Run A* to solve the 8-Queens problem
# solution = a_star()
# if solution:
#     print(f"Solution found: {solution}")
# else:
#     print("No solution found.")
import heapq

# Helper function to calculate the heuristic (number of conflicts)
def heuristic(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# A* Search for 8-queens
def a_star_8_queens():
    n = 8
    open_set = []
    # Initial state: empty board
    heapq.heappush(open_set, (0, []))  # (f, board)
    
    while open_set:
        f, board = heapq.heappop(open_set)
        
        # Goal check
        if len(board) == n and heuristic(board) == 0:
            return board
        
        # Generate successors
        row = len(board)
        for col in range(n):
            new_board = board + [col]
            if heuristic(new_board) == 0:  # No conflicts so far
                g = row + 1
                h = heuristic(new_board)
                heapq.heappush(open_set, (g + h, new_board))


    return None  # No solution found

# Run A* search
solution = a_star_8_queens()
print("Solution board (column positions for each row):", solution)
