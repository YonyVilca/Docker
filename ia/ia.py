import numpy as np

current_solution = np.array([0, 1, 2, 3])
np.random.shuffle(current_solution)

def fitness(sol):
  distance = 0
  for i in range(len(sol)-1):
    distance += distances[sol[i]][sol[i+1]]
  return distance

def get_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(current_solution):
    while True:
        print("procesando...", current_solution)
        neighbors = get_neighbors(current_solution)
        best_neighbor = min(neighbors, key=fitness)  

        if fitness(current_solution) < fitness(best_neighbor):
            break
        else:
            current_solution = best_neighbor

    return current_solution

result = hill_climbing(current_solution)
print("Resultado final:", result)
