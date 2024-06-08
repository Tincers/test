import math
import numpy as np
from geopy.geocoders import Nominatim

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = calculate_distance(coords[i], coords[j])
    return dist_matrix


def get_coordinates(city_names):
    geolocator = Nominatim(user_agent="tsp_solver")
    coords = []
    for city in city_names:
        location = geolocator.geocode(city)
        if location:
            coords.append((location.latitude, location.longitude))
        else:
            raise ValueError(f"Город '{city}' не найден")
    return coords


def solve_tsp(city_names):
    coords = get_coordinates(city_names)
    dist_matrix = create_distance_matrix(coords)
    return dist_matrix