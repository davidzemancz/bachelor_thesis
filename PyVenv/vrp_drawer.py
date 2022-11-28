import random
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from vrp import VRP,Ride,Vehicle,Order

def draw(vrp):
    # Grid graph
    G = nx.Graph()
    plt.figure(figsize=(12,8))

    # Add edges and get plannar layout
    for ride in vrp.rides:
        for i in range(len(ride.nodes)-1):
            u = ride.nodes[i]
            v = ride.nodes[i+1]
            G.add_edge(u, v, weight = 1/abs(u-v), len=abs(u-v))
    pos = nx.spring_layout(G)

    # Nodes
    nx.draw_networkx_nodes(     # basic nodes
        G, 
        pos, 
        node_size = 600, 
        node_color="gray"
    )
    nx.draw_networkx_nodes(     # orders
        G, 
        pos,
        node_size = 600,
        nodelist=[order.node for order in vrp.orders],
        node_color="lightgreen",
    )
    nx.draw_networkx_nodes(     # depot
        G, 
        pos,
        node_size = 600,
        nodelist=[vrp.depot_node],
        node_color="lightblue"
    )
    labels = {order.node: f'{order.id};{order.demand}' for order in vrp.orders}
    labels[vrp.depot_node] = 'D'
    nx.draw_networkx_labels(G, pos, labels)

    # Draw edges
    for ride in vrp.rides:
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(ride.nodes[i], ride.nodes[i+1]) for i in range(len(ride.nodes)-1)],
            width=4,
            edge_color=(random.uniform(0.5,1), random.uniform(0.5,1), random.uniform(0.5,1)),
            alpha=1,
        )
    edge_labels = nx.get_edge_attributes(G, 'len')
    nx.draw_networkx_edge_labels(G, pos=pos, label_pos=0.5, edge_labels=edge_labels)

    # Plot graph
    plt.show()
