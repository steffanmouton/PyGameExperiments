from game import *
import agent
import constants


def main():
    '''main execution func'''
    game = Game("game")

    game.gameObjects.append(agent.Agent([100, 500], vel = (1.0,-1.0)))
    
    game.gameObjects.append(agent.Agent([600, 100], col = constants.BLUE))

    game.gameObjects[0].setTarget(game.gameObjects[1])

    #add the gameObjects here
    if game._startup():#if the game starts up correctly
        while game._update():#update the game if the game updates then
            game._draw()#draw elements from the game
        game._shutdown()

if __name__ == "__main__":
    main()