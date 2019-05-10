import math
import random
import stefmath
import constants


def seek(agent):
    if agent.target is None:
        return
    vectorToTarget = stefmath.find_vector_from(agent.pos, agent.target.pos)
    v = stefmath.normalize(vectorToTarget)
    force = [v[0] - agent.curVelocity[0], v[1] - agent.curVelocity[1]]
    return force


def flee(agent):
    v = seek(agent)
    force = [-v[0], -v[1]]
    return force


def wander(agent, circleDistance):
    circleCenter = stefmath.normalize(agent.curVelocity)
    circleCenter = [circleCenter[0]*circleDistance, circleCenter[1]*circleDistance]
    wanderAngle = 0
    displacement = [0, -1]

    displacement = [displacement[0] * agent.pursuit_circle_radius, displacement[1] * agent.pursuit_circle_radius]
    stefmath.rotate_around_point(displacement, wanderAngle)

    wanderAngle += random.random() * constants.ANGLE_CHANGE - constants.ANGLE_CHANGE * .5

    force = [circleCenter[0] + displacement[0], circleCenter[1] + displacement[1]]
    return force


def pursue(agent):
    distance = stefmath.find_distance(agent.pos, agent.target.pos)
    T = distance / constants.MAX_VELOCITY
    futurePosition = agent.target.pos + agent.target.curVelocity * T
    vectorToTarget = stefmath.find_vector_from(agent.pos, futurePosition)
    v = stefmath.normalize(vectorToTarget)
    force = [v[0] - agent.curVelocity[0], v[1] - agent.curVelocity[1]]
    return force


def evade(agent):
    distance = stefmath.find_distance(agent.pos, agent.target.pos)
    updatesAhead = distance / constants.MAX_VELOCITY
    futurePosition = futurePosition = agent.target.pos + agent.target.curVelocity * updatesAhead
    return flee(futurePosition)


# TODO: Create Arrive Bhv
