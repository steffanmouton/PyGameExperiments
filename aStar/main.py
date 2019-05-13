from game import *
import graph
from agent import *


def main():
    """main execution func"""
    game = Game("game")

    # BEGIN A* TEST
    # Generate nXn nodes, set edges, construct as graph
    nodes = graph.gen_nodes(9)
    edges = graph.gen_nbr_edges(nodes)
    chart = graph.Graph(nodes, edges)
    astarGoal = None

    # Given test values
    # --------------------------------------------#
    test_start = [3, 4]
    test_goal = [7, 4]
    test_walls = [[4, 4], [5, 4], [6, 4]]
    # --------------------------------------------#

    # Iterate through nodes, assigning test values
    for n in chart.nodes:
        if n.pos == test_start:
            chart.currentNode = n
        if n.pos == test_goal:
            astarGoal = n
        for wall in test_walls:
            if n.pos == wall:
                n.isWalkable = False

    # Run A* algorithm, returning list that is the path from start to goal
    test = stefmath.aStar(chart, astarGoal, stefmath.manhattan)

    for node in test:
        print(node.pos)
    """
    Expected results are 
    [3,4], [4,3], [5, 3], [6,3], [7,4]
    OR
    [3,4], [4,5], [5, 5], [6,5], [7,4]
    
    RESULTS ARE:
    [3,4], [4,3], [5, 3], [6,3], [7,4]
    CORRECT
    """
    # END OF ASTAR TEST

    # BEGIN STEERING BEHAVIOURS TEST
    testagent = Agent(position=[500, 500])
    mouseagent = MouseAgent()
    testagent.target = mouseagent
    game.gameObjects.append(testagent)
    game.gameObjects.append(mouseagent)

    # add the gameObjects here
    if game._startup():  # if the game starts up correctly
        while game._update():  # update the game if the game updates then
            game._draw()  # draw elements from the game
        game._shutdown()


if __name__ == "__main__":
    main()
