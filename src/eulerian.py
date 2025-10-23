import networkx as nx

def make_eulerian_multigraph(G):
    """
    Returns a multigraph where all nodes have even degree for Eulerian circuit.
    """
    M = nx.MultiGraph(G)  # copy graph as multigraph
    odd_nodes = [v for v, d in M.degree() if d % 2 == 1]

    # Pair odd degree nodes arbitrarily and add edges
    for i in range(0, len(odd_nodes), 2):
        u = odd_nodes[i]
        v = odd_nodes[i + 1]
        M.add_edge(u, v, weight=0)  # add edge of weight 0

    return M

def fleury_route(G):
    """
    Returns an Eulerian circuit (list of edges) using Fleury's algorithm.
    Works for MultiGraph and NetworkX >=3.0.
    """
    if not nx.is_eulerian(G):
        raise ValueError("Graph is not Eulerian")

    G_copy = G.copy()
    circuit = []
    u = next(iter(G_copy.nodes()))

    while G_copy.number_of_edges() > 0:
        neighbors = list(G_copy.neighbors(u))
        if not neighbors:
            break
        v = neighbors[0]  # pick first neighbor
        circuit.append((u, v))
        G_copy.remove_edge(u, v)
        u = v

    return circuit
