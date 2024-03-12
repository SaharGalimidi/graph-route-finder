
import heapq
import math
from typing import Dict, Tuple, List, Optional
import matplotlib.pyplot as plt
# Use non-interactive backend to avoid displaying the plot
plt.switch_backend('Agg')


Vertex = Tuple[float, float]
AdjacencyDict = Dict[str, Dict[str, float]]


class Graph:
    def __init__(self) -> None:
        self.adjacency_dict: AdjacencyDict = {}

    def add_vertex(self, vertex: str) -> None:
        """
        Add a vertex to the graph.

        Args:
            vertex (str): The vertex (coordinate) to be added.
        """
        if vertex not in self.adjacency_dict:
            self.adjacency_dict[vertex] = {}

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        """
        Add an undirected edge between two vertices to the graph.

        Args:
            vertex1 (str): The first vertex (coordinate).
            vertex2 (str): The second vertex (coordinate).
        """
        if vertex2 not in self.adjacency_dict[vertex1]:
            vertex1_coord = tuple(map(float, vertex1[1:-1].split(', ')))

            vertex2_coord = tuple(map(float, vertex2[1:-1].split(', ')))
            weight = self.__distance(vertex1_coord, vertex2_coord)
            self.adjacency_dict[vertex1][vertex2] = weight
            # Ensure the graph is undirected
            self.adjacency_dict[vertex2][vertex1] = weight

    def find_shortest_path(self, start: str, end: str) -> Tuple[Optional[List[str]], Optional[float]]:
        """
        Find the shortest path between two vertices using Dijkstra's algorithm.

        Args:
            start (str): The starting vertex (coordinate).
            end (str): The ending vertex (coordinate).

        Returns:
            Tuple[Optional[List[str]], Optional[float]]: A tuple containing
                1) A list of vertices representing the shortest path from start to end, or None if no path exists.
                2) The total distance of the shortest path, or None if no path exists.

        Raises:
            ValueError: If either the start or end vertex does not exist in the graph.
        """
        if start not in self.adjacency_dict or end not in self.adjacency_dict:  # Ensure both vertices exist in the graph
            raise ValueError(
                "One or both start and end vertices do not exist in the graph.")

        distances: Dict[str, float] = {vertex: float(
            'infinity') for vertex in self.adjacency_dict}  # Initialize distances to infinity
        distances[start] = 0    # The distance from start to itself is 0
        # Initialize previous vertices to None
        previous: Dict[str, Optional[str]] = {
            vertex: None for vertex in self.adjacency_dict}
        # Initialize priority queue with start vertex and distance 0
        pq: List[Tuple[float, str]] = [(0, start)]

        while pq:
            # Get the vertex with the smallest distance from the priority queue
            current_dist, current_vertex = heapq.heappop(pq)

            # Skip the rest of the loop if the distance is already larger than the known distance
            if current_dist > distances[current_vertex]:
                continue

            if current_vertex == end:  # We have reached the end vertex
                path: List[str] = []  # Initialize the shortest path
                vertex = end  # Start from the end vertex
                total_distance = current_dist  # The total distance is the current distance
                while vertex is not None:  # Go through the previous vertices until we reach the start vertex
                    path.append(vertex)  # Add the vertex to the path
                    vertex = previous[vertex]  # Move to the previous vertex
                path.reverse()  # Reverse the path to start from the start vertex
                return path, total_distance  # Return the shortest path and the total distance

            # Go through the neighbors of the current vertex
            for neighbor, weight in self.adjacency_dict[current_vertex].items():
                distance = current_dist + weight  # Calculate the distance to the neighbor
                # If the new distance is smaller than the known distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance  # Update the distance
                    # Update the previous vertex
                    previous[neighbor] = current_vertex
                    # Add the neighbor to the priority queue with the new distance
                    heapq.heappush(pq, (distance, neighbor))

        return None, None

    def find_closest_vertex(self, point: Vertex) -> Tuple[Vertex, float]:
        """
        Find the vertex closest to a given point.

        Args:
            point (Tuple[float, float]): The point for which to find the closest vertex.

        Returns:
            Tuple[Tuple[float, float], float]: A tuple containing
                1) The vertex (coordinate) closest to the given point.
                2) The distance between the point and the closest vertex.
        """
        closest_vertex = None
        min_distance = float('infinity')

        for vertex_str in self.adjacency_dict:
            vertex_coord = tuple(map(float, vertex_str[1:-1].split(', ')))
            if vertex_coord == point:
                continue    # Skip the point itself
            distance = self.__distance(point, vertex_coord)

            if distance < min_distance:
                min_distance = distance
                closest_vertex = vertex_coord

        return closest_vertex, min_distance

    def show_graph(self, shortest_path: List[str] = None, closest_vertex_info: Tuple[Vertex, float] = None, source_vertex: Vertex = None) -> None:
        """
        Visualize the graph and optionally highlight the shortest path, the closest vertex, the source vertex, and the edge from the source to the closest vertex.

        Args:
            shortest_path (List[str], optional): A list of vertices representing the shortest path.
                Defaults to None.
            closest_vertex_info (Tuple[Vertex, float], optional): A tuple containing
                1) The closest vertex (coordinate) to the given point.
                2) The distance between the point and the closest vertex.
                Defaults to None.
            source_vertex (Vertex, optional): The source vertex (coordinate) from which to highlight the edge to the closest vertex.
                Defaults to None.
        """
        fig, ax = plt.subplots(figsize=(12, 10))

        # Extract coordinates for plotting
        x_coords = []
        y_coords = []
        labels = {}  # Dictionary to store vertex labels

        for vertex_str in self.adjacency_dict:
            vertex_coord = tuple(map(float, vertex_str[1:-1].split(', ')))
            x_coords.append(vertex_coord[0])
            y_coords.append(vertex_coord[1])
            # Set vertex label as its string representation
            labels[vertex_str] = vertex_str

        # Plot vertices with labels
        ax.scatter(x_coords, y_coords, color='blue',
                   marker='o', label='Vertices')
        for vertex_str, (x, y) in zip(self.adjacency_dict.keys(), zip(x_coords, y_coords)):
            ax.text(x, y, labels[vertex_str], fontsize=8,
                    ha='center', va='center')  # Add vertex label

        # Plot edges with weight labels
        for vertex1, neighbors in self.adjacency_dict.items():
            vertex1_coord = tuple(map(float, vertex1[1:-1].split(', ')))
            for vertex2, weight in neighbors.items():
                vertex2_coord = tuple(map(float, vertex2[1:-1].split(', ')))
                ax.plot([vertex1_coord[0], vertex2_coord[0]], [
                        vertex1_coord[1], vertex2_coord[1]], color='gray')
                ax.text((vertex1_coord[0] + vertex2_coord[0]) / 2,
                        (vertex1_coord[1] + vertex2_coord[1]) / 2, f'{weight:.2f}', fontsize=8)

        # Highlight closest vertex and its edge
        if closest_vertex_info and source_vertex:
            closest_vertex, _ = closest_vertex_info
            closest_vertex_coord = closest_vertex

            ax.scatter(closest_vertex_coord[0], closest_vertex_coord[1], color='red',
                       s=100, marker='o', edgecolors='black', label='Closest Vertex')
            ax.scatter(source_vertex[0], source_vertex[1], color='green',
                       s=100, marker='o', edgecolors='black', label='Source Vertex')

            # Highlight edge from source to closest vertex
            for neighbor_str, weight in self.adjacency_dict[str(source_vertex)].items():
                neighbor_coord = tuple(
                    map(float, neighbor_str[1:-1].split(', ')))
                if neighbor_coord == closest_vertex_coord:
                    ax.plot([source_vertex[0], neighbor_coord[0]], [
                            source_vertex[1], neighbor_coord[1]], color='red', linewidth=2)
                    break

        # Highlight shortest path
        if shortest_path:
            path_x = []
            path_y = []
            for vertex_str in shortest_path:
                vertex_coord = tuple(map(float, vertex_str[1:-1].split(', ')))
                path_x.append(vertex_coord[0])
                path_y.append(vertex_coord[1])
            ax.plot(path_x, path_y, color='red', linewidth=2)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Graph Visualization')
        ax.grid(True)
        ax.legend()

        image_path = 'app/static/images/graph.png'
        plt.savefig(image_path)  # Save the figure

    @staticmethod
    def __distance(coord1: Vertex, coord2: Vertex) -> float:
        """
        Calculate the Euclidean distance between two coordinates.

        Args:
            coord1 (Tuple[float, float]): The first coordinate.
            coord2 (Tuple[float, float]): The second coordinate.

        Returns:
            float: The Euclidean distance between the two coordinates.
        """
        x1, y1 = coord1
        x2, y2 = coord2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    @staticmethod
    def create_graph_from_json(json_data: dict) -> 'Graph':
        graph = Graph()

        # A set to keep track of all vertices (to avoid duplicates).
        all_vertices = set()

        # First, add all vertices to the set to ensure uniqueness.
        for vertex_str, neighbors_list in json_data.items():
            # Add the original vertex
            all_vertices.add(vertex_str)
            # Add all neighbor vertices
            for neighbor in neighbors_list:
                neighbor_str = f"({neighbor[0]}, {neighbor[1]})"
                all_vertices.add(neighbor_str)

        # Now, add all vertices to the graph.
        for vertex_str in all_vertices:
            graph.add_vertex(vertex_str)

        # Finally, add all edges to the graph.
        for vertex_str, neighbors_list in json_data.items():
            for neighbor in neighbors_list:
                neighbor_str = f"({neighbor[0]}, {neighbor[1]})"
                graph.add_edge(vertex_str, neighbor_str)

        return graph
