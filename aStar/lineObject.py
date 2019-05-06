import pygame
import constants
import main as Main

class LineObject:
    def __init__(self, value, edge):
        self.val = value
        self.edges = (edge[0], edge[1])
        self.color = constants.BLUE
        self.scale = 75
        self.clickable = False

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):

        pygame.draw.line(
        screen, 
        self.color, 
        [self.edges[0].pos[0]*self.scale + self.scale, self.edges[0].pos[1]*self.scale + self.scale], 
        [self.edges[1].pos[0]*self.scale + self.scale, self.edges[1].pos[1]*self.scale + self.scale]
        )

if __name__ == "__main__":
    Main.main()