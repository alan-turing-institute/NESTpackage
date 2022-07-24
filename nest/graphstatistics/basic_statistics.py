import networkx as nx
from nest.graphstatistics.base import baseStatClass
from nest.graphstatistics.base import baseWithHistPlot
from nest.graphstatistics.base import baseTimeSeriesStats
from nest.graphstatistics.base import baseTimeSeriesWithHistPlot
from nest.graphstatistics.base import baseTimeSeriesFromBase
from nest.reportgenerator import plot_maker
from math import ceil, log
import numpy as np
name = 'Basic Network Statistics'

# Helper Functions

def __filterNan__(value,defaultValue):
    if np.isnan(value):
        return defaultValue
    return value

# Main functions


class number_of_nodes(baseStatClass):
    """
        Basic statistic: Number of Nodes
    """
    def __init__(self, G, optionsDict):
        self.data = G.number_of_nodes()

class number_of_nodes_TS(baseTimeSeriesFromBase):
    """
        Time Series Basic statistic: Number of Nodes
    """
    inbuiltMethod = number_of_nodes



class number_of_edges(baseStatClass):
    """
        Basic statistic: Number of Edges
    """
    def __init__(self, G, optionsDict):
        self.data = G.number_of_edges()

class number_of_edges_TS(baseTimeSeriesFromBase):
    """
        Time Series Basic statistic: Number of Edges
    """
    inbuiltMethod = number_of_edges


class density(baseStatClass):
    def __init__(self, G, optionsDict):
        self.data = nx.density(G)

class density_TS(baseTimeSeriesFromBase):
    inbuiltMethod = density

class number_of_triangles(baseStatClass):
    def __init__(self, G, optionsDict):
        Gtemp = G.to_undirected()
        self.data = sum(nx.triangles(Gtemp).values())/3.0


class number_of_triangles_TS(baseTimeSeriesFromBase):
    inbuiltMethod = number_of_triangles


class number_of_selfloops(baseStatClass):
    def __init__(self, G, optionsDict):
        self.data = len(list(nx.selfloop_edges(G)))


class number_of_selfloops_TS(baseTimeSeriesFromBase):
    inbuiltMethod = number_of_selfloops


class assortavitity(baseStatClass):
    def __init__(self, G, optionsDict):
        temp1 = nx.assortativity.degree_assortativity_coefficient(G)
        temp2 = __filterNan__(temp1,-2)
        self.data = temp2


class assortavitity_TS(baseTimeSeriesFromBase):
    inbuiltMethod = assortavitity


class assortavitity_Undirected(baseStatClass):
    def __init__(self, G1, optionsDict):
        G = G1.to_undirected()
        temp1 = nx.assortativity.degree_assortativity_coefficient(G)
        temp2 = __filterNan__(temp1,-2)
        self.data = temp2


class assortavitity_Undirected_TS(baseTimeSeriesFromBase):
    inbuiltMethod = assortavitity


class reciprocity(baseStatClass):
    def __init__(self, G, optionsDict):
        self.data = nx.reciprocity(G)


class reciprocity_TS(baseTimeSeriesFromBase):
    inbuiltMethod = reciprocity


class number_of_connected(baseStatClass):
    directed = False
    def __init__(self, G, optionsDict):
        self.data = nx.number_connected_components(G)

class number_of_connected_TS(baseTimeSeriesFromBase):
    inbuiltMethod = number_of_connected

