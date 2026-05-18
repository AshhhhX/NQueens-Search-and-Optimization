import time
import tracemalloc


class DFSNQueens:

    def __init__(self, n):
        self.n = n
        self.board = [-1] * n

        # Start time
        self.start_time = time.time()

        # 6 hours = 21600 seconds
        self.time_limit = 21600

    # Check if a queen can be placed at (row, col)
    def is_safe(self, row, col):
        for r in range(row):
            # Same column
            if self.board[r] == col:
                return False
            # Diagonal attack
            if abs(self.board[r] - col) == abs(r - row):
                return False
        return True

    # DFS Backtracking
    def solve(self, row=0):

        # Timeout check
        if time.time() - self.start_time > self.time_limit:
            return "TIMEOUT"

        # All queens placed
        if row == self.n:
            return True

        # Try each column
        for col in range(self.n):

            # Timeout check inside loop
            if time.time() - self.start_time > self.time_limit:
                return "TIMEOUT"

            if self.is_safe(row, col):
                self.board[row] = col

                result = self.solve(row + 1)

                if result is True:
                    return True
                if result == "TIMEOUT":
                    return "TIMEOUT"

                # Backtrack
                self.board[row] = -1

        return False


# Run DFS for required N values
if __name__ == "__main__":

    n_values = [10, 30, 50, 100, 200, 500]

    for n in n_values:

        tracemalloc.start()
        start = time.time()

        solver = DFSNQueens(n)
        result = solver.solve()

        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print("\n======================")
        print("N =", n)
        print("======================")

        if result is True:
            print("Solved Successfully")
            print("Board:", solver.board)

        elif result == "TIMEOUT":
            print("Execution exceeded 6 hours")
            print("DFS could not solve this N value")

        else:
            print("No Solution Found")

        print("Execution Time:", round(end - start, 4), "seconds")
        print("Peak Memory:", round(peak / 1024, 2), "KB")
