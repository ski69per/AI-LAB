 
class SlidingPuzzle:
    def __init__(self, board, empty_pos, path=[]):
        self.board = board
        self.empty_pos = empty_pos
        self.path = path

    def is_solved(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_moves(self):
        x, y = self.empty_pos
        possible_moves = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board[:]
                new_board[x * 3 + y], new_board[nx * 3 + ny] = new_board[nx * 3 + ny], new_board[x * 3 + y]
                possible_moves.append((new_board, (nx, ny)))
        return possible_moves

def depth_first_search(initial_puzzle):
    stack, visited = [initial_puzzle], set()
    while stack:
        current_puzzle = stack.pop()
        if current_puzzle.is_solved():
            return current_puzzle.path
        visited.add(tuple(current_puzzle.board))
        for new_board, new_empty_pos in current_puzzle.get_moves():
            new_state = SlidingPuzzle(new_board, new_empty_pos, current_puzzle.path + [new_board])
            if tuple(new_board) not in visited:
                stack.append(new_state)
    return None

def display_board(board):
    for i in range(0, 9, 3):
        print(board[i:i + 3])
    print()

def main():
    initial_board = [1, 2, 3, 4, 0, 5, 7, 8, 6]
    empty_pos = initial_board.index(0)
    initial_puzzle = SlidingPuzzle(initial_board, (empty_pos // 3, empty_pos % 3))
    
    print("Initial state:")
    display_board(initial_board)
    
    solution = depth_first_search(initial_puzzle)
    
    if solution:
        print("Solution found:")
        for step in solution:
            display_board(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
