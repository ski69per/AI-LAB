import random

def heuristic(state):
    attacks = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def hill_climbing_8_queens():
    state = [random.randint(0, 7) for _ in range(8)]  # Random initial state
    while True:
        current_h = heuristic(state)
        if current_h == 0:  # Found a solution
            return state
       
        next_state = None
        next_h = float('inf')

        for col in range(8):
            for row in range(8):
                if state[col] != row:  # Only consider moving the queen
                    new_state = state.copy()
                    new_state[col] = row
                    h = heuristic(new_state)
                    if h < next_h:
                        next_h = h
                        next_state = new_state

        if next_h >= current_h:  # No better neighbor found
            return None  # Stuck at local maximum
        state = next_state

solution = hill_climbing_8_queens()
print("Hill Climbing solution:", solution)
