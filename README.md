# Floyd Warshall Algorithm & Bellman Ford Algorithm
 
This project implements shortest path algorithms for weighted directed graphs. It includes the Floyd-Warshall and Johnson's algorithms to calculate shortest paths and visualize the results using NetworkX and Matplotlib.

## Overview
**Floyd-Warshall Algorithm:** Computes shortest paths between all pairs of vertices. Handles negative weight cycles. 

**Johnson's Algorithm:** Computes shortest paths between all pairs of vertices efficiently using reweighting. Utilizes Bellman-Ford for reweighting and Dijkstra's algorithm for shortest path calculation. Efficient for sparse graphs.

## Project Structure
#### Floyd-Warshall Implementation

**floyd_warshall(graph):** Computes shortest paths using the Floyd-Warshall algorithm.  
**visualize_graph(graph):** Visualizes the graph with Matplotlib.  

#### Johnson's Algorithm Implementation

**bellman_ford(graph, source):** Runs Bellman-Ford algorithm for reweighting.  
**reweight(graph, distances):** Adjusts edge weights based on Bellman-Ford results.  
**dijkstra(graph, source):** Runs Dijkstra’s algorithm for shortest path calculation.  
**johnsons_algorithm(graph):** Implements Johnson's algorithm using the above components.  
**visualize_graph(graph, shortest_paths):** Visualizes the graph with shortest path distances.  

#### Graph Input
**input_graph():** Prompts user for graph input and edge weights.  

