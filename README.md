
---

## Algorithms

### Depth‑First Search (DFS)
- Backtracking search
- Always finds a valid solution if one exists
- Not practical for large N due to exponential growth

### Hill Climbing
- Greedy local search that reduces conflicts
- Very fast for small and medium N
- Can get stuck in local minima

### Simulated Annealing
- Probabilistic search with a temperature schedule
- Can escape local minima
- Sensitive to parameter choices (cooling rate, iterations)

### Genetic Algorithm
- Population‑based evolutionary approach
- Uses selection, crossover, and mutation
- Works well for small N, may converge prematurely for large N

---

## Summary of Results (Example)

| N   | DFS | HC | SA | GA |
|-----|-----|----|----|----|
| 10  | ✔   | ✔  | ✔  | ✔  |
| 30  | ❌  | ✔  | ✔  | ✔  |
| 50  | ❌  | ✔  | ❌ | ❌ |
| 100 | ❌  | ❌ | ❌ | ❌ |

*(These are representative outcomes based on typical runs without heavy tuning.)*

---

## Running the Code

From the project directory:

---

## 📄 Report

The full written report (IEEE style) is available in Overleaf:

👉 **Overleaf link:** [insert your Overleaf link here]

---

## 👤 Author

**Name:** Ashik Kirmani  
**Email:** akashikkirmani@gmail.com  
**University:** University of Europe for Applied Sciences, Potsdam

```bash
python dfs_nqueens.py
python hillclimbing_nqueens.py
python simulatedannealing_nqueens.py
python genetic_nqueens.py
