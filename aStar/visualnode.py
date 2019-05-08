import pygame
import constants
import main as Main
import stefmath
from enum import Enum


class State(Enum):
    Normal = 1
    Start = 2
    Path = 3
    Goal = 4


class VisualNode:
    def __init__(self, value, position=(0, 0)):
        self.val = value
        self.pos = position
        self.color = constants.BLUE
        self.scale = 75
        self.radius = 20
        self.curState = State(1)
        self.clickable = True

    def update(self, dt):
        if self.curState == 1:
            self.color = constants.BLUE
        if self.curState == 2:
            self.color = constants.GREEN
        if self.curState == 3:
            self.color = constants.YELLOW
        if self.curState == 4:
            self.color = constants.RED

    def draw(self, screen):

        pygame.draw.circle(
            screen, 
            self.color, 
            (self.pos[0]*self.scale + self.scale, self.pos[1]*self.scale + self.scale), 
            self.radius
            )
    
    def is_point_inside(self, point):
        if stefmath.find_distance((self.pos[0]*self.scale + self.scale, self.pos[1]*self.scale + self.scale), point) < self.radius:
            return True
        return False

    def onClick(self):
        m1, m2, m3 = pygame.mouse.get_pressed()
        if m1:
            self.curState = 4
        if m3:
            self.curState = 2
