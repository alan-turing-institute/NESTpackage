from reportGenerator import reportGenerator
import argparse
import networkx as nx
import pandas as pd
import datetime
import random as rd
import sys




def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Compute Nest Network statistics',
        usage='runArgs.py [<args>] [-h | --help]'
    )

    parser.add_argument('--data_file', type=str, default=None,
                            help="Csv file path ",metavar='')
    parser.add_argument('--src', type=str, default=None,
                            help = 'Source Columns separated by commas',
                            metavar='')
    parser.add_argument('--dst', type=str, default=None,
                            help = 'Dest Columns separated by commas',
                            metavar='')
    parser.add_argument('--weight', type=str, default=None,
                            help = 'Weight Column', metavar='')
    parser.add_argument('--time', type=str, default=None,
                            help = 'Time Column', metavar='')
    parser.add_argument('--output_file', type=str, default='testTS.pdf',
                            help = 'Output file', metavar='')
    parser.add_argument('--data_name', type=str, default='Test',
                            help = 'Data set name', metavar='')

    return parser.parse_args(args)


def main(args):

    # Load data
    if args.data_file is None:
        args.data_file = 'exampleData.csv'

    df = pd.read_csv(args.data_file)

    if args.src is None:
        args.src = [df.columns[1], df.columns[2]]
        print('No source column provided using ', args.src)
    else:
        args.src = args.src.split(',')
        for item in args.src:
            if item not in df.columns:
                raise Exception('Column',item,' not found')

    if args.dst is None:
        args.dst = [df.columns[3], df.columns[4]]
        print('No dest column provided using ', args.dst)
    else:
        args.dst = args.dst.split(',')
        for item in args.dst:
            if item not in df.columns:
                raise Exception('Column',item,' not found')

    if args.weight is None:
        args.weight = df.columns[-2]
        print('No weight column provided using ', args.weight)
    else:
        if args.weight not in df.columns:
            raise Exception('Column',args.weight,' not found')

    if args.time is None:
        args.time = df.columns[-1]
        print('No time column provided using ', args.time)
    else:
        if args.time not in df.columns:
            raise Exception('Column',args.time,' not found')

    if args.output_file == 'testTS.pdf':
        print('No filename provided using ', args.output_file)

    if args.data_name == 'Test':
        print('No data name provided using ', args.data_name)

    reportGenerator.makeFullReport(df, args.output_file, args.data_name,
                                   args.src, args.dst, args.weight, args.time)


if __name__ == '__main__':
    main(parse_args())
