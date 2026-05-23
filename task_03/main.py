import heapq


def create_graph():
    return {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }


def dijkstra(graph, start):
    distances = {}
    previous_vertices = {}

    for vertex in graph:
        distances[vertex] = float("inf")
        previous_vertices[vertex] = None

    distances[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    return distances, previous_vertices


def restore_path(previous_vertices, start, end):
    path = []
    current_vertex = end

    while current_vertex is not None:
        path.append(current_vertex)

        if current_vertex == start:
            break

        current_vertex = previous_vertices[current_vertex]

    path.reverse()

    if path and path[0] == start:
        return path

    return []


def print_result(distances, previous_vertices, start):
    print(f"Shortest paths from vertex {start}:")

    for vertex in distances:
        path = restore_path(previous_vertices, start, vertex)
        path_text = " -> ".join(path)
        print(f"{start} to {vertex}: distance = {distances[vertex]}, path = {path_text}")


def run_tests():
    graph = create_graph()
    distances, previous_vertices = dijkstra(graph, "A")

    assert distances == {
        "A": 0,
        "B": 3,
        "C": 2,
        "D": 8,
        "E": 10,
        "F": 13,
    }

    assert restore_path(previous_vertices, "A", "F") == [
        "A",
        "C",
        "B",
        "D",
        "E",
        "F",
    ]


def main():
    run_tests()

    graph = create_graph()
    start_vertex = "A"

    distances, previous_vertices = dijkstra(graph, start_vertex)
    print_result(distances, previous_vertices, start_vertex)


if __name__ == "__main__":
    main()
