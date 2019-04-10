import math
import pygame
import constants
import main as Main

class GameObject:
    def __init__(self, position = [0,0]):
        self.pos = position
        self.color = None

    def update(self, dt):
        ''' For Inheritence'''

    def draw(self, screen):
        '''
        surface = pygame.Surface((30, 30))
        surface.fill(constants.BLACK)
        screen.blit(surface, self.pos)
        '''

if __name__ == "__main__":
    Main.main()