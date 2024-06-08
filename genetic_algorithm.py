import random

class GeneticAlgorithm:
    def __init__(self, dist_matrix, population_size=100, generations=500, mutation_rate=0.01):
        self.dist_matrix = dist_matrix
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.num_cities = len(dist_matrix)
        self.population = self.initialize_population()
        self.best_route = None
        self.best_distance = float('inf')

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            route = list(range(self.num_cities))
            random.shuffle(route)
            population.append(route)
        return population

    def evaluate(self, route):
        return sum(self.dist_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + self.dist_matrix[route[-1]][route[0]]

    def selection(self):
        scores = [(route, self.evaluate(route)) for route in self.population]
        scores.sort(key=lambda x: x[1])
        selected = [route for route, score in scores[:self.population_size // 2]]
        self.best_route, self.best_distance = scores[0]
        return selected

    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(self.num_cities), 2))
        child = [None] * self.num_cities
        child[start:end + 1] = parent1[start:end + 1]
        pointer = 0
        for i in range(self.num_cities):
            if child[i] is None:
                while parent2[pointer] in child:
                    pointer += 1
                child[i] = parent2[pointer]
        return child

    def mutate(self, route):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.num_cities), 2)
            route[i], route[j] = route[j], route[i]

    def evolve(self):
        for generation in range(self.generations):
            selected = self.selection()
            self.population = []
            while len(self.population) < self.population_size:
                parent1, parent2 = random.sample(selected, 2)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                self.population.append(child)
        return self.best_route, self.best_distance