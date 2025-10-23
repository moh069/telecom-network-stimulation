import networkx as nx

def kruskal_mst(G):
    """
    Returns the Minimum Spanning Tree using Kruskal's algorithm.
    """
    T = nx.Graph()
    # Add minimum=True to fix NetworkX 3.x signature
    for u, v, w in nx.algorithms.tree.mst.kruskal_mst_edges(G, minimum=True, data=True):
        T.add_edge(u, v, weight=w['weight'])
    return T

def prim_mst(G):
    """
    Returns the Minimum Spanning Tree using Prim's algorithm.
    """
    T = nx.Graph()
    for u, v, w in nx.algorithms.tree.mst.prim_mst_edges(G, data=True):
        T.add_edge(u, v, weight=w['weight'])
    return T
