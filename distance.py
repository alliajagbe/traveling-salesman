import math 
def calculate_euclidean(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        total_distance += distance_matrix[from_city][to_city]
    return total_distance
