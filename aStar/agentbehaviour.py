import math
import random
import stefmath
import constants


def seek(agent):
    if agent.target is None:
        return
    vectorToTarget = stefmath.find_vector_from(agent.pos, agent.target.pos)
    v = stefmath.normalize(vectorToTarget)
    if v is None:
        return
    force = [v[0] - agent.curVelocity[0], v[1] - agent.curVelocity[1]]
    return force


def flee(agent):
    v = seek(agent)
    if v is None:
        return
    force = [-v[0], -v[1]]
    return force


def wander(agent):
    circleCenter = stefmath.normalize(agent.curVelocity)
    if circleCenter is None:
        circleCenter = [agent.pos[0] + 5, agent.pos[1] + 5]
    circleCenter = [circleCenter[0]*agent.wander_circle_distance, circleCenter[1]*agent.wander_circle_distance]

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
    futurePosition = [agent.target.pos[0] + agent.target.curVelocity[0] * T, agent.target.pos[1] + agent.target.curVelocity[1] * T]
    vectorToTarget = stefmath.find_vector_from(agent.pos, futurePosition)
    v = stefmath.normalize(vectorToTarget)
    if v is None:
        return
    force = [v[0] - agent.curVelocity[0], v[1] - agent.curVelocity[1]]
    return force


def evade(agent):
    distance = stefmath.find_distance(agent.pos, agent.target.pos)
    updatesAhead = distance / constants.MAX_VELOCITY
    futurePosition = [
        agent.target.pos[0] + agent.target.curVelocity[0] * updatesAhead,
        agent.target.pos[1] + agent.target.curVelocity[1] * updatesAhead
    ]
    vectorToTarget = stefmath.find_vector_from(agent.pos, futurePosition)
    v = stefmath.normalize(vectorToTarget)
    if v is None:
        return
    force = [v[0] - agent.curVelocity[0], v[1] - agent.curVelocity[1]]
    force = [-force[0], -force[1]]
    return force


def arrive(agent):
    desired_velocity = stefmath.find_vector_from(agent.pos, agent.target.pos)
    distance = stefmath.find_vector_mag(desired_velocity)

    if stefmath.find_distance(agent.pos, agent.target.pos) < agent.arrival_circle_radius:
        desired_velocity = stefmath.normalize(desired_velocity) * constants.MAX_VELOCITY * (distance / agent.arrival_circle_radius)
    else:
        desired_velocity = stefmath.normalize(desired_velocity) * constants.MAX_VELOCITY

    force = desired_velocity - agent.curVelocity
    return force
