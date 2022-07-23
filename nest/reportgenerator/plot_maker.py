from matplotlib import pylab
import seaborn as sns
import networkx as nx
sns.set()

MODE = "pandoc"


def distPlot(data, name):
    """Constructs a dist plot from set of data

    :param data: Data assumed to be a column of values for the plot
    :param name: Name used for the title
    :return: Figure handle of the resultant plot
    """

    temp1 = sns.displot(data,kde=True)
    temp1.set_titles(name)
    return temp1


def makeSpy(data, name):
    """Constructs a spy plot from set of data

    :param data: Data assumed to be a column of values for the plot
    :param name: Name used for the title
    :return: Figure handle of the resultant plot
    """
    figure = pylab.figure(figsize=(5, 5))
    pylab.spy(data, markersize=1)
    pylab.title(name)
    return figure


def makeImshow(data, name):
    """Constructs a imshow plot from set of data

    :param data: Data assumed to be a column of values for the plot
    :param name: Name used for the title
    :return: Figure handle of the resultant plot
    """
    figure = pylab.figure(figsize=(6, 6))
    sns.heatmap(data, annot=True, fmt='.0e', annot_kws={"size": 8})
    pylab.title(name)
    return figure


def makeHistogram(data, name, log=False):
    """Constructs a imshow plot from set of data

    :param data: Data assumed to be a column of values for the plot
    :param name: Name used for the title
    :param log: Boolean variable which log transforms the y axis
    :return: Figure handle of the resultant plot
    """
    figure = pylab.figure(figsize=(5, 2.4))
    pylab.hist(data, bins='doane')
    pylab.xlabel(name)
    pylab.ylabel('Freq')
    pylab.title(name)
    if log:
        pylab.yscale('log')
    return figure


def linePlot(ts, ys, title):
    """Constructs line plot plot from set of data
    with no y axis label

    :param ts: X values for the line plot
    :param ys: Y values for the line plot
    :param title: Title for the plot
    :return: Figure handle of the resultant plot
    """
    figure = pylab.figure(figsize=(5, 2.3))
    pylab.plot(ts, ys, '--*')
    pylab.xticks(rotation=90, fontsize=8)
    pylab.title(title)
    return figure


def linePlotTS(ts, ys, title):
    """Constructs a temporal line plot from set of data
    with a axis labels

    :param ts: X values for the line plot
    :param ys: Y values for the line plot
    :param title: Title for the plot
    :return: Figure handle of the resultant plot
    """
    figure = pylab.figure(figsize=(5, 2.4))
    pylab.plot(ts, ys)
    pylab.xlabel('Time')
    pylab.ylabel('Frequency')
    pylab.title(title)
    return figure


def rankPlot(df, col):
    """Constructs a rank plot from a column of a dataframe

    :param df: data frame
    :param col: Column to construct the rank plot from.
    :return: Figure handle of the resultant plot
    """
    ran = df.value_counts(sort=True)
    figure = pylab.figure(figsize=(5, 2.4))
    pylab.plot(range(len(ran)), ran)
    pylab.ylabel('Freq.')
    pylab.xlabel('Rank')
    pylab.title(col)
    return figure


def neighborhoodPlot(subg):
    """Constructs a network plot

    :param subg: A networkx graph
    :return: Figure handle of the resultant plot
    """
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
