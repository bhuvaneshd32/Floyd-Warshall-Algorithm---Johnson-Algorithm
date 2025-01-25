import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float("inf")] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        for neighbor, weight in graph[i]:
            dist[i][neighbor] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Negative cycle detected in the graph.")

    return dist

def visualize_graph(graph):
    G = nx.DiGraph()

    node_index = {}
    index = 0
    for node, neighbors in graph.items():
        if node not in node_index:
            node_index[node] = index
            index += 1
        for neighbor, weight in neighbors:
            if neighbor not in node_index:
                node_index[neighbor] = index
                index += 1
            G.add_edge(node_index[node], node_index[neighbor], weight=weight)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = {(node, neighbor): G[node][neighbor]['weight'] for node, neighbor in G.edges()}

    plt.figure(figsize=(12, 8))
    node_sizes = [1500 for _ in range(len(G))]
    node_colors = ['skyblue' for _ in range(len(G))]
    labels = {index: node for node, index in node_index.items()}

    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='black')
    nx.draw_networkx_labels(G, pos, labels=labels, font_color='black', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    st.pyplot(plt)

st.title('Graph Visualization and Floyd-Warshall Algorithm')
st.write("Enter the graph details to visualize and compute shortest paths.")

n = st.number_input("Enter the number of vertices", min_value=1, step=1)
graph = {}
for i in range(n):
    edges = []
    st.write(f"Vertex {i}:")
    edge_index = 0  # Initialize edge index for each vertex
    while True:
        neighbor_key = f"neighbor_{i}_{edge_index}"
        weight_key = f"weight_{i}_{edge_index}"
        
        neighbor = st.number_input(f"Enter the neighbor vertex for vertex {i} (-1 to stop)", min_value=-1, step=1, key=neighbor_key)
        if neighbor == -1:
            break
        
        weight = st.number_input(f"Enter the weight for edge ({i}, {neighbor})", step=1, key=weight_key)
        edges.append((neighbor, weight))
        
        edge_index += 1  # Increment edge index for each new edge
    graph[i] = edges

if st.button('Calculate Shortest Paths'):
    try:
        dist = floyd_warshall(graph)
        st.write("Shortest path distances:")
        for i in range(n):
            for j in range(n):
                st.write(f"Shortest path from {i} to {j} is {dist[i][j]}")
    except ValueError as e:
        st.error(e)

if st.button('Visualize Graph'):
    visualize_graph(graph)
