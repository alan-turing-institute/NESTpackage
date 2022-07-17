import networkx as nx
from typing import List
import pandas as pd


def makeDirectedGraph(df, srcColNames: List[str], dstColNames: List[str],
                      weightCol: str):
    """ Constructs a graph from a dataframe.  This function takes a dataframe
    and constructs a graph in which each of the rows represents an edge.

    :param df: pandas dataframe where each row represents an edge
    :param srcColNames: Columns that represent the source columns
    :param dstColNames: Columns that represent the destination columns
    :param weightCol: Column that represents the edge weight
    :return: A networkx graph
    """
    # combine the columns
    cols = list(srcColNames) + list(dstColNames)
    # group over the columns 
    df1 = df.groupby(cols, as_index=False, observed=False)
    # sum over the column
    df2 = df1[weightCol].sum()
    # make new columns
    df2['src'] = df2[srcColNames].apply(tuple, axis=1)
    df2['dst'] = df2[dstColNames].apply(tuple, axis=1)
    #
    G = nx.from_pandas_edgelist(df2, 'src', 'dst', edge_attr=weightCol,
                                create_using=nx.DiGraph)
    for x in G:
        for y in G[x]:
            G[x][y]['weight'] = G[x][y][weightCol]
    return G

def makeTimeSeriesOfGraphs(df,timeCol: str, srcColNames: List[str],
                           dstColNames: List[str], weightCol: str):
    """ Constructs a graph from a dataframe.  This function takes a dataframe
    and constructs a graph in which each of the rows represents an edge.

    :param df: pandas dataframe where each row represents an edge
    :param timeCol: Columns that represent the time column
    :param srcColNames: Columns that represent the source columns
    :param dstColNames: Columns that represent the destination columns
    :param weightCol: Column that represents the edge weight
    :return: A networkx graph
    """
    result = {}

    df['tempCol'] = pd.to_datetime(df[timeCol],dayfirst=True)

    for time, df_t in df.groupby('tempCol'):
        Gt = makeDirectedGraph(df_t, srcColNames, dstColNames, weightCol)
        result[time] = Gt

    del df['tempCol']
    return result
