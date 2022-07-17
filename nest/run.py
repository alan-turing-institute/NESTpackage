from nest.reportgenerator import report_generator
from nest import renderer
import argparse
import networkx as nx
import pandas as pd
import datetime
import random as rd
import sys
import os




def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Compute Nest Network statistics.',
        epilog = 'The data is assumed to be unweighted and static unless otherwise specified.',
        usage='nest [<args>] [-h | --help]'
    )

    parser.add_argument('--data_file', type=str, default=None,
                            help="Csv file path ",metavar='')
    parser.add_argument('--src', type=str, default=None,
                            help = 'Source Column(s) separated by commas (Default Column 1)',
                            metavar='')
    parser.add_argument('--dst', type=str, default=None,
                            help = 'Dest Column(s) separated by commas (Default Column 2)',
                            metavar='')
    parser.add_argument('--weight', type=str, default=None,
                            help = 'Weight Column (Default None)', metavar='')
    parser.add_argument('--time', type=str, default=None,
                            help = 'Time column (Default None)', metavar='')
    parser.add_argument('--output_type', type=str, default="reportlabPDF",
                            help = 'Specify the output type, current options are reportlabPDF (default), pandocPDF and pandocHTML', metavar='')

    parser.add_argument('--output_file', type=str, default='testTS',
                            help = 'Output file', metavar='')
    parser.add_argument('--data_name', type=str, default='Test',
                            help = 'Data set name', metavar='')

    return parser.parse_args(args)


def main():
    args = parse_args()

    # Load data
    if args.data_file is None:
        raise Exception('Data filename not given.')

    if not os.path.exists(args.data_file):
        raise Exception('We could not find the data file you specified')


    df = pd.read_csv(args.data_file)

    if args.src is None:
        args.src = [df.columns[0], ]
        print('No source column provided using', args.src)
    else:
        args.src = args.src.split(',')
        for item in args.src:
            if item not in df.columns:
                raise Exception('Column',item,' not found')

    if args.dst is None:
        args.dst = [df.columns[1], ]
        print('No dest column provided using ', args.dst)
    else:
        args.dst = args.dst.split(',')
        for item in args.dst:
            if item not in df.columns:
                raise Exception('Column',item,' not found')

    if (args.weight is not None) and (args.weight not in df.columns):
        raise Exception('Column',args.weight,' not found')

    if args.time is None:
        print('No time column provided,')
    else:
        if args.time not in df.columns:
            raise Exception('Column',args.time,' not found')

    if args.output_file == 'testTS':
        print('No filename provided using ', args.output_file)

    if args.data_name == 'Test':
        print('No data name provided using ', args.data_name)



    if args.output_type not in renderer.renderer_list:
            print('\n\nThe output type ',args.output_type,' is not known. Possible options are:')
            for item in renderer.renderer_list:
                print(item)
            print("\n")
            raise Exception('Unknown renderer type')
    else:
        if args.output_type in renderer.renderer_dict:
            rend = renderer.renderer_dict[args.output_type]
        else:
            # Valid package but package not installed
            raise Exception("Packages ",renderer.renderer_req[args.output_type]," missing for renderer ",args.output_type)


    report_generator.makeFullReport(rend, df, args.output_file, args.data_name,
                                   args.src, args.dst, args.weight, args.time)


if __name__ == '__main__':
    main()
