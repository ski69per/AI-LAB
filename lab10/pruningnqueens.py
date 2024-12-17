import math
from copy import deepcopy

# Define the Tic-Tac-Toe board size and players
EMPTY = "-"
PLAYER_X = "X"  # Maximizing player (Computer)
PLAYER_O = "O"  # Minimizing player (User)

# Helper functions
def is_terminal(board):
    """Checks if the game has ended."""
    winner = get_winner(board)
    if winner or not any(EMPTY in row for row in board):
        return True
    return False

def get_winner(board):
    """Checks for a winner on the board."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def utility(board):
    """Returns the utility of a terminal state."""
    winner = get_winner(board)
    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    return 0

def get_actions(board):
    """Returns a list of possible moves."""
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions

def result(board, action, player):
    """Returns the board resulting from applying an action."""
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player
    return new_board

# Alpha-Beta Search
def alpha_beta_search(board):
    """Performs Alpha-Beta Pruning to find the best action."""
    alpha = -math.inf
    beta = math.inf
    best_action = None

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility(state)
        v = -math.inf
        for action in get_actions(state):
            v = max(v, min_value(result(state, action, PLAYER_X), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility(state)
        v = math.inf
        for action in get_actions(state):
            v = min(v, max_value(result(state, action, PLAYER_O), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    for action in get_actions(board):
        value = min_value(result(board, action, PLAYER_X), alpha, beta)
        if value > alpha:
            alpha = value
            best_action = action

    return best_action

# Game loop
def print_board(board):
    """Displays the board."""
    for row in board:
        print(" | ".join(row))
    print()

def play_game():
    """Runs the Tic-Tac-Toe game with user input."""
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', and the computer is 'X'.")
    print_board(board)

    while not is_terminal(board):
        # User's turn
        user_move = None
        while user_move not in get_actions(board):
            try:
                print("Your turn! Enter your move as 'row col' (e.g., '1 2'):")
                row, col = map(int, input().split())
                user_move = (row - 1, col - 1)  # Convert to 0-based index
                if user_move not in get_actions(board):
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space.")
        
        board = result(board, user_move, PLAYER_O)
        print("You played:")
        print_board(board)

        if is_terminal(board):
            break

        # Computer's turn
        print("Computer's turn...")
        computer_move = alpha_beta_search(board)
        board = result(board, computer_move, PLAYER_X)
        print("Computer played:")
        print_board(board)

    # Game over
    winner = get_winner(board)
    if winner == PLAYER_X:
        print("Computer wins!")
    elif winner == PLAYER_O:
        print("Congratulations! You win!")
    else:	
        print("It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()

