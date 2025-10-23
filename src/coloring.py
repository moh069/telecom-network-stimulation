import networkx as nx

def greedy_coloring(G):
    """
    Assigns colors to nodes so no two adjacent nodes share the same color.
    Returns a dictionary: {node: color}.
    """
    coloring = nx.coloring.greedy_color(G, strategy='largest_first')
    return coloring
