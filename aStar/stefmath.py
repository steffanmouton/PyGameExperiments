import math

def find_distance(a, b):
    """Returns the distance between two points by pythagorean theorem."""
    alpha = (float(a[0]), float(a[1]))
    beta = (float(b[0]), float(b[1]))
    return float(abs(math.sqrt(pow(beta[0]-alpha[0], 2) + pow(beta[1]-alpha[1], 2))))


def find_vector_from(a, b):
    """Returns the vector originating at point a, reaching point b"""
    return b[0] - a[0], b[1] - a[1]


def find_vector_mag(v):
    """Returns the magnitude of a given vector"""
    return float(math.sqrt(pow(v[0], 2) + pow(v[1], 2)))


def normalize(v):
    """Returns the normalized form of a given vector"""
    mag = find_vector_mag(v)
    if mag == 0:
        return [0, 0]
    return [v[0] / mag, v[1] / mag]


def rotate_around_point(point, radians, origin=(0, 0)):
    """Given a point and an origin to rotate around, rotate in radians"""
    x, y = point
    originX, originY = origin
    newX = originX + math.cos(radians) * (x-originX) + math.sin(radians) * (y-originY)
    newY = originY + math.sin(radians) * (x-originX) + math.cos(radians) * (y-originY)

    return [newX, newY]


def move_agent(ag, dt):
    """Move the agent based on its own forces being applied, mass, current velocity, and position"""
    acceleration = [ag.force[0]/ag.mass, ag.force[1]/ag.mass]
    ag.curVelocity = [ag.curVelocity[0] + (acceleration[0] * dt), ag.curVelocity[1] + (acceleration[1] * dt)]
    ag.pos = [ag.pos[0] + (ag.curVelocity[0] * dt), ag.pos[1] + (ag.curVelocity[1] * dt)]


def manhattan(a, b):
    """ Returns the manhattan distance between two given points"""
    distanceX = abs(10*(b[0] - a[0]))
    distanceY = abs(10*(b[1] - a[1]))
    return distanceX + distanceY


def aStar_path(start, goal):
    """Returns the path from start to goal, as found by aStar function"""
    fullPath = []
    current = goal
    while current != start:
        fullPath.append(current)
        current = current.parent

    fullPath.append(current)
    fullPath.reverse()
    return fullPath


def aStar(graph, goal, heuristic=manhattan):
    """A* algorithm. Given graph, goal, and a heuristic to follow, find the best path between two points"""
    closedNodes = []
    start = graph.currentNode
    discoveredNodes = [graph.currentNode]

    while len(discoveredNodes) > 0:
        discoveredNodes.sort(key=lambda Node: Node.fScore)
        current = discoveredNodes[0]
        if current == goal:
            path = aStar_path(start, goal)
            return path
        
        discoveredNodes.remove(current)
        closedNodes.append(current)

        for n in graph.adjacent_nodes(current):
            if n in closedNodes:
                continue
            if not n.isWalkable:
                closedNodes.append(n)
                continue
            tent_gScore = current.gScore + find_distance(current.pos, n.pos)

            if n not in discoveredNodes:
                discoveredNodes.append(n)
            elif tent_gScore >= n.gScore:
                continue

            n.parent = current
            n.gScore = tent_gScore
            n.fScore = n.gScore + heuristic(n.pos, goal.pos)
