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