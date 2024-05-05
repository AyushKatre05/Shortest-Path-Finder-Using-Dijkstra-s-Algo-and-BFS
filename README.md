# Pathfinding Visualizer

This is a simple pathfinding visualizer implemented in Python using Pygame for the desktop version and Streamlit for the web version. The visualizer allows users to create obstacles, set start and target points, and visualize the pathfinding algorithms finding the shortest path between them.

## Algorithms Used

### Dijkstra's Algorithm

Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a weighted graph. In this visualizer, Dijkstra's algorithm is used to find the shortest path between the start and target points, taking into account the weights of the edges.

### Breadth-First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm that explores all the neighbor nodes at the present depth before moving on to the nodes at the next depth level. In this visualizer, BFS is used to find the shortest path between the start and target points in an unweighted graph.

## Features

- **Set Start and Target Points**: Users can click on cells to set the start and target points for the pathfinding algorithm.
- **Draw Obstacles**: Users can click and drag to draw obstacles on the grid, which the pathfinding algorithm will avoid.
- **Visualize Path**: Users can visualize the pathfinding algorithm in action by clicking a button.

## Desktop Version (Dijkstra)

The desktop version of the visualizer uses Pygame for graphics and user interaction. To run the desktop version:

1. Install Pygame: Make sure you have Pygame installed (`pip install pygame`).
2. Run the Script: Execute the Python script `pathfinding_visualizer_dijkstra.py`.

## Web Version (BFS)

The web version of the visualizer uses Streamlit for web deployment. To run the web version:

1. Install Streamlit: Make sure you have Streamlit installed (`pip install streamlit`).
2. Run the Script: Execute the Python script `pathfinding_visualizer_bfs.py`. This will launch a Streamlit server.
3. Open in Browser: Open the URL provided by Streamlit in your web browser to interact with the visualizer.

## Contributors

- [Ayush Katre] - [ayushkatre1801@gmail.com]

## Acknowledgments

- This code is inspired by various pathfinding visualization projects available online.
- Special thanks to the developers of Pygame and Streamlit for providing tools to create interactive visualizations in Python.



