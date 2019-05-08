from game import *
import graph


def main():
    """main execution func"""
    game = Game("game")

    nodes = graph.gen_nodes(10)
    edges = graph.gen_nbr_edges(nodes)
    chart = graph.Graph(nodes, edges)
    chart.render(game)

    currentPath = None

    # add the gameObjects here
    if game._startup():  # if the game starts up correctly
        while game._update():  # update the game if the game updates then
            game._draw()  # draw elements from the game
        game._shutdown()


if __name__ == "__main__":
    main()
