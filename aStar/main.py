from game import *
import graph
import stefmath


def main():
    """main execution func"""
    game = Game("game")

    # add the gameObjects here
    if game._startup():  # if the game starts up correctly
        while game._update():  # update the game if the game updates then
            game._draw()  # draw elements from the game
        game._shutdown()


if __name__ == "__main__":
    main()


""" Test for Astar
    nodes = graph.gen_nodes(9)
    edges = graph.gen_nbr_edges(nodes)
    chart = graph.Graph(nodes, edges)
    chart.render(game)
    astarGoal = None
    # --------------------------------------------#
    test_start = [3, 4]
    test_goal = [7, 4]
    test_walls = [[4, 4], [5, 4], [6, 4]]
    # --------------------------------------------#

    for n in chart.nodes:
        if n.pos == test_start:
            chart.currentNode = n
        if n.pos == test_goal:
            astarGoal = n
        for wall in test_walls:
            if n.pos == wall:
                n.isWalkable = False

    test = stefmath.aStar(chart, astarGoal, stefmath.manhattan)

    # Todo : Test aStar
    # Printing to console to check test
    for node in test:
        print(node.pos)
"""