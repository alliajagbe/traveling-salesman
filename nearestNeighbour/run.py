from input_reader import read_input
from distance import calculate_euclidean, calculate_tour_distance
from nearest_neighbour import nearest_neighbor
import numpy as np

def main():
    input_file = "200.txt"
    tsp_type, N, cities, distances = read_input(input_file)

    best_tour = nearest_neighbor(distances)
    print("PATH REPRESENTATION OF TOUR:")
    print(" ".join(map(str, best_tour)))

if __name__ == "__main__":
    main()