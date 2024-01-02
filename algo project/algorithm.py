from queue import PriorityQueue

def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    queue = PriorityQueue()
    queue.put((0, start))

    for _ in range(len(graph)):
        (dist, current_node) = queue.get()
        if current_node in shortest_paths:
            for neighbor, neighbor_dist in graph[current_node].items():
                old_cost = shortest_paths.get(neighbor, (None, float('inf')))[1]
                new_cost = dist + neighbor_dist
                if new_cost < old_cost:
                    shortest_paths[neighbor] = (current_node, new_cost)
                    queue.put((new_cost, neighbor))

    return shortest_paths

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2, 'D': 4, 'E': 6},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'B': 4, 'C': 1, 'E': 1},
    'E': {'B': 6, 'D': 1}
}

print(dijkstra(graph, 'A'))  # Output: shortest paths to all nodes from 'A'