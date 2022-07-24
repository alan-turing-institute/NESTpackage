import networkx as nx
import numpy as np
from scipy import sparse
from numpy import linalg
from nest.graphstatistics.base import baseStatClass
from nest.graphstatistics.base import baseWithHistPlot
from nest.reportgenerator import plot_maker
from collections import Counter
import community
name = 'Communities'


class Louvain(baseWithHistPlot):
    def __init__(self, G, optionsDict):
        print('community --> not weighted')
        q1 = community.best_partition(G.to_undirected())
        m1 = max(q1.values())+1
        numer = np.zeros((m1,m1))
        denom = np.zeros((m1,m1))
        counts = Counter(q1.values())
        for c1 in range(m1):
            for c2 in range(m1):
                denom[c1][c2] = counts[c1]*counts[c2]

        for x1 in sorted(G):
            c1 = q1[x1]
            for x2 in sorted(G):
                c2 = q1[x2]
                if G.has_edge(x1,x2):
                    numer[c1][c2]+=1
        self.imData = numer/denom
        q2 = list(q1.values())
        self.data = {'numComs':1+max(q2)}
        self.histData = q2
    def makePlot(self):
        statName = type(self).__name__
        p1 = [plot_maker.makeHistogram(self.histData, statName),]
        p1 += [plot_maker.makeImshow(self.imData, statName),]
        return p1



class Louvain_lcc(baseWithHistPlot):
    def __init__(self, G1, optionsDict):
        print('community --> not weighted')
        if isinstance(G1,nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        q1 = community.best_partition(G.to_undirected())
        m1 = max(q1.values())+1
        numer = np.zeros((m1,m1))
        denom = np.zeros((m1,m1))
        counts = Counter(q1.values())
        for c1 in range(m1):
            for c2 in range(m1):
                denom[c1][c2] = counts[c1]*counts[c2]

        for x1 in sorted(G):
            c1 = q1[x1]
            for x2 in sorted(G):
                c2 = q1[x2]
                if G.has_edge(x1,x2):
                    numer[c1][c2]+=1
        self.imData = numer/denom
        q2 = list(q1.values())
        self.data = {'numComs':1+max(q2)}
        self.histData = q2
    def makePlot(self):
        statName = type(self).__name__
        p1 = [plot_maker.makeHistogram(self.histData, statName),]
        p1 += [plot_maker.makeImshow(self.imData, statName),]
        return p1

