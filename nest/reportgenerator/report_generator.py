from inspect import isclass
from nest.graphcreator import make_graph as mg
from nest.graphstatistics.base import baseStatClass
from nest.graphstatistics.base import baseTimeSeriesStats
from nest.reportgenerator import plot_maker
from pandas.api.types import is_numeric_dtype
from sklearn.metrics import mutual_info_score
from typing import List
import csv
from nest import graphstatistics
import numpy as np
import pandas as pd
import sys

VERSION = 1.0

def getAllStatistics(G, reqStats=lambda x: True):
    """ Computes all network statistics on a graph graph of choice
    Note the computed statistics are still in the nest class structure which is
    used to construct the pdf outputs.

    :param G: A networkx graph
    :param reqStats: A function to filter the statistics produces defaults to true
    :return: A dictionary of the results of each of the statistics
    """

    result = {}
    for statModule in graphstatistics.statModules:
        result[statModule.name] = {}
        vStat0 = vars(statModule)
        vStat = {x:vStat0[x] for x in list(vStat0)}
        for meth in vStat:
            if isclass(vStat[meth]) and issubclass(vStat[meth], baseStatClass):
                if vStat[meth].__module__ != 'nest.graphstatistics.base':
                    if reqStats(vStat[meth]):
                        tempRes = vStat[meth](G, reqStats)
                        name = meth.split('_')
                        name = [x.capitalize() for x in name]
                        name = ' '.join(name)
                        result[statModule.name][name] = tempRes
    return result


def getAllTimeSeriesStatistics(Gs, reqStats=lambda x: True):
    """ Computes all temporal network statistics on a graph graph of choice
    Note the computed statistics are still in the nest class structure which is
    used to construct the pdf outputs.

    :param Gs: A time series of networkx graphs as a dictionary
    :param reqStats: A function to filter the statistics produces defaults to true
    :return: A dictionary of the results of each of the statistics
    """
    result = {}
    for statModule in graphstatistics.statModules:
        result[statModule.name] = {}
        vStat0 = vars(statModule)
        vStat = {x:vStat0[x] for x in list(vStat0)}
        for meth in vStat:
            if isclass(vStat[meth]):
                if issubclass(vStat[meth], baseTimeSeriesStats):
                    if vStat[meth].__module__ != 'nest.graphstatistics.base':
                        if reqStats(vStat[meth]):
                            tempRes = vStat[meth](Gs, reqStats)
                            name = meth.split('_')
                            name = ' '.join([x.capitalize() for x in name])
                            result[statModule.name][name] = tempRes
    return result



def __addStatToOutput__(secNum, stats, renderer, csvObj, csvStart):
    sections = [x for x in stats if len(stats[x]) > 0]
    for idx, statType in enumerate(sorted(sections)):
        if idx != 0:
            renderer.addPageBreak()

        name = 'Section '+secNum+'.'+str(1+idx) + ' ' + statType
        renderer.addHeading(2, name)

        for innerIdx, stat in enumerate(stats[statType]):
            # Print current status
            print(['Section '+str(secNum),statType,stat])
            sys.stdout.flush()
            if hasattr(stats[statType][stat], 'makePlot') and innerIdx != 0:
                renderer.addPageBreak()
            for row in stats[statType][stat].get_csv():
                csvObj.writerow([csvStart, statType, stat, ]+row)
            val = stats[statType][stat].get_report()
            renderer.addHeading(3,stat)
            if isinstance(val, dict):
#                if 'unweighted_mean' in val:
#                    import pdb
#                    pdb.set_trace()
                renderer.addTableFromDict(val)
            elif type(val) == str:
                renderer.addText(val)
            else:
                print('my val is not text huh?')
                import pdb
                pdb.set_trace()
                #flowables.append(val)
            if hasattr(stats[statType][stat], 'makePlot'):
                for plot in stats[statType][stat].makePlot():
                    renderer.addPlot(plot)



