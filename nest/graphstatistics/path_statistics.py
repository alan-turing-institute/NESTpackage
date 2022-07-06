import networkx as nx
import numpy as np
from nest.graphstatistics.base import baseWithHistPlot
import random as rd

name = 'Path Statistics'


class Path_Dist(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        lengths = []
        nodes = list(G.nodes())
        for run in range(1000):
            n1, n2 = rd.sample(nodes, 2)
            if rd.random() < 0.5:
                n2, n1 = n1, n2
            try:
                l1 = nx.shortest_path_length(G, n1, n2)
            except nx.NetworkXNoPath:
                l1 = -20
            lengths.append(l1)
        self.histData = lengths
        self.data = {}
        self.data['min'] = np.min(lengths)
        self.data['mean'] = np.mean(lengths)
        self.data['median'] = np.median(lengths)
        self.data['max'] = np.max(lengths)


class Path_Dist_LSCC(baseWithHistPlot):
    def __init__(self, G1, optionsDict):
        nodes = max(nx.strongly_connected_components(G1), key=len)
        G = G1.subgraph(nodes)
        lengths = []
        nodes = list(G.nodes())
        for run in range(1000):
            n1, n2 = rd.sample(nodes, 2)
            if rd.random() < 0.5:
                n2, n1 = n1, n2
            try:
                l1 = nx.shortest_path_length(G, n1, n2)
            except nx.NetworkXNoPath:
                l1 = -20
            lengths.append(l1)
        self.histData = lengths
        self.data = {}
        self.data['min'] = np.min(lengths)
        self.data['mean'] = np.mean(lengths)
        self.data['median'] = np.median(lengths)
        self.data['max'] = np.max(lengths)
