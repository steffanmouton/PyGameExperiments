from game import *
from gameObject import *
from graphObject import *
from lineObject import *
import graph
import graphrenderer


def main():
    '''main execution func'''
    game = Game("game")

    #To Test the graph renderer, uncomment the following code
    n1 = graph.Node(1, (200, 200))
    n2 = graph.Node(2, (200, 500))
    n3 = graph.Node(3, (500, 500))
    n4 = graph.Node(4, (500, 200))
    node_list = [n1, n2, n3, n4]

    e1 = graph.Edge(n1, n2)
    e2 = graph.Edge(n2, n3)
    e3 = graph.Edge(n2, n4)
    edge_list = [e1, e2, e3]
    ### Set 'chart' below to your instance of a graph.
    ### A 'graph' takes in two parameters: Graph(nodes_list, edges_list)
    chart = graph.Graph(node_list, edge_list)
    chart.render(game)

    #add the gameObjects here
    if game._startup():#if the game starts up correctly
        while game._update():#update the game if the game updates then
            game._draw()#draw elements from the game
        game._shutdown()

if __name__ == "__main__":
    main()