import networkx as nx
import numpy as np
from nest.graphstatistics.base import baseWithHistPlot
name = 'Centrality Approaches'


def __getStats__(q2):
    data = {}
    data['min'] = np.min(q2)
    data['mean'] = np.mean(q2)
    data['median'] = np.median(q2)
    data['max'] = np.max(q2)
    return data


class Betweenness(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        if len(G) > 1000:
            print('Betweenness approximation')
            q1 = nx.betweenness_centrality(G, k=int(len(G)*0.1))
        else:
            q1 = nx.betweenness_centrality(G)
        q2 = list(q1.values())
        self.data = __getStats__(q2)
        if len(G) > 1000:
            self.data['type'] = 'Approximation'
        else:
            self.data['type'] = 'Exact'
        self.histData = q2


class Katz_alpha_0_1(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        q1 = nx.katz_centrality_numpy(G)
        q2 = list(q1.values())
        self.data = __getStats__(q2)
        self.histData = q2


class Katz_alpha_0_01(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        q1 = nx.katz_centrality_numpy(G, alpha=0.01)
        q2 = list(q1.values())
        self.data = __getStats__(q2)
        self.histData = q2


class Katz_alpha_10_pow_m10(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        q1 = nx.katz_centrality_numpy(G, alpha=10**(-10))
        q2 = list(q1.values())
        self.data = __getStats__(q2)
        self.histData = q2


class Eigenvector(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        q1 = nx.eigenvector_centrality_numpy(G)
        q2 = list(q1.values())
        self.data = __getStats__(q2)
        self.histData = q2


class Kcore(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        G1 = G.copy().to_undirected()
        G1.remove_edges_from(nx.selfloop_edges(G))
        q1 = nx.core_number(G1)
        q2 = list(q1.values())
        self.data = __getStats__(q2)
        self.histData = q2
