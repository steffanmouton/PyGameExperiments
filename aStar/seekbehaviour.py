import stefmath

def seek(seeker):
    if seeker.target is None:
        return
    vectorToTarget = stefmath.find_vector_from(seeker.pos, seeker.target.pos)
    v = stefmath.normalize(vectorToTarget)
    force = [v[0] - seeker.curVelocity[0], v[1] - seeker.curVelocity[1]]
    return force