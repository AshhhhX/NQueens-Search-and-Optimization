import random
import math
import time
import tracemalloc


class SimulatedAnnealingNQueens:

    def __init__(self, n):
        self.n = n

    def compute_conflicts(self, board):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def solve(self):
        board = [random.randint(0, self.n - 1) for _ in range(self.n)]
        current_conf = self.compute_conflicts(board)

        T = 1.0
        cooling = 0.9993

        while T > 1e-6:
            if current_conf == 0:
                return True, board

            row = random.randint(0, self.n - 1)
            new_col = random.randint(0, self.n - 1)

            new_board = board[:]
            new_board[row] = new_col

            new_conf = self.compute_conflicts(new_board)

            delta = new_conf - current_conf

            if delta < 0 or random.random() < math.exp(-delta / T):
                board = new_board
                current_conf = new_conf

            T *= cooling

        return False, None


if __name__ == "__main__":

    n_values = [10, 30, 50, 100, 200, 500]

    for n in n_values:
        tracemalloc.start()
        start = time.time()

        solver = SimulatedAnnealingNQueens(n)
        solved, board = solver.solve()

        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print("\n====================")
        print("N =", n)
        print("====================")

        print("Solved:", solved)
        if solved:
            print("Board:", board)

        print("Execution Time:", end - start)
        print("Memory Usage (KB):", peak / 1024)
