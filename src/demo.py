import os
import networkx as nx
import matplotlib.pyplot as plt
# Ensure outputs folder exists
os.makedirs('outputs', exist_ok=True)


from src.graph_utils import generate_sample_graph
from src.mst import kruskal_mst, prim_mst
from src.eulerian import make_eulerian_multigraph, fleury_route
from src.coloring import greedy_coloring
import csv

def plot_graph(G, title, path=None, edge_labels=True):
    """
    Plots the graph and saves to file if path is provided.
    """
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_size=600)
    if edge_labels:
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    if path:
        plt.savefig(path, bbox_inches='tight')
    else:
        plt.show()
    plt.close()

if __name__ == '__main__':
    # 1. Generate sample graph
    G = generate_sample_graph()
    plot_graph(G, 'Original Cable Graph', 'outputs/original_graph.png')

    # 2. Minimum Spanning Tree
    T = kruskal_mst(G)
    plot_graph(T, 'Kruskal MST (backbone)', 'outputs/mst.png')

    # 3. Eulerian inspection route
    M = make_eulerian_multigraph(G)
    route = fleury_route(M)
    with open('outputs/eulerian_route.txt','w') as f:
        for u, v in route:
            f.write(f"{u} -> {v}\n")

    # 4. Maintenance schedule (Greedy Coloring)
    coloring = greedy_coloring(G)
    with open('outputs/schedule.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['city','day'])
        for city, color in coloring.items():
            writer.writerow([city, color])

    print('Demo complete. outputs/ contains generated files.')
