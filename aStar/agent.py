import pygame
import constants
import stefmath
import agentbehaviour as ab
from enum import Enum


class Mode(Enum):
    """Enumerator to keep track of current Behavior Mode"""
    Neutral = 0
    Seek = 1
    Flee = 2
    Wander = 3
    Pursue = 4
    Evade = 5


class MouseAgent:
    """Version of Agent. Used to track mouse and update position every frame."""
    def __init__(self):
        self.pos = [0,0]
        self.lastpos = [0,0]
        self.curVelocity = [0,0]
        self.color = constants.BLUE

    def update(self, dt):
        self.lastpos = self.pos
        try:
            self.pos = pygame.mouse.get_pos()
        except:
            self.pos = [500,500]
        self.curVelocity = stefmath.find_vector_from(self.lastpos, self.pos)

    def draw(self, screen):
        self.pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.circle(screen, self.color, self.pos, 10, 0)


class Agent:
    """Agent. Can move based on forces applied."""
    def __init__(self, position=[0, 0], vel=[0, 0], col=constants.RED):
        self.pos = position
        self.curVelocity = vel
        self.color = col
        self.target = None
        self.force = [0, 0]
        self.mass = 1.0
        self.isPredator = True
        self.wander_circle_distance = 20
        self.pursuit_circle_radius = 1
        self.arrival_circle_radius = 1
        self.behaviour_mode = Mode(0)

    def resetPhysics(self):
        """Reset all movement attributes to base"""
        self.curVelocity = [0, 0]
        self.force = [0, 0]
        self.acceleration = [0, 0]

    def update(self, dt):
        """Checks to see if a button is pressed. Sets behavior to assigned Mode."""

        self.changeBehavior()  # Check for button press
        if self.behaviour_mode == 0:
            return

        if self.behaviour_mode == 1:
            if self.target is not None:
                self.addForce(ab.seek(self))
                # self.addForce(ab.arrive(self))

        if self.behaviour_mode == 2:
            if self.target is not None:
                self.addForce(ab.flee(self))

        if self.behaviour_mode == 3:
            self.addForce(ab.wander(self))

        if self.behaviour_mode == 4:
            self.addForce(ab.pursue(self))
            # self.addForce(ab.arrive(self))

        if self.behaviour_mode == 5:
            self.addForce(ab.evade(self))

        stefmath.move_agent(self, dt)

    def draw(self, screen):
        self.pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.circle(screen, self.color, self.pos, 10, 0)
        pygame.display.set_caption("Current Mode is: {}".format(self.behaviour_mode))

    def addForce(self, v):
        """Each update, adds force to current force on the Agent."""
        if v is None:
            return
        self.force = [self.force[0] + v[0], self.force[1] + v[1]]

    def changeBehavior(self):
        """Each update, check to see if a button is pressed and sets behaviour_mode attribute appropriately"""
        keystate = pygame.key.get_pressed()
        if keystate[pygame.constants.K_0]:
            self.behaviour_mode = 0
        if keystate[pygame.constants.K_1]:
            self.behaviour_mode = 1
        if keystate[pygame.constants.K_2]:
            self.behaviour_mode = 2
        if keystate[pygame.constants.K_3]:
            self.behaviour_mode = 3
        if keystate[pygame.constants.K_4]:
            self.behaviour_mode = 4
        if keystate[pygame.constants.K_5]:
            self.behaviour_mode = 5
        return

