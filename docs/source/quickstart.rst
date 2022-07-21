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


data_file
   Path to the csv file. The dataset if assumed to  
   be a csv file where there is one row per edge,   
   and each row consists of a set of columns        
   representing the source and destination, and     
   columns with the time and weight information.    

src
   Source Column(s) separated by commas (Default    
   Column 1). If multiple columns are given it will 
   construct the node ID with the combination of the
   columns                                          

dst
   Destination Column(s) separated by commas        
   (Default Column 2). If multiple columns are given
   it will construct the node ID with the           
   combination of the columns                       

weight 
   Weight Column (Default None). If this flag is set
   to None, the network is assumed to be unweighted 
   (all weights are set at 1).                      

time 
   Time Column (Default None) If this flag is set to
   None, the network is assumed to be static,       
   i.e. all no temporal information.                

output_type
   Specify the output type, current options are     
   reportlabPDF (default), pandocPDF and pandocHTML.
   The pandoc library needs to be installed to use  
   the pandoc options.                              

output_file
   Output file name, no extension needed

data_name
   Data set name (Used for presentation)      

Example 
-------

Thus to run nest on a dataset contained in the file data.csv, where the source
column is named "from" and the destination column is named "to" we would run
the following: 

.. code-block:: console

   nest --data_file data.csv --src from --dst to

Running this would then produce a PDF summarising your network using every
statistic in Nest. Note for large graphs this may take a long time, see later
in this section for a way to reduce the number of methods that run. 

If you would like to have a html output, then you can use the following
command:

.. code-block:: console

   nest --data_file data.csv --src from --dst to --output_type pandocHTML

Note to run this you need to have the pandoc library installed, which is not
installed by default by Nest, and needs to be installed separately.


