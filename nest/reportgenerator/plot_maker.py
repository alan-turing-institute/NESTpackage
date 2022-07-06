from matplotlib import pylab
import seaborn as sns
import networkx as nx
sns.set()

MODE = "pandoc"


def distPlot(data, name):
    figure = pylab.figure(figsize=(5, 2.4))
    # distplot has been deprecated
    sns.distplot(data)
    pylab.title(name)
    return figure


def makeSpy(data, name):
    figure = pylab.figure(figsize=(5, 5))
    pylab.spy(data, markersize=1)
    pylab.title(name)
    return figure


def makeImshow(data, name):
    figure = pylab.figure(figsize=(6, 6))
    sns.heatmap(data, annot=True, fmt='.0e', annot_kws={"size": 8})
    pylab.title(name)
    return figure


def makeHistogram(data, name, log=False):
    figure = pylab.figure(figsize=(5, 2.4))
    pylab.hist(data, bins='doane')
    pylab.xlabel(name)
    pylab.ylabel('Freq')
    pylab.title(name)
    if log:
        pylab.yscale('log')
    return figure


def linePlot(ts, ys, title):
    figure = pylab.figure(figsize=(5, 2.3))
    pylab.plot(ts, ys, '--*')
    pylab.xticks(rotation=90, fontsize=8)
    pylab.title(title)
    return figure


def linePlotTS(ts, ys, title):
    figure = pylab.figure(figsize=(5, 2.4))
    pylab.plot(ts, ys)
    pylab.xlabel('Time')
    pylab.ylabel('Frequency')
    pylab.title(title)
    return figure


def rankPlot(df, col):
    ran = df.value_counts(sort=True)
    figure = pylab.figure(figsize=(5, 2.4))
    pylab.plot(range(len(ran)), ran)
    pylab.ylabel('Freq.')
    pylab.xlabel('Rank')
    pylab.title(col)
    return figure


def neighborhoodPlot(subg):
    figure = pylab.figure(figsize=(5, 2.4))
    nx.draw_networkx(subg, pos=nx.spring_layout(subg))
    axis = pylab.gca()
    axis.set_xlim([1.5*x for x in axis.get_xlim()])
    axis.set_ylim([1.5*y for y in axis.get_ylim()])
    return figure


def countPlot(df, col):
    figure = pylab.figure(figsize=(5, 2.4))
    df.value_counts(sort=True, normalize=True).nlargest(10).plot(kind='bar')
    pylab.ylabel('Freq.')
    pylab.xlabel(col)
    pylab.title(col)
    return figure
