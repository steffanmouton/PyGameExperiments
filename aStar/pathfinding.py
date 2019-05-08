import math


def find_distance(a, b):
    """Returns the distance between two points by pythagorean theorem."""
    alpha = (float(a[0]), float(a[1]))
    beta = (float(b[0]), float(b[1]))
    return float(abs(math.sqrt(pow(beta[0]-alpha[0], 2) + pow(beta[1]-alpha[1], 2))))


def manhattan(a, b):
    """ Returns the manhattan distance between two given points"""
    distanceX = abs(10*(b[0] - a[0]))
    distanceY = abs(10*(b[1] - a[1]))
    return distanceX + distanceY


def aStar_path(start, goal):
    fullPath = []
    current = goal
    while current != start:
        fullPath.append(current)
        current = current.parent

    return fullPath.reverse()


def aStar(graph, goal, heuristic=manhattan):
    closedNodes = []
    start = graph.currentNode
    discoveredNodes = [graph.currentNode]

    while len(discoveredNodes) > 0:
        discoveredNodes.sort(key=lambda Node: Node.fScore)
        current = discoveredNodes[0]
        if current == goal:
            return aStar_path(start, goal)

        discoveredNodes.remove(current)
        closedNodes.append(current)

        for n in graph.adjacent_nodes(current):
            if n in closedNodes:
                continue

            tent_gScore = current.gScore + find_distance(current.pos, n.pos)

            if n not in discoveredNodes:
                discoveredNodes.append(n)
            elif tent_gScore >= n.gScore:
                continue

            n.parent = current
            n.gScore = tent_gScore
            n.fScore = n.gScore + heuristic(n.pos, goal.pos)
