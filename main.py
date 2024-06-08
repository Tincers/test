import logging
from genetic_algorithm import GeneticAlgorithm
import tracemalloc
from dynamic import tsp_dp
from ant_colony import AntColony
from print_logging import log
from deff import solve_tsp
from Immune import ImmuneAlgorithmTSP
from Simulated_Annealing import simulated_annealing
import time

# Общий

city_names = ["Черкассы", "Киев", "Сумы", "Луцк", "Мелитополь", "Никополь", "Славянск", "Полтава", "Николаев"]

#Динамическое

tracemalloc.start()
try:
    start_time = time.time()
    result = tsp_dp(solve_tsp(city_names))
    elapsed_time = time.time() - start_time
except ValueError as e:
    logging.error(e)
    raise
current, peak = tracemalloc.get_traced_memory()
log("Динамический", result, current, peak, elapsed_time)


#Генетический

tracemalloc.start()
try:
    start_time = time.time()
    ga = GeneticAlgorithm(solve_tsp(city_names))
    best_distance = ga.evolve()
    elapsed_time = time.time() - start_time
except ValueError as e:
    logging.error(e)
    raise
current, peak = tracemalloc.get_traced_memory()
log("Генетический", result, current, peak, elapsed_time)
tracemalloc.stop()


#Муравьиный

tracemalloc.start()
try:
    start_time = time.time()
    ant_colony = AntColony(solve_tsp(city_names))
    best_route, result = ant_colony.run()
    elapsed_time = time.time() - start_time
except ValueError as e:
    logging.error(e)
    raise
current, peak = tracemalloc.get_traced_memory()
log("Муравьиный", result, current, peak, elapsed_time)
tracemalloc.stop()

#Имунный

tracemalloc.start()
try:
    start_time = time.time()
    immune_algorithm = ImmuneAlgorithmTSP(solve_tsp(city_names))
    best_route, best_distance = immune_algorithm.run()
    elapsed_time = time.time() - start_time
except ValueError as e:
    logging.error(e)
    raise
current, peak = tracemalloc.get_traced_memory()
log("Имунний", result, current, peak, elapsed_time)
tracemalloc.stop()

#Ройовий

tracemalloc.start()
try:
    start_time = time.time()
    immune_algorithm = ImmuneAlgorithmTSP(solve_tsp(city_names))
    best_route, best_distance = immune_algorithm.run()
    elapsed_time = time.time() - start_time
except ValueError as e:
    logging.error(e)
    raise
current, peak = tracemalloc.get_traced_memory()
log("Имунний", result, current, peak, elapsed_time)
tracemalloc.stop()

#Отжимания
tracemalloc.start()
try:
    start_time = time.time()
    best_route, best_distance = simulated_annealing(solve_tsp(city_names))
    elapsed_time = time.time() - start_time
except ValueError as e:
    logging.error(e)
    raise
current, peak = tracemalloc.get_traced_memory()
log("Отжимания", result, current, peak, elapsed_time)
tracemalloc.stop()