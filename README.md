# NEST

The NEtwork STatistic (**NEST**) package is designed to give a quick
and easy way to produce in depth initial exploratory analysis of a network
dataset. Full details can be found in the [documentation](https://network-statistic-nest-package.readthedocs.io/en/latest/).


This framework where given an input graph, of any type, 

- directed or undirected, 
- temporal or static,
- with (or without) node attributes 
- with (or without) edge attributes 

node and/or edge attributes, temporal or {static}, and will produce an
exhaustive range of statistics summerising this graph, in a nicely presented
document in numerous formats, namely:  

- Pdf
- Csv
- Html
- Others to follow

The outputs are designed to allow a researcher/data scientist to quickly
evaluate a dataset, or to share crucial statistics of a dataset with
others.

The statistics in question cover many different areas of network science,
leveraging several python based network science libraries, with a strong
emphasis on the excellent ``networkx`` library. They include:

- Basic summary statistics (number of nodes etc)
- Centrality Measures
- Community structure
- Path based measures
- Spectral measures
- Motif measures
- Time series measures

Further, we strongly encourage others to contribute either your own measures to
our library, or indeed any other additions to the library that may be helpful
to others.

## Installation


The most direct way to install the package to use it directly is to install it
via pip. For now it can be directly installed from github, and in future it
will be available on directly on PyPI

```{bash}
   pip install git+https://github.com/alan-turing-institute/nestpackage
```

The package can also just be clone directly from our github package, which is
the recommended route if you wish to add additional statistics. 

### Requirements

Required:
  - matplotlib
  - networkx
  - numpy
  - pandas
  - scipy
  - seaborn
  - scikit-learn

The package also requires at least one of the following:
  - pandoc
  - reportlab


Finally, the following packages are optional and are needed for some statistics:
  - motifcluster
  - python-louvain

 
## Usage

The package can be used both directly from python or alternatively via a command line tool.

The command line tool has the following options:

Optons:

| Arguments     | Description                        |
|---------------|------------------------------------|
| -h, --help    | show this help message and exit    |
| --data_file   | Csv file path                      |
| --src         | Source Columns separated by commas |
| --dst         | Dest Columns separated by commas   |
| --directed    | Data is directed (Default)         |
| --no-directed | Data is undirected (Not Default)   |
| --weight      | Weight Column                      |
| --time        | Time Column                        |
| --output_file | Output file                        |
| --data_name   | Data set name                      |

### Examples
 
Specify a data file (represented as an edge list).. 
```bash
nest --data_file exampleData.csv 
```

Specify columns that make up the source node . The combination of columns are used the source ID. 
```bash
nest --src F,G 
```

Specify columns that make up the destination. The combination of columns are used the source ID. 
```bash
nest --dst F,G 
```
  
