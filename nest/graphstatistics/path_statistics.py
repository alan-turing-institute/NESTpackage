import networkx as nx
import numpy as np
from nest.graphstatistics.base import baseWithHistPlot
import random as rd

name = 'Path Statistics'


class Path_Dist(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        lengths = []
        self.data = {}
        if len(G)<3:
            self.data = "Cannot be (meaningfully) computed as the LSCC is of size less than 3."
            return
        elif len(G)<110:
            ## Do not need to rely on samples
            ## we can just compute everything
            ## as this is th largest scc
            ## do not need to worry about disconnections
            l1 = nx.shortest_path_length(G)
            lengths = []
            for item in l1:
                n1 = item[0]
                for n2 in item[1]:
                    if n1!=n2:
                        lengths.append(item[1][n2])
            self.data['method'] = "exact"
        else:
            ## Rely on samples
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
            self.data['method'] = "sampled"
        self.histData = lengths
        self.data['min'] = np.min(lengths)
        self.data['mean'] = np.mean(lengths)
        self.data['median'] = np.median(lengths)
        self.data['max'] = np.max(lengths)
        self.data['num_points'] = len(lengths)


class Path_Dist_LSCC(baseWithHistPlot):
    def __init__(self, G1, optionsDict):
        nodes = max(nx.strongly_connected_components(G1), key=len)
        G = G1.subgraph(nodes)
        self.data = {}
        if len(G)<3:
            self.data = "Cannot be (meaningfully) computed as the LSCC is of size less than 3."
            return
        elif len(G)<110:
            ## Do not need to rely on samples
            ## we can just compute everything
            ## as this is th largest scc
            ## do not need to worry about disconnections
            print("shortcut")
            l1 = nx.shortest_path_length(G)
            lengths = []
            for item in l1:
                n1 = item[0]
                for n2 in item[1]:
                    if n1!=n2:
                        lengths.append(item[1][n2])
            self.data['method'] = "exact"
        else:
            ## Rely on samples
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
            self.data['method'] = "sampled"
        self.histData = lengths
        self.data['min'] = np.min(lengths)
        self.data['mean'] = np.mean(lengths)
        self.data['median'] = np.median(lengths)
        self.data['max'] = np.max(lengths)
        self.data['num_points'] = len(lengths)