class number_of_weakly_connected(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.data = nx.number_weakly_connected_components(G)

class number_of_weakly_connected_TS(baseTimeSeriesFromBase):
    directed = True
    inbuiltMethod = number_of_weakly_connected

class number_of_strongly_connected(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.data = nx.number_strongly_connected_components(G)

class number_of_strongly_connected_TS(baseTimeSeriesFromBase):
    directed = True
    inbuiltMethod = number_of_strongly_connected


class number_degree0(baseStatClass):
    directed = False
    def __init__(self, G, optionsDict):
        self.data = sum(1 for x in G if G.degree(x)==0)

class number_degree0_TS(baseTimeSeriesFromBase):
    directed = False
    inbuiltMethod = number_degree0

class number_outdegree0(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.data = sum(1 for x in G if G.out_degree(x)==0)

class number_outdegree0_TS(baseTimeSeriesFromBase):
    directed = True
    inbuiltMethod = number_outdegree0

class number_indegree0(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.data = sum(1 for x in G if G.in_degree(x)==0)

class number_indegree0_TS(baseTimeSeriesFromBase):
    directed = True
    inbuiltMethod = number_indegree0

class number_degree1(baseStatClass):
    directed = False
    def __init__(self, G, optionsDict):
        self.data = sum(1 for x in G if G.degree(x)==1)

class number_degree1_TS(baseTimeSeriesFromBase):
    directed = False
    inbuiltMethod = number_degree1

class number_outdegree1(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.data = sum(1 for x in G if G.out_degree(x)==1)

class number_outdegree1_TS(baseTimeSeriesFromBase):
    directed = True
    inbuiltMethod = number_outdegree1

class number_indegree1(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.data = sum(1 for x in G if G.in_degree(x)==1)

class number_indegree1_TS(baseTimeSeriesFromBase):
    directed = True
    inbuiltMethod = number_indegree1



from scipy import stats
def __getStats__(q2):
    data = {}
    data['min']  = np.min(q2)
    data['mean'] = np.mean(q2)
    data['median']  = np.median(q2)
    data['max']  = np.max(q2)
    data['variance']  = np.var(q2)
    data['skew']  = stats.skew(q2)
    data['kurtosis']  = stats.kurtosis(q2)
    return data


class degree_Hist(baseWithHistPlot):
    directed = False
    def __init__(self, G, optionsDict):
        deg  = list(dict(G.degree()).values())
        self.histData = deg
        self.histlog = True
        self.data = __getStats__(deg)

class in_degree_Hist(baseWithHistPlot):
    directed = True
    def __init__(self, G, optionsDict):
        indeg  = list(dict(G.in_degree()).values())
        self.histData = indeg
        self.histlog = True
        self.data = __getStats__(indeg)


class out_degree_Hist(baseWithHistPlot):
    directed = True
    def __init__(self, G, optionsDict):
        outdeg  = list(dict(G.out_degree()).values())
        self.histData = outdeg
        self.histlog = True
        self.data = __getStats__(outdeg)


class weight_hist(baseWithHistPlot):
    directed = False
    def __init__(self, G, optionsDict):
        def get_weight(x):
            return sum(G[x][y]['weight'] for y in G[x])
        weight = [get_weight(x) for x in G]
        self.histData = weight
        self.histlog = True
        self.data = __getStats__(weight)


class out_weight_hist(baseWithHistPlot):
    directed = True
    def __init__(self, G, optionsDict):
        def get_out_weight(x):
            return sum(G[x][y]['weight'] for y in G[x])
        outweight = [get_out_weight(x) for x in G]
        self.histData = outweight
        self.histlog = True
        self.data = __getStats__(outweight)


class in_weight_hist(baseWithHistPlot):
    directed = True
    def __init__(self, G, optionsDict):
        def get_in_weight(x):
            return sum(G[y][x]['weight'] for y, _ in G.in_edges(x))
        inweight = [get_in_weight(x) for x in G]
        self.histData = inweight
        self.histlog = True
        self.data = __getStats__(inweight)


class out_in_degree_heatmap(baseStatClass):
    directed = True
    def __init__(self, G, optionsDict):
        self.scatter = [(G.in_degree(x),G.out_degree(x)) for x in G]
        self.data = ''
    def makePlot(self):
        pylab = plot_maker.pylab
        scatter  = self.scatter
        b1 = [-0.5,0.5,1.5,2.5,3.5,4.5,5.5,10.5,20.5,50.5,100.5,]
        m3 = max(y for x in scatter for y in x)
        b1 += [0.5+10**i for i in range(3, ceil(log(m3)/log(10)))]
        fig, ax = pylab.subplots( figsize=( 5, 5) )
        scatter = np.array(scatter)
        b2 = np.array([b1,b1])
        aq1 = np.histogramdd(scatter,bins=b2)
        aq2 = np.ma.array(aq1[0], mask=(aq1[0]==0))
        aq1 = aq1[1][1]
        pylab.imshow(aq2,cmap='plasma',interpolation='nearest',origin='lower')
        for i in range(len(aq2)):
            for j in range(len(aq2)):
                if aq2[i,j]>0:
                    text = ax.text(j, i, int(aq2[i, j]),
                                   ha="center", va="center", color="r",fontsize=10)
        labels = [str(aq1[i])+'-'+str(aq1[i+1]) for i in range(len(b1)-1)]
        pylab.xticks(range(len(b1)-1),labels,rotation=90)
        pylab.yticks(range(len(b1)-1),labels)
        pylab.title('In-degree, Out degree Hist',fontsize=16)
        pylab.xlabel('Out Degree',fontsize=16)
        pylab.ylabel('In Degree',fontsize=16)
        pylab.colorbar()
        return [fig,]

