import random
import math


def simulated_annealing(dist_matrix):
    num_cities = len(dist_matrix)
    initial_temp = 1000  # Начальная температура
    cooling_rate = 0.995  # Коэффициент охлаждения
    max_iterations = 10000
    def route_length(route):
        return sum(dist_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + dist_matrix[route[-1]][route[0]]

    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_length = route_length(current_route)

    best_route = current_route
    best_length = current_length

    current_temp = initial_temp

    for iteration in range(max_iterations):
        new_route = current_route[:]
        i, j = random.sample(range(num_cities), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_length = route_length(new_route)

        if new_length < current_length or random.random() < math.exp((current_length - new_length) / current_temp):
            current_route = new_route
            current_length = new_length

            if new_length < best_length:
                best_route = new_route
                best_length = new_length

        # Уменьшение температуры
        current_temp *= cooling_rate

    return best_route, best_length