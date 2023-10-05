from distance import calculate_tour_distance

def nearest_neighbor(matrix):
    num_cities = len(matrix)
    tour = [0]  # Start from city 0
    unvisited_cities = set(range(1, num_cities))
    
    current_city = 0
    best_tour = None
    best_distance = float('inf')

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

        # Calculate the tour distance so far
        tour_distance = calculate_tour_distance(tour, matrix)
        
        # If this tour is better than the best one so far, update it
        if tour_distance < best_distance:
            best_distance = tour_distance
            best_tour = tour.copy()

    # Return to the starting city
    best_tour.append(best_tour[0])
    
    return best_tour