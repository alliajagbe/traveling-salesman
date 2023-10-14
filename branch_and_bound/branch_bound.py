from lowerbound import calculate_lower_bound


def tour_to_path_representation(tour):
    n = len(tour)
    path_representation = [(tour[i]) % n for i in range(n)] + [tour[0]]
    return ' '.join(map(str, path_representation))

def print_path_representation(tour):
    path_representation = tour_to_path_representation(tour)
    print(path_representation)


# Branch and Bound TSP solver
def tsp_branch_and_bound(matrix):
    n = len(matrix)
    min_cost = float('inf')
    best_tour = None
    all_tours = []

    # Initialize the root node
    root_node = (0, [0], 0)

    # Initialize priority queue for the nodes to be explored
    nodes_to_explore = [root_node]

    while nodes_to_explore:
        # Pop the node with the lowest lower bound
        current_node = min(nodes_to_explore, key=lambda x: x[2])
        nodes_to_explore.remove(current_node)

        current_city, current_path, current_cost = current_node

        # If the path includes all cities, update the best tour
        if len(current_path) == n:
            current_cost += matrix[current_path[-1]][current_path[0]]
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_path
                print("New best tour found with cost", min_cost)

            all_tours.append(current_path)

        # Explore child nodes
        for city in range(n):
            if city not in current_path:
                lower_bound = calculate_lower_bound(matrix, current_path + [city])
                if lower_bound < min_cost:
                    nodes_to_explore.append((city, current_path + [city], current_cost + matrix[current_city][city]))

    # Print all paths except the last (optimal) one
    for path in all_tours:
        print_path_representation(path)

    best_tour = tour_to_path_representation(best_tour)

    return best_tour, min_cost