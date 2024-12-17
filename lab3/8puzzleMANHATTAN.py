Using Manhattan Distance
class SlidingPuzzleSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_i = (state[i][j] - 1) // 3
                    goal_j = (state[i][j] - 1) % 3
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def get_neighbors(self, state):
        i, j = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
        moves = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        return [self.swap(state, i, j, x, y) for x, y in moves if 0 <= x < 3 and 0 <= y < 3]

    def swap(self, state, i1, j1, i2, j2):
        new_state = [row[:] for row in state]
        new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
        return new_state

    def dfs_with_manhattan(self, state, visited=set()):
        if state == self.goal_state:
            return [state]
        visited.add(str(state))
        neighbors = sorted(self.get_neighbors(state), key=lambda x: self.manhattan_distance(x))
        for neighbor in neighbors:
            if str(neighbor) not in visited:
                path = self.dfs_with_manhattan(neighbor, visited)
                if path:
                    return [state] + path
        return None

    def solve(self):
        solution = self.dfs_with_manhattan(self.initial_state)
        return solution


initial_state = [[int(x) for x in input(f"Enter row {i + 1}: ").split()] for i in range(3)]
solver = SlidingPuzzleSolver(initial_state)
solution = solver.solve()

if solution:
    print("Solution found:")
    for state in solution:
        print(*state, sep='\n', end='\n\n')
else:
    print("No solution found.")
