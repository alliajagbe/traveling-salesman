from distance import calculate_tour_length

def nearest_neighbor(matrix):
    num_cities = len(matrix)
    best_tour = None
    best_distance = float('inf') # initializing distance to infinity

    for start_city in range(num_cities):
        tour = [start_city]
        unvisited_cities = set(range(num_cities))
        unvisited_cities.remove(start_city)
        current_city = start_city

        while unvisited_cities:
            nearest_city = min(unvisited_cities, key=lambda city: matrix[current_city][city])
            tour.append(nearest_city)
            unvisited_cities.remove(nearest_city)
            current_city = nearest_city

        # Return to the starting city
        tour.append(start_city)
        tour_distance = calculate_tour_length(tour, matrix)

        if tour_distance < best_distance:
            best_distance = tour_distance
            best_tour = tour

    return best_tour
