import pygame
import constants


class LineObject:
    def __init__(self, value, edge):
        self.val = value
        self.edges = (edge[0], edge[1])
        self.color = constants.BLUE
        self.scale = 75
        self.clickable = False

    def update(self, dt):
        """ For Inheritance"""

    def draw(self, screen):

        pygame.draw.line(
            screen,
            self.color,
            [self.edges[0].pos[0]*self.scale + self.scale, self.edges[0].pos[1]*self.scale + self.scale],
            [self.edges[1].pos[0]*self.scale + self.scale, self.edges[1].pos[1]*self.scale + self.scale]
        )
