import math
from game import *
from gameObject import *
from graphObject import *
from lineObject import *

def find_distance(a, b):
        sum_under_root = 0.0
        for i in zip(a, b):
            sum_under_root += pow(b[i]-a[i], 2)
        return (math.sqrt(sum_under_root))
          

def gen_edges(graph):
    '''Takes in a graph. Generates edges connecting all nodes. Return a list of these edges.'''
    edgeslist = []
    for node_alpha in graph.nodes:
        for node_beta in graph.nodes:
            if node_alpha == node_beta:
                continue
            edgeslist.append(Edge(node_alpha, node_beta))
    return edgeslist

def gen_nodes(size):
    node_list = []
    for i in range(0,size):
        for j in range(0,size):
            node_list.append((i,j))

class Node:
    '''Contains data.'''
    def __init__(self, value, position):
        self._data = value
        self._pos = position

class Edge:
    '''Connection between two nodes. Takes in parameters of two points to be connected.'''
    def __init__(self, alpha, beta, relation = None):
        self._points = (alpha, beta)

        if relation:
            self._relation = relation(alpha,beta)
    
    @property
    def points(self):
        return self._points

class Graph:
    '''Take in arguments: nodes and edges''' 
    def __init__(self, nodes_param, edges_param = None):
        self._nodes = nodes_param
        self._edges = edges_param
        if not self.edges:
            self.set_edges(gen_edges(self))

    def adjacent_edges(self, n):
        '''Takes in a node, returns a list of edges connected to itself'''
        adj_edge_list = []

        for e in self.edges:
            if e.points[0] == n or e.points[1] == n:
                adj_edge_list.append(e)
        
        return adj_edge_list

    def render(self, game):
        for n in self.nodes:
            game.gameObjects.append(GraphObject(n._data, n._pos))
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