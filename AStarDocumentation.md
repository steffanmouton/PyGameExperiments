# Astar Pathfinding Documentation

Steffan Mouton

s188045

AI Assessment

## Requirements Documentation

- Description of Problem
  - Name: A* pathfinding algorithm
  - Problem Statement: Create a functional A* search algorithm in python
  - Problem Specification: Must be created in python language using the pygame structure. Can be proven using a test and the console, or with a visual representation.
- Output Information
  - Prints out the node path found by A* algorithm to console or a visual representation. I opted for printing to console.

- User Interface Information
  - Console only.

## Design Documentation

- Information about the objects
  - *Module/Class Information*
    - Name: stefmath
      - Description: Python module for my custom math functions
      - Base Class: NA
      - Module Operations
        - Prototype: find_distance(a,b)
          - Description: Returns the distance between two points by pythagorean theorem.
          - Pre-Conditions: two points exist
          - Post-Conditions: return float value of the distance between the points
        - Prototype: find_vector_from(a, b)
          - Description: Returns the vector originating at point a, reaching point b
          - Pre-Conditions: two vectors exist
          - Post-Conditions: return a vector that connects the two points
        - Prototype: find_vector_mag(v)
          - Description: Returns the magnitude of a given vector
          - Pre-Conditions: vector exists
          - Post-Conditions: returns float of the vector's magnitude
        - Prototype: normalize(v)
          - Description: Returns the normalized form of a given vector
          - Pre-Conditions: vector exists
          - Post-Conditions: returns a normalized vector crafted from the given vector
        - Prototype: manhattan(a, b)
          - Description: Returns the manhattan distance between two given points
          - Pre-Conditions: Two points exist
          - Post-Conditions: returns int of the manhattan distance
        - Prototype: aStar(graph, goal, heuristic=manhattan)
          - Description: A* algorithm. Given graph, goal, and a heuristic to follow, find the best path between two points
          - Pre-Conditions: Graph exists. Graph has nodes. Graph nodes are equally spaced. Heuristic is defined (default is stefmath.manhattan)
          - Post-Conditions: stefmath.aStar_path(start, goal) is called, which returns the path found by this search function
        - Prototype: aStar_path(start, goal)
          - Description: Returns the path from start to goal, as found by aStar function
          - Pre-Conditions: aStar() function is called and it is valid
          - Post-Conditions: return path of nodes from start to goal
    - Name: graph
      - Description: Python module for functionality regarding a graph system of nodes and edges
      - Base Class: NA
      - Module Operations
        - Prototype: find_distance(a,b)
          - Description: Finds the distance between two nodes inside the graph
          - Pre-Conditions: two points exist
          - Post-Conditions: return float value of the distance between the points
        - Prototype: gen_nbr_edges(nodes)
          - Description: Takes in a list of nodes. Generates edges connecting all nodes. Return a list of these edges.
          - Pre-Conditions: list of nodes exists
          - Post-Conditions: generates a returns a list of edges that connects all nodes that neighbour each other
        - Prototype: gen_nodes(size)
          - Description: Generates nodes of a given size, where size is n and number of nodes is n*n
          - Pre-Conditions: NA
          - Post-Conditions: returns a list of nodes that is n*n
    - Name: graph/Node
      - Description: Contains data within the graph
      - Base Class: NA
      - Class Attributes
        - Name: data
          - Description: a container for data
          - Range of Acceptable Values: any
        - Name: pos
          - Description: the position of the node within the graph
          - Range of Acceptable Values: tuple of (int1, int2), where int is > 0
        - Name: parent
          - Description: parent node
          - Type: node
          - Range of Acceptable Values: any node
        - Name: fScore
          - Description: handled by aStar
          - Range of Acceptable Values: float
        - Name: gScore
          - Description: handled by aStar
          - Range of Acceptable Values: float
        - Name: hScore
          - Description: handled by aStar
          - Range of Acceptable Values: float
        - Name: isWalkable
          - Description: Is node traversable by aStar? Default true
          - Range of Acceptable Values: bool
      - Module Operations
        - Prototype: __eq__(self, other)
          - Description: Overloaded equal check for nodes
          - Pre-Conditions: two nodes exist
          - Post-Conditions: return whether data in each node is equivalent
        - Prototype: find_vector_from(a, b)
          - Description: Returns the vector originating at point a, reaching point b
          - Pre-Conditions: two vectors exist
          - Post-Conditions: return a vector that connects the two points
        - Prototype: find_vector_mag(v)
          - Description: Returns the magnitude of a given vector
          - Pre-Conditions: vector exists
          - Post-Conditions: returns float of the vector's magnitude
        - Prototype: normalize(v)
          - Description: Returns the normalized form of a given vector
          - Pre-Conditions: vector exists
          - Post-Conditions: returns a normalized vector crafted from the given vector
        - Prototype: manhattan(a, b)
          - Description: Returns the manhattan distance between two given points
          - Pre-Conditions: Two points exist
          - Post-Conditions: returns int of the manhattan distance
        - Prototype: aStar(graph, goal, heuristic=manhattan)
          - Description: A* algorithm. Given graph, goal, and a heuristic to follow, find the best path between two points
          - Pre-Conditions: Graph exists. Graph has nodes. Graph nodes are equally spaced. Heuristic is defined (default is stefmath.manhattan)
          - Post-Conditions: stefmath.aStar_path(start, goal) is called, which returns the path found by this search function
        - Prototype: aStar_path(start, goal)
          - Description: Returns the path from start to goal, as found by aStar function
          - Pre-Conditions: aStar() function is called and it is valid
          - Post-Conditions: return path of nodes from start to goal
