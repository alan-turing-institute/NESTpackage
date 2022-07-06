import networkx as nx
from nest.reportgenerator import plot_maker
from nest.graphstatistics.base import baseStatClass
name = 'Initial Visualisation'



class MatrixPlot(baseStatClass):
    def __init__(self, G, optionsDict):
        n1 = sorted([(y,x) for x,y in dict(G.out_degree()).items()])
        n2 = [x[1] for x in n1]
        A = nx.to_scipy_sparse_matrix(G,nodelist=n2)
        self.A = A
    def get_csv(self):
        return []
    def get_report(self):
        return ''
    def makePlot(self):
        statName = type(self).__name__
        return [plot_maker.makeSpy(self.A,statName),]

