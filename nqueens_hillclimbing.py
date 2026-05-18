import random
import time
import tracemalloc


class HillClimbingNQueens:

    def __init__(self, n):

        self.n = n

        # random initial board
        self.board = [
            random.randint(0, n - 1)
            for _ in range(n)
        ]

    def conflicts(self, board):

        attacks = 0

        for i in range(self.n):

            for j in range(i + 1, self.n):

                # same column
                if board[i] == board[j]:
                    attacks += 1

                # diagonal attack
                elif abs(board[i] - board[j]) == abs(i - j):
                    attacks += 1

        return attacks

    def solve(self, max_steps=5000):

        current = self.board[:]

        for step in range(max_steps):

            current_conflicts = self.conflicts(current)

            # solution found
            if current_conflicts == 0:
                return current

            best_board = current[:]
            best_conflicts = current_conflicts

            # try improving board
            for row in range(self.n):

                original = current[row]

                for col in range(self.n):

                    current[row] = col

                    new_conflicts = self.conflicts(current)

                    if new_conflicts < best_conflicts:

                        best_conflicts = new_conflicts
                        best_board = current[:]

                current[row] = original

            # local minimum -> random restart
            if best_conflicts >= current_conflicts:

                current = [
                    random.randint(0, self.n - 1)
                    for _ in range(self.n)
                ]

            else:
                current = best_board

        return None


n_values = [10, 30, 50, 100]

for n in n_values:

    tracemalloc.start()

    start = time.time()

    solver = HillClimbingNQueens(n)

    result = solver.solve()

    end = time.time()

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print("\nN =", n)

    print("Solved:", result is not None)

    if result is not None:
        print("Board:", result)

    print("Execution Time:", end - start)

    print("Memory Usage (KB):", peak_memory / 1024)