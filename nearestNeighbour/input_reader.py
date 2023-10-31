def read_input(file_path):
    with open(file_path, 'r') as file:
        tsp_type = file.readline().strip()
        N = int(file.readline())
        cities = []
        for _ in range(N):
            x, y = map(float, file.readline().split())
            cities.append((x, y))
        distances = []
        for _ in range(N):
            distances.append(list(map(float, file.readline().split())))
        return tsp_type, N, cities, distances

def read_input_from_terminal():
    tsp_type = input().strip()
    N = int(input())
    cities = []
    distances = []

    for i in range(N):
        x, y = map(float, input().split())
        cities.append((x, y))

    for i in range(N):
        row = list(map(float, input().split()))
        distances.append(row)

    return tsp_type, N, cities, distances

tsp_type, N, cities, distances = read_input_from_terminal()
print(tsp_type)
print(N)
print(cities)
print(distances)