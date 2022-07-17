Quickstart
==========

The simplest way to use the package is to use the command line tool directly
with a csv containing the required network data, which this quick start guide
will focus on. For users who may wish to interact with the package via python
directly (e.g. to produce reports on graph data as part of a wider pipeline), 
please consult the API guide for the underlying calls. 

Using the package using the command line tool is very simple. After installing
the using pip the `nest` command will be available on the command line can be
called with the following options. 

- **--data_file** Path to the csv file 

  The dataset if assumed to be a csv file where there is one row per edge, and each row consists of a set of columns representing the source and destination, and columns with the time and weight information. 

- **--src** Source Column(s) separated by commas (Default Column 1). If multiple columns are given it will construct the node ID with the combination of the columns
- **--dst** Destination Column(s) separated by commas (Default Column 2). If multiple columns are given it will construct the node ID with the combination of the columns
- **--weight** Weight Column (Default None), if this flag is set to None, the network is assumed to be unweighted (all weights are set at 1).
- **--time** Time Column (Default None), if this flag is set to None, the network is assumed to be static, i.e. all no temporal information.  
- **--output_type** Specify the output type, current options are reportlabPDF (default), pandocPDF and pandocHTML, the pandoc library needs to be installed to use the pandoc options.
- **--output_file** Output file name (no extension needed)
- **--data_name** 'Data set name (used for presentation)

