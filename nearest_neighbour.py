from distance import calculate_tour_distance

def nearest_neighbor(matrix):
    num_cities = len(matrix)
    tour = [0]  # Start from city 0
    unvisited_cities = set(range(1, num_cities))
    
    current_city = 0
    best_tour = [current_city]
    best_distance = 0

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city
        best_distance += matrix[tour[-2]][tour[-1]]

    # Return to the starting city
    tour.append(tour[0])
    best_distance += matrix[tour[-2]][tour[-1]]
    
    if best_distance < calculate_tour_distance(best_tour, matrix):
        return tour
    else:
        return best_tour