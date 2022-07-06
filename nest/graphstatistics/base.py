import numpy as np
from nest.reportgenerator import plot_maker



class baseStatClass:
    def get_csv(self):
        if isinstance(self.data, dict):
            return [list(x) for x in self.data.items()]
        return [['value', str(self.data), ]]

    def get_report(self):
        if isinstance(self.data, dict):
            return self.data
        return str(self.data)


class baseWithHistPlot(baseStatClass):
    def get_csv(self):
        if isinstance(self.data, dict):
            res = [list(x) for x in self.data.items()]
        else:
            res = [['', str(self.data), ]]
        res.append(['NumRecords', len(self.histData)])
        values, edges = np.histogram(self.histData, bins='doane')
        for i in range(101):
            p1 = np.percentile(self.histData, i)
            res.append(['percentile '+str(i), p1])
        return res

    def makePlot(self):
        statName = type(self).__name__
        if hasattr(self, 'histlog') and self.histlog:
            return [plot_maker.makeHistogram(self.histData, statName, True), ]
        else:
            return [plot_maker.makeHistogram(self.histData, statName), ]


class baseTimeSeriesStats:
    def get_csv(self):
        if isinstance(self.data, dict):
            return [list(x) for x in self.data.items()]
        return str(self.data)

    def get_report(self):
        if isinstance(self.data, dict):
            return self.data
        return str(self.data)


class baseTimeSeriesWithHistPlot(baseTimeSeriesStats):
    def get_csv(self):
        if isinstance(self.data, dict):
            res = [list(x) for x in self.data.items()]
        else:
            res = [['', str(self.data), ]]
        res.append(['NumRecords', len(self.histData)])
        values, edges = np.histogram(self.histData, bins='doane')
        for i in range(101):
            p1 = np.percentile(self.histData, i)
            res.append(['percentile '+str(i), p1])
        return res

    def makePlot(self):
        statName = type(self).__name__
        return [plot_maker.makeHistogram(self.histData, statName), ]


class baseTimeSeriesFromBase(baseTimeSeriesStats):
    def __init__(self, Gs, optionsDict):
        ts = []
        plotdata = []
        for t in sorted(Gs):
            ts.append(t)
            G = Gs[t]
            d1 = self.inbuiltMethod(G, {})
            plotdata.append(d1.data)
        self.ts = ts
        self.plotData = plotdata
        data = {}
        data['min'] = np.min(plotdata)
        data['mean'] = np.mean(plotdata)
        data['median'] = np.median(plotdata)
        data['max'] = np.max(plotdata)
        self.data = data

    def get_csv(self):
        if isinstance(self.data, dict):
            res = [list(x) for x in self.data.items()]
        else:
            res = [['', str(self.data), ]]
        res.append(['NumRecords', len(self.plotData)])
        values, edges = np.histogram(self.plotData, bins='doane')
        for i in range(101):
            p1 = np.percentile(self.plotData, i)
            res.append(['percentile '+str(i), p1])
        for timePoint, data in zip(self.ts, self.plotData):
            res.append(['TimePoint '+str(timePoint), data])
        return res

    def makePlot(self):
        statName = type(self).__name__
        plots = [plot_maker.linePlot(self.ts, self.plotData, statName), ]
        plots += [plot_maker.makeHistogram(self.plotData, statName), ]
        return plots
