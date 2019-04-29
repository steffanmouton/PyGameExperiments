import math

def find_distance(a, b):
    '''Returns the distance between two points by pythagorean theorum.'''
    if a is tuple and b is tuple:
        alpha = (float(a[0]), float(a[1]))
        beta = (float(b[0]), float(b[1]))
        return float(abs(math.sqrt(pow(beta[0]-alpha[0], 2) + pow(beta[1]-alpha[1], 2))))

def find_vector_from(a, b):
    return (b[0] - a[0], b[1] - a[1])

def find_vector_mag(v):
    return float(math.sqrt(pow(v[0], 2) + pow(v[1], 2)))

def normalize(v):
    mag = find_vector_mag(v)
    return [v[0] / mag, v[1] / mag]

def move_agent(ag, dt):
    ag.acceleration = [ag.force[0]/ag.mass, ag.force[1]/ag.mass]
    ag.curVelocity = [ag.curVelocity[0] + (ag.acceleration[0] * dt), ag.curVelocity[1] + (ag.acceleration[1] * dt)]
    ag.pos = [ag.pos[1] + (ag.curVelocity[0] * dt), ag.pos[1] + (ag.curVelocity[1] * dt)]

def manhattan(a, b):
    return a + b

def a_star(graph, goal, heuristic = manhattan):
    closedNodes = []
    discoveredNodes = [graph.currentNode]

    while discoveredNodes.length() > 0:
        discoveredNodes.sort(fScore) # TODO FIX THIS
        current = discoveredNodes[0]
        if current == goal:
            return
                
        discoveredNodes.remove(current)
        closedNodes.append(current)

        for n in graph.adjacent_nodes(current):
            if n in closedNodes():
                continue

            tent_gScore = current.gScore + find_distance(current, n)

            if n not in discoveredNodes():
                discoveredNodes.append()
            elif tent_gScore >= n.gScore:
                continue
            
            n.parent = current
            n.gScore = tent_gScore
            n.fScore = n.gScore + heuristic(n, goal)