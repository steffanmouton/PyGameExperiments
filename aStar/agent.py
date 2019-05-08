import pygame
import constants
import seekbehaviour
import stefmath


class Agent:
    def __init__(self, position=[0, 0], vel=[0, 0], col=constants.RED):
        self.pos = position
        self.curVelocity = vel
        self.color = col
        self.target = None
        self.force = [0, 0]
        self.acceleration = [0, 0]
        self.mass = 1.0

    def update(self, dt):
        self.addForce(seekbehaviour.seek(self))
        stefmath.move_agent(self, dt)

    def draw(self, screen):
        self.pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.circle(screen, self.color, self.pos, 10, 0)

    def setTarget(self, targ):
        self.target = targ

    def addForce(self, v):
        if v is None:
            return
        self.force = [self.force[0] + v[0], self.force[1] + v[1]]