# based on
# https://medium.com/@vonkunesnewton/generating-pdfs-with-reportlab-ced3b04aedef
def makeFullReport(rendererClass, df: pd.DataFrame, filename: str,name: str,
                   srcCols: List[str], dstCols: List[str],
                   weightCol: str, timeCol: str,options={}):
    """
    Main function of Nest. This function takes the dataset, and the renderer
    and the metadata and combines this into the report.

    :param rendererClass: The renderer to use to use (e.g. reportlabPDF), see the renderer module for a list of possible options.
    :param df: A pandas dataframe containing the edge list
    :param filename: The filename to store the resultant output
    :param name: The name of the dataset (used for titles)
    :param srcCols: The column(s) used to construct the source node
    :param dstCols: The column(s) used to construct the destination node
    :param weightCol: The column which stores the edge weight.  If none the function assumes that all weights are 1.
    :param timeCol: The column which stores the temporal index If none, we assume that the data is static.


    :return: Functions saves output to disk.
    """



    fcsv = open(filename.split('.')[0]+'.csv', 'w')
    csvObj = csv.writer(fcsv)
    headerRow = ['Data Type', 'Method Type', 'Statistic/Name', 'Measure',
                 'Value']
    csvObj.writerow(headerRow)

    ## Make the render class object
    ## This also adds the front page
    renderer = rendererClass(filename,name,options)

    ## Section 1, Column summaries
    renderer.addSectionPage('Section 1: Column Summaries')

    # Get basic data
    for col in df:
        renderer.addHeading(3,'Summary Statisics: '+col)
        # Create a simple summary table
        # could be replaced with describe
        if is_numeric_dtype(df[col]):
            table = []
            table.append(['Min', df[col].min()])
            table.append(['Mean', df[col].mean()])
            table.append(['Median', df[col].median()])
            table.append(['Max', df[col].max()])

            ## Add this as a table to the document
            renderer.addTable(table)

            ## Add a distribution plot
            plot = plot_maker.distPlot(df[col], col)
            renderer.addPlot(plot)

            for x in table:
                csvObj.writerow(['Column data', 'Summary Stat', col, ]+x)

        ## Add additional plots here
        plot = plot_maker.rankPlot(df[col], col)
        renderer.addPlot(plot)
        plot = plot_maker.countPlot(df[col], col)
        renderer.addPlot(plot)

        # Add a page break to split this up
        renderer.addPageBreak()

        # Making a CSV file of the data
        countCsv=df[col].value_counts(sort=True,normalize=True).nlargest(10)
        for x in countCsv.items():
            csvObj.writerow(['Column data', 'HighRanks', col, x[0], x[1]])

    mutualInfoMatrix = np.zeros((len(df.columns), len(df.columns)))
    for ix1, col1 in enumerate(df):
        for ix2, col2 in enumerate(df):
            val = mutual_info_score(df[col1], df[col2])
            mutualInfoMatrix[ix1][ix2] = val
            if ix1 < ix2:
                csvObj.writerow(['Column data', 'MutualInfo', col1, col2, val])

    renderer.addText('Mutual Information')
    plot = plot_maker.makeImshow(mutualInfoMatrix, 'MutualInfo')
    renderer.addPlot(plot)

    renderer.addPageBreak()
    renderer.addSectionPage('Section 2: Full Graph stats')


    if weightCol is None:
        # a weight column with value 1 if there is no weight specified
        df["temp_weight_col"] = 1.0
        weightCol = "temp_weight_col"

    G = mg.makeDirectedGraph(df, srcCols, dstCols, weightCol)
    stats = getAllStatistics(G)
    __addStatToOutput__('2', stats, renderer, csvObj, 'FullGraph')

    renderer.addPageBreak()
    renderer.addSectionPage('Section 3: Time Series Graph stats')

    if timeCol is not None:

        # If there is a time column

        Gs = mg.makeTimeSeriesOfGraphs(df, timeCol, srcCols, dstCols, weightCol)
        stats = getAllTimeSeriesStatistics(Gs)
        __addStatToOutput__('3', stats, renderer, csvObj, 'GraphTs')
    fcsv.close()

    ## Final render step
    renderer.render()
