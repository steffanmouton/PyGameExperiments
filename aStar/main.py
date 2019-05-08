from game import *
import graph
import stefmath


def main():
    """main execution func"""
    game = Game("game")

    nodes = graph.gen_nodes(3)
    edges = graph.gen_nbr_edges(nodes)
    chart = graph.Graph(nodes, edges)
    chart.render(game)
    g1 = chart.nodes[8]
    test = stefmath.aStar(chart, g1, stefmath.manhattan)

    # add the gameObjects here
    if game._startup():  # if the game starts up correctly
        while game._update():  # update the game if the game updates then
            game._draw()  # draw elements from the game
        game._shutdown()


if __name__ == "__main__":
    main()
