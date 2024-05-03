"""
A graph data structure consists of a finite (and possibly mutable) set of vertices (also called nodes or points), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as edges (also called links or lines), and for a directed graph are also known as edges but also sometimes arrows or arcs. The vertices may be part of the graph structure, or may be external entities represented by integer indices or references. [Wikepedia => https://en.wikipedia.org/wiki/Graph_(abstract_data_type)]

The basic operations provided by a graph data structure G usually include:[1]

1. adjacent(G, x, y): tests whether there is an edge from the vertex x to the vertex y;
2. neighbors(G, x): lists all vertices y such that there is an edge from the vertex x to the vertex y;
3. add_vertex(G, x): adds the vertex x, if it is not there;
remove_vertex(G, x): removes the vertex x, if it is there;
4. add_edge(G, x, y, z): adds the edge z from the vertex x to the vertex y, if it is not there;
5. remove_edge(G, x, y): removes the edge from the vertex x to the vertex y, if it is there;
6. get_vertex_value(G, x): returns the value associated with the vertex x;
7. set_vertex_value(G, x, v): sets the value associated with the vertex x to v.

Structures that associate values to the edges usually also provide:[1]

1. get_edge_value(G, x, y): returns the value associated with the edge (x, y);
2. set_edge_value(G, x, y, v): sets the value associated with the edge (x, y) to v.

COMMON DATA STRUCTURE FOR GRAPH REPRESENTATION

- Adjacency list 
- Adjancy matrix
- Incidence matrix

GRAPH TRAVERSAL

- BFS [Breadth First Search]
- DFS [Depth First Search]
"""

from typing import List, Tuple, Union
import numpy as np


class AdjacencyListGraphNode:
    def __init__(
        self,
        vertices: List[str | int],
        edges: Union[
            List[Union[List[str | int], Tuple[str | int]]],
            Tuple[Union[List[str | int], Tuple[str | int]]],
        ],
    ) -> None:
        self.vertices = vertices
        self.edges = edges

    @property
    def data(self) -> dict:
        return {vertex: edge for vertex, edge in zip(self.vertices, self.edges)}

    def __repr__(self) -> str:
        return "\n".join([f"{key}: {value}" for key, value in self.data.items()])

    def __str__(self) -> str:
        return self.__repr__()


graph = AdjacencyListGraphNode(
    ["a", "b", "c", "d", "e"], [["b", "c"], ["a", "d"], ["a", "d"], ["e"], ["d"]]
)

# print(graph)


class AdjacencyMatrixGraphNode:
    def __init__(
        self,
        vertices: List[str | int],
        edges: Union[
            List[Union[List[str | int], Tuple[str | int]]],
            Tuple[Union[List[str | int], Tuple[str | int]]],
        ],
    ) -> None:
        self.vertices = vertices
        self.edges = edges

    @property
    def data(self) -> dict:
        matrix = np.zeros((len(self.vertices), len(self.vertices)), dtype=np.int32)

        for rIndex, row in enumerate(matrix):
            for cIndex, col in enumerate(row):
                if self.vertices[cIndex] in self.edges[rIndex]:
                    matrix[rIndex, cIndex] = 1

        return matrix

    def __repr__(self) -> str:
        matrix = np.zeros((len(self.vertices), len(self.vertices)), dtype=np.int32)
        outputMatrix = "[\n"

        for rIndex, row in enumerate(matrix):
            for cIndex in range(len(row)):
                if self.vertices[cIndex] in self.edges[rIndex]:
                    matrix[rIndex, cIndex] = 1

            outputMatrix += f"    {matrix[rIndex]}\n"

        outputMatrix += "]"

        return outputMatrix


graph = AdjacencyMatrixGraphNode(
    ["a", "b", "c", "d", "e"], [["b", "c"], ["a", "d"], ["a", "d"], ["e"], ["d"]]
)

print(graph)
