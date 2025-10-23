import networkx as nx
import json

def generate_sample_graph():
    """
    Generates a sample telecom cable network graph.
    Nodes represent cities; edges represent cable connections with weights.
    """
    G = nx.Graph()
    G.add_weighted_edges_from([
        (1, 2, 100),
        (1, 3, 250),
        (2, 3, 200),
        (2, 4, 300),
        (3, 4, 400),
        (3, 6, 1200),
        (2, 5, 1100)
    ])
    return G

def save_graph_data(G, filename):
    """
    Saves graph data in node-link JSON format.
    """
    data = nx.node_link_data(G)
    with open(filename, 'w') as f:
        json.dump(data, f)
