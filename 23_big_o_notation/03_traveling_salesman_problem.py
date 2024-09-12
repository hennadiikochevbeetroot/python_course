import itertools


# Function to calculate the distance between two cities
def calculate_distance(city1: int, city2: int, distances: list[list[int]]) -> int:
    return distances[city1][city2]


# Function to calculate the total distance of a given path
def calculate_total_distance(path: tuple[int, ...], distances: list[list[int]]) -> int:
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += calculate_distance(path[i], path[i + 1], distances)
    # Add the return trip to the starting point
    total_distance += calculate_distance(path[-1], path[0], distances)
    return total_distance


# Function to find the shortest path using brute force (factorial complexity)
def traveling_salesman_bruteforce(distances: list[list[int]]) -> tuple[tuple[int, ...], int]:
    num_cities = len(distances)
    cities = range(num_cities)

    # Generate all possible permutations of cities
    all_possible_routes = itertools.permutations(cities)

    # Initialize the best route and minimum distance
    best_route: tuple[int, ...] = ()
    min_distance: int = float('inf')

    # Evaluate each route
    # O(N!)
    for route in all_possible_routes:
        # Calculate the total distance for this route
        current_distance = calculate_total_distance(route, distances)
        # Update the best route if the current one is shorter
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance


# Example usage: distance matrix where distances[i][j] is the distance from city i to city j
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_distance = traveling_salesman_bruteforce(distances)

print(f"Best route: {best_route}")
print(f"Minimum distance: {min_distance}")
