import random
import numpy as np
import time


class AntColony:
    def __init__(self, dist_matrix, colony_size=10, generations=500, alpha=1.0, beta=2.0, rho=0.5, q=10):
        self.dist_matrix = dist_matrix
        self.colony_size = colony_size
        self.generations = generations
        self.alpha = alpha  # вес феромона
        self.beta = beta  # вес расстояния
        self.rho = rho  # коэффициент испарения феромона
        self.q = q  # количество феромона, откладываемого муравьем
        self.num_cities = len(dist_matrix)
        self.pheromone_matrix = np.ones_like(dist_matrix)  # начальное количество феромона на каждом ребре

    def run(self):
        best_route = None
        best_distance = float('inf')
        start_time = time.time()

        for gen in range(self.generations):
            all_ant_routes = self.gen_all_ant_routes()
            self.update_pheromone(all_ant_routes)

            current_best_route, current_best_distance = self.get_best_route(all_ant_routes)

            if current_best_distance < best_distance:
                best_route, best_distance = current_best_route, current_best_distance

        return best_route, best_distance

    def gen_ant_route(self, start_city):
        route = []
        visited = set()
        current_city = start_city
        visited.add(current_city)

        while len(visited) < self.num_cities:
            probs = self.gen_probs(current_city, visited)
            next_city = self.choose_next_city(probs, visited)
            route.append((current_city, next_city))
            current_city = next_city
            visited.add(current_city)

        route.append((current_city, route[0][0]))  # go back to start
        return route

    def gen_all_ant_routes(self):
        return [self.gen_ant_route(i) for i in range(self.num_cities)]

    def gen_probs(self, current_city, visited):
        pheromone = np.copy(self.pheromone_matrix[current_city])
        pheromone[list(visited)] = 0

        distance = self.dist_matrix[current_city].copy()
        distance[list(visited)] = np.inf

        # Calculate probabilities
        probabilities = np.zeros(self.num_cities)
        for i in range(self.num_cities):
            if i not in visited and distance[i] != 0:  # проверка на ноль в знаменателе
                probabilities[i] = (pheromone[i] ** self.alpha) * ((1.0 / distance[i]) ** self.beta)

        # Normalize probabilities
        total = np.sum(probabilities)
        if total > 0:
            probabilities /= total
        else:
            # If all probabilities are zero, return equal probabilities
            probabilities = np.ones(self.num_cities) / self.num_cities

        return probabilities

    def choose_next_city(self, probs, visited):
        # Randomly choose the next city based on probabilities
        if np.isnan(probs).any():
            # If probabilities contain NaNs, choose randomly from unvisited cities
            unvisited = [i for i in range(self.num_cities) if i not in visited]
            return random.choice(unvisited)
        else:
            # Otherwise, choose according to probabilities
            return np.random.choice(self.num_cities, 1, p=probs)[0]

    def update_pheromone(self, all_ant_routes):
        # Initialize pheromone_delta matrix
        pheromone_delta = np.zeros_like(self.pheromone_matrix)

        # Update pheromone_delta with each ant's contribution
        for path in all_ant_routes:
            for move in path:
                pheromone_delta[move] += self.q / self.dist_matrix[move]

        # Update global pheromone_matrix using rho
        self.pheromone_matrix = (1 - self.rho) * self.pheromone_matrix + pheromone_delta

    def get_best_route(self, all_ant_routes):
        best_distance = float('inf')
        best_route = None
        for route in all_ant_routes:
            total_distance = sum([self.dist_matrix[i][j] for i, j in route])
            if total_distance < best_distance:
                best_distance = total_distance
                best_route = route
        return best_route, best_distance