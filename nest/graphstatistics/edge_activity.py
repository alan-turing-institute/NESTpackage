import networkx as nx
from nest.reportgenerator import plot_maker
import numpy as np
from nest.graphstatistics.base import baseTimeSeriesStats

name = 'Most active edges statistics'


class Most_active_edge_participation_per_day(baseTimeSeriesStats):
    def __init__(self, Gs, optionsDict):
        ts = []
        plotdata = []
        all_edges = []
        edge_dict = {}
        edge_info = []
        for g in Gs.values():
            all_edges+= list(g.edges.data())
        edge_ordered = sorted([(i,j,list(k.values())[0]) for i,j,k in all_edges], key = lambda x:x[2])[-1000:]

        for key1, key2, value in edge_ordered:
            edge_dict[(key1,key2)] = value
        for t in sorted(Gs):
            ts.append(t)
            G = Gs[t]
            #d1 = self.inbuiltMethod(G,{})
            edge_counter = 0
            active_edge_in_G = []
            for edge in G.edges():
                if edge in edge_dict.keys():
                    edge_counter += 1
                    active_edge_in_G.append(edge)
            edge_info.append((edge_counter,active_edge_in_G))
            plotdata.append(edge_counter)
        self.ts = ts
        self.plotData = plotdata
        data = {}
        data['min']     = np.min(plotdata)
        data['mean']    = np.mean(plotdata)
        #data['median']  = np.median(plotdata)
        data['std']     = np.std(plotdata)
        data['max']     = np.max(plotdata)

        self.data = data
        self.edges_value_distribution_ts = edge_info
    def makePlot(self):
        statName = type(self).__name__
        plots =  [plot_maker.linePlotTS(self.ts, self.plotData, statName),]
        plots += [plot_maker.makeHistogram(self.plotData, statName),]
        return plots

class Inter_arrival_times(baseTimeSeriesStats):
    def __init__(self, Gs, optionsDict):
        ts = []
        plotdata = []
        all_edges = []
        edge_dict = {}
        edge_info = {}
        for g in Gs.values():
            all_edges+= list(g.edges.data())
        edge_ordered = sorted([(i,j,list(k.values())[0]) for i,j,k in all_edges], key = lambda x:x[2])[-1000:]

        for key1, key2, value in edge_ordered:
            edge_dict[(key1,key2)] = value

        for t in sorted(Gs):
            G = Gs[t]

            #t = pd.to_datetime(t,dayfirst = True)

            ts.append(t)
            #d1 = self.inbuiltMethod(G,{})
            edge_counter = 0
            active_edge_in_G = []
            for edge in G.edges():
                if edge in edge_dict.keys():
                    edge_counter += 1
                    active_edge_in_G.append(edge)
            edge_info[t] = active_edge_in_G
            plotdata.append(edge_counter)
        time0 = ts[0]#pd.to_datetime(sorted(Gs)[0])
        edge_inter_time = {}
        for edge in edge_dict.keys():
            edge_inter_time[edge] = []
            for time, edge_list in edge_info.items():
                if edge in edge_list:
                    delta_time = time-time0
                    edge_inter_time[edge].append(delta_time.days)
                time0 = time
            time0 = ts[0]
        plotdata = [np.mean(l) for l in edge_inter_time.values()]
        self.ts = range(len(plotdata))
        self.plotData = plotdata
        data = {}
        data['min']     = np.min(plotdata)
        data['mean']    = np.mean(plotdata)
        #data['median']  = np.median(plotdata)
        data['std']     = np.std(plotdata)
        data['max']     = np.max(plotdata)

        self.data = data
    def makePlot(self):
        statName = type(self).__name__
        plots =  [plot_maker.linePlotTS(self.ts, self.plotData, statName),]
        plots += [plot_maker.makeHistogram(self.plotData, statName),]
        return plots


class Cascading_behaviour_over_3_days(baseTimeSeriesStats):
    def __init__(self, Gs, optionsDict):
        ts = []
        plotdata = []
        all_edges = []
        edge_dict = {}
        edge_info = {}
        for g in Gs.values():
            all_edges+= list(g.edges.data())
        edge_ordered = sorted([(i,j,list(k.values())[0]) for i,j,k in all_edges], key = lambda x:x[2])[-300:]


        ego_graphs = {}
        counter = 0
        edge_cascade_from_initial = []
        for top_edge in edge_ordered:
            edges_cascading = 0

            for t in sorted(Gs):

                G = Gs[t]
                if top_edge[1] in G.nodes():
                    if counter > 0:
                        ego_graphs[t] = nx.ego_graph(G,top_edge[1],radius = 1)
                        edges_cascading += len(list(ego_graphs[t].edges()))
                        counter += -1
                if (top_edge[0],top_edge[1]) in G.edges():

                    counter = 3
            edge_cascade_from_initial.append(edges_cascading)

        plotdata = [np.log(k+1) for k in edge_cascade_from_initial]
        self.plotData = plotdata
        data = {}
        data['min']     = np.min(edge_cascade_from_initial)
        data['mean']    = np.mean(edge_cascade_from_initial)
        #data['median']  = np.median(plotdata)
        data['std']     = np.std(edge_cascade_from_initial)
        data['max']     = np.max(edge_cascade_from_initial)
        self.data = data
        self.ts = range(len(plotdata))

    def makePlot(self):
        statName = type(self).__name__
        plots =  [plot_maker.linePlotTS(self.ts, self.plotData, statName),]
        plots += [plot_maker.makeHistogram(self.plotData, statName),]
        return plots
