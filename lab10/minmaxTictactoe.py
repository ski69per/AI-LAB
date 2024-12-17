import math

def is_terminal(state, n):
    """Check if the board is a valid solution (no conflicts, all queens placed)."""
    return len(state) == n

def count_conflicts(state):
    """Calculate the number of conflicts between queens."""
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            # Same column or diagonal conflicts
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def utility(state):
    """Return a utility score based on the number of conflicts (higher is better)."""
    return -count_conflicts(state)

def actions(state, n):
    """Generate possible next moves."""
    next_row = len(state)
    if next_row >= n:
        return []
    return [state + [col] for col in range(n)]

def max_value(state, alpha, beta, n):
    """Maximizing function."""
    if is_terminal(state, n):
        return utility(state)
    v = -math.inf
    for action in actions(state, n):
        v = max(v, min_value(action, alpha, beta, n))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(state, alpha, beta, n):
    """Minimizing function."""
    if is_terminal(state, n):
        return utility(state)
    v = math.inf
    for action in actions(state, n):
        v = min(v, max_value(action, alpha, beta, n))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alpha_beta_search(n):
    """Perform Alpha-Beta pruning to solve the N-Queens problem."""
    alpha = -math.inf
    beta = math.inf
    best_action = None
    initial_state = []

    for action in actions(initial_state, n):
        value = min_value(action, alpha, beta, n)
        if value > alpha:
            alpha = value
            best_action = action

    return best_action

# Example usage
if __name__ == "__main__":
    n = 8  # Number of queens
    solution = alpha_beta_search(n)
    if solution:
        print("Solution:", solution)
    else:
        print("No solution found.")

