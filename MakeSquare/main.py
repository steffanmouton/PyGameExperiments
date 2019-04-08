from game import *
from gameObject import *

def main():
    '''main execution func'''
    game = Game("game")

    for i in range (0,40):
        game.gameObjects.append(GameObject([600,i*50]))
    #add the gameObjects here
    if game._startup():#if the game starts up correctly
        while game._update():#update the game if the game updates then
            game._draw()#draw elements from the game
        game._shutdown()

if __name__ == "__main__":
    main()