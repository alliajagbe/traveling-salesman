# Function to calculate the lower bound of a node's cost using the minimum edge values
def calculate_lower_bound(matrix, path):
    bound = 0

    # Add the cost of the edges in the path
    for i in range(len(path) - 1):
        bound += matrix[path[i]][path[i + 1]]

    # Add the cost of the minimum edge connecting the last city to the starting city
    bound += matrix[path[-1]][path[0]]

    # Reduce the bound by subtracting the minimum edge value for each city
    for i in range(len(matrix)):
        if i not in path:
            bound += min(matrix[i])

    return bound