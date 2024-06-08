import numpy as np


class ImmuneAlgorithmTSP:
    def __init__(self, distance_matrix, population_size=50, generations=100, mutation_rate=0.2):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = [np.random.permutation(self.num_cities) for _ in range(population_size)]

    def calculate_fitness(self, route):
        total_distance = 0
        for i in range(self.num_cities - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        total_distance += self.distance_matrix[route[-1]][route[0]]  # Замикання маршруту
        return total_distance

    def clone_and_mutate(self, route):
        cloned_routes = [np.copy(route) for _ in range(int(self.mutation_rate * self.num_cities))]
        for cloned_route in cloned_routes:
            idx1, idx2 = np.random.choice(self.num_cities, size=2, replace=False)
            cloned_route[idx1], cloned_route[idx2] = cloned_route[idx2], cloned_route[idx1]
        return cloned_routes

    def evolve_generation(self):
        new_population = []
        for route in self.population:
            clones = self.clone_and_mutate(route)
            new_population.extend(clones)
        sorted_population = sorted(new_population, key=lambda x: self.calculate_fitness(x))
        self.population = sorted_population[:self.population_size]

    def run(self):
        for generation in range(self.generations):
            self.evolve_generation()
            best_route = min(self.population, key=lambda x: self.calculate_fitness(x))

        best_route = min(self.population, key=lambda x: self.calculate_fitness(x))
        best_distance = self.calculate_fitness(best_route)
        return best_route, best_distance