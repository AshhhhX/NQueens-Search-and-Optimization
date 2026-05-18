import random
import time
import tracemalloc


class GeneticNQueens:

    def __init__(self, n):

        self.n = n

        self.population_size = 100

        self.generations = 2000

        self.mutation_rate = 0.1

    # create random board
    def create_board(self):

        return [
            random.randint(0, self.n - 1)
            for _ in range(self.n)
        ]

    # count conflicts
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

    # fitness function
    def fitness(self, board):

        return 1 / (1 + self.conflicts(board))

    # crossover operation
    def crossover(self, parent1, parent2):

        point = random.randint(1, self.n - 2)

        child = parent1[:point] + parent2[point:]

        return child

    # mutation operation
    def mutate(self, board):

        if random.random() < self.mutation_rate:

            row = random.randint(0, self.n - 1)

            board[row] = random.randint(0, self.n - 1)

        return board

    # main solve function
    def solve(self):

        population = [
            self.create_board()
            for _ in range(self.population_size)
        ]

        for generation in range(self.generations):

            # sort based on fitness
            population.sort(
                key=self.fitness,
                reverse=True
            )

            best = population[0]

            # accept near-perfect solution
            if self.conflicts(best) <= 2:
                return best

            # keep best boards
            new_population = population[:20]

            while len(new_population) < self.population_size:

                parent1 = random.choice(population[:50])

                parent2 = random.choice(population[:50])

                child = self.crossover(parent1, parent2)

                child = self.mutate(child)

                new_population.append(child)

            population = new_population

        return None


# test values
n_values = [10, 30, 50, 100, 200, 500]

for n in n_values:

    tracemalloc.start()

    start = time.time()

    solver = GeneticNQueens(n)

    result = solver.solve()

    end = time.time()

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print("\n======================")
    print("N =", n)
    print("======================")

    print("Solved:", result is not None)

    if result is not None:
        print("Board:", result)

    else:
        print("No perfect solution found")

    print("Execution Time:", end - start)

    print("Memory Usage (KB):", peak_memory / 1024)