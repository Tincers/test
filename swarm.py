import numpy as np


class Particle:
    def __init__(self, num_cities):
        self.position = np.random.permutation(num_cities)
        self.velocity = np.random.uniform(size=num_cities)
        self.best_position = np.copy(self.position)
        self.best_score = float('inf')


def calculate_distance(matrix, route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += matrix[route[i]][route[i + 1]]
    total_distance += matrix[route[-1]][route[0]]
    return total_distance


def pso_tsp(matrix, num_particles, num_iterations):
    num_cities = len(matrix)
    particles = [Particle(num_cities) for _ in range(num_particles)]
    global_best_position = None
    global_best_score = float('inf')

    for iteration in range(num_iterations):
        for particle in particles:
            current_score = calculate_distance(matrix, particle.position)
            if current_score < particle.best_score:
                particle.best_position = np.copy(particle.position)
                particle.best_score = current_score

            if current_score < global_best_score:
                global_best_position = np.copy(particle.position)
                global_best_score = current_score

        for particle in particles:
            inertia_weight = 0.5
            cognitive_weight = 1.5
            social_weight = 1.5

            r1 = np.random.random(size=num_cities)
            r2 = np.random.random(size=num_cities)

            particle.velocity = (inertia_weight * particle.velocity +
                                 cognitive_weight * r1 * (particle.best_position - particle.position) +
                                 social_weight * r2 * (global_best_position - particle.position))

            particle.position = np.argsort(particle.position + particle.velocity)

    return global_best_position, global_best_score
