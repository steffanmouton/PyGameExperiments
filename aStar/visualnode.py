import pygame
import constants
import main as Main

class VisualNode:
    def __init__(self, value, position = [0,0]):
        self.val = value
        self.pos = position
        self.color = constants.BLUE
        self.scale = 75

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (self.pos[0]*self.scale + self.scale, self.pos[1]*self.scale + self.scale), 20)

if __name__ == "__main__":
    Main.main()