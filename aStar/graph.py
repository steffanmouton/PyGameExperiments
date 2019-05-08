import math
from game import *
from visualnode import *
from lineObject import *


def find_distance(a, b):
        xLeg = b[0] - a[0]
        yLeg = b[1] - a[1]

        return math.sqrt(float(xLeg**2) + float(yLeg**2))


def gen_nbr_edges(nodes):
    """Takes in a graph. Generates edges connecting all nodes. Return a list of these edges."""
    edgeslist = []
    for node_alpha in nodes:
        for node_beta in nodes:
            if node_alpha == node_beta:
                continue
            if find_distance(node_alpha.pos, node_beta.pos) < 1.42:
                if Edge(node_alpha, node_beta) in edgeslist or Edge(node_beta, node_alpha) in edgeslist:
                    continue
                edgeslist.append(Edge(node_alpha, node_beta))
    return edgeslist
    # Need to overload comparison operator for edges


def gen_nodes(size):
    node_list = []
    count = 1
    for i in range(0, size):
        for j in range(0, size):
            node_list.append(Node([i, j], count))
            count += 1
    return node_list


class Node:
    """Contains data."""
    def __init__(self, position=[0, 0], value=0):
        self.data = value
        self.pos = position
        self.parent = None
        self.fScore = 0
        self.gScore = 0
        self.hScore = 0
        self.isWalkable = 1

    def __eq__(self, other):
        return self.data == other.data


class Edge:
    """Connection between two nodes. Takes in parameters of two points to be connected."""
    def __init__(self, alpha, beta, relation=None):
        self._points = (alpha, beta)

        if relation:
            self._relation = relation(alpha,beta)
    
    def __eq__(self, other):
        return self.points == other.points
    
    @property
    def points(self):
        return self._points


class Graph:
    """Take in arguments: nodes and edges"""
    def __init__(self, nodes_param, edges_param=None):
        self._nodes = nodes_param
        self._edges = edges_param
        if self._nodes is None:
            return
        
        self.currentNode = self._nodes[0]

    def adjacent_edges(self, n):
        """Takes in a node, returns a list of edges connected to itself"""
        adj_edge_list = []

        for e in self.edges:
            if e.points[0] == n or e.points[1] == n:
                adj_edge_list.append(e)
        
        return adj_edge_list

    def adjacent_nodes(self, this_node):
        """Takes in a node, returns a list of neighbouring nodes"""
        connected_edges = self.adjacent_edges(this_node)
        nbrs = []

        for e in connected_edges:
            for n in e.points:
                if n == this_node:
                    continue
                if n in nbrs:
                    continue
                nbrs.append(n)

        return nbrs

    def render(self, game):
        for n in self.nodes:
            game.gameObjects.append(VisualNode(n.data, n.pos))
        for e in self.edges:
            game.gameObjects.append(LineObject(1, e._points))

    @property
    def nodes(self):
        return self._nodes
    
    def set_nodes(self, n):
        self._nodes = n
    
    @property
    def edges(self):
        return self._edges
    
    def set_edges(self, e):
        self._edges = e
