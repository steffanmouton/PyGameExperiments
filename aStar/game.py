'''game.py'''

import pygame
from constants import *

class Game(object):
    """pygame object"""

    def __init__(self, name):
        """abc"""
        self._name = name
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))        
        self._clock = pygame.time.Clock()

        self._background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self._background.fill((255, 255, 255))
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        self._events = pygame.event.get()
        self.gameObjects = []
        self._playtime = 0.0
        self._deltatime = 0.0
        self._fps = 30
        self.screen_rect = pygame.Rect(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen_mid = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]

    def _startup(self):
        pygame.display.set_caption(self._name)
        return True

    def _update(self):
        """input and time"""
        seconds = self._clock.tick(self._fps)
        self._deltatime = seconds / 1000.0
        self._playtime += self._deltatime
        self._events = pygame.event.get()

        for event in self._events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_ESCAPE]:
                    pygame.quit()
            if event.type == pygame.constants.QUIT:
                pygame.quit()

        for go in self.gameObjects:
            go.update(self._deltatime)
        return True

    def _draw(self):
        """Causes each game object to call its own Draw function"""
        self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
            self._clock.get_fps(), " " * 5, self._playtime))
        for go in self.gameObjects:
            go.draw(self._screen)
        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))

    def _shutdown(self):
        """shutdown the game properly"""
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        surface = self.font.render(text, True, (0, 0, 0))       
        self._screen.blit(surface, (25, 25))


if __name__ == '__main__':
    import main as Main
    Main.main()
