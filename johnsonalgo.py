import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    for _ in range(len(graph) - 1):
        for u, v, weight in graph.edges(data=True):
            if dist[u] + weight['weight'] < dist[v]:
                dist[v] = dist[u] + weight['weight']

    return dist

def reweight(graph, distances):
    for u, v, weight in graph.edges(data=True):
        graph[u][v]['weight'] += distances[u] - distances[v]

def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph.nodes()}
    dist[source] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = min((node for node in graph.nodes() if node not in visited), key=lambda x: dist[x])
        visited.add(min_node)

        for neighbor in graph.neighbors(min_node):
            total_weight = dist[min_node] + graph[min_node][neighbor]['weight']
            if total_weight < dist[neighbor]:
                dist[neighbor] = total_weight

    return dist

def johnsons_algorithm(graph):
    new_vertex = 'new'
    graph.add_node(new_vertex)
    for node in graph.nodes():
        if node != new_vertex:
            graph.add_edge(new_vertex, node, weight=0)

    distances = bellman_ford(graph, new_vertex)
    reweight(graph, distances)
    graph.remove_node(new_vertex)

    shortest_paths = {}
    for node in graph.nodes():
        shortest_paths[node] = dijkstra(graph, node)

    return shortest_paths

def visualize_graph(graph, shortest_paths):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold')
    edge_labels = {(u, v): data['weight'] for u, v, data in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
    plt.title('Graph Visualization with Shortest Path Distances', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def input_graph():
    graph = nx.DiGraph()
    n = int(input("Enter the number of vertices: "))

    for i in range(n):
        while True:
            neighbor = int(input(f"Enter the neighbor vertex for vertex {i} (-1 to stop): "))
            if neighbor == -1:
                break

            weight = int(input(f"Enter the weight for edge ({i}, {neighbor}): "))
            graph.add_edge(i, neighbor, weight=weight)

    return graph

if __name__ == "__main__":
    graph = input_graph()
    shortest_paths = johnsons_algorithm(graph)

    for node, paths in shortest_paths.items():
        print(f"Shortest paths from node {node}: {paths}")

    visualize_graph(graph, shortest_paths)
    print("\n\n")
    print("-----------------------")
    print("Shortest paths have been calculated using Johnson's algorithm.")
