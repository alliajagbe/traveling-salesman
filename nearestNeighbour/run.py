from input_reader import read_input
from distance import calculate_tour_length
from nearest_neighbour import nearest_neighbor

def main():
    input_file = "200.txt"
    tsp_type, N, cities, distances = read_input(input_file)

    best_tour = nearest_neighbor(distances)
    print("PATH REPRESENTATION OF TOUR:")
    print(" ".join(map(str, best_tour)))

    print("TOUR LENGTH:")
    print(calculate_tour_length(best_tour, distances))

if __name__ == "__main__":
    main()