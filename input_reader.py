def read_euclidean_input():
    N = int(input())
    cities = []
    for _ in range(N):
        x, y = map(float, input().split())
        cities.append((x, y))
    return cities

def read_non_euclidean_input():
    N = int(input())
    distance_matrix = []
    for _ in range(N):
        distances = list(map(float, input().split()))
        distance_matrix.append(distances)
    return distance_matrix