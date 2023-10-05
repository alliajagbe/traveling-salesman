def read_euclidean_input():
    N = int(input())
    cities = []
    for _ in range(N):
        x, y = map(float, input().split())
        cities.append((x, y))
    return cities