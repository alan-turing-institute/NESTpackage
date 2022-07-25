Quickstart
==========

The simplest way to use the package is to use the command line tool directly
with a csv containing the required network data, which this quick start guide
will focus on. 

For users who may wish to interact with the package via python
directly (e.g. to produce reports on graph data as part of a wider pipeline), 
please consult the API guide for the underlying calls, to the integration of
the nest pipeline into a general pipeline. 

Data
-----

The `nest` package assumes that your data is in a standard csv format where
each row represents a single edge with attributes. For example, here is the
first few lines of an example dataset: 

```
Col1,Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,time
9,6,3,6,2,7,2,3,1,0.621414985445744,2000-01-14
5,9,3,10,3,1,10,10,4,0.5998827544069725,2000-02-10
1,0,10,8,1,7,2,2,6,0.48768217626404864,2000-01-20
5,5,9,3,2,8,6,7,4,0.06281386892763785,2000-02-12
1,3,1,8,2,3,3,4,5,0.7001516115392037,2000-01-21
```

Thus, if the source and destination information is stored in `Col1` and `Col2`,
with weight information in `Col10` the first row would represents an edge
between node 9 and node 6 of weight 0.621. 

For reference the full dataset can be found at the following 
`webpage. <https://raw.githubusercontent.com/alan-turing-institute/NESTpackage/main/data/exampleData.csv>`


Running Nest
------------

From a `csv` file running `nest` is as simple as running:

.. code-block:: console

   nest --data_file exampleData.csv 

Running this would then produce a PDF summarising your network using every
statistic in Nest. Note for large graphs this may take a long time. 

This will run the full nest report but it needs to make some assumptions:  

* The data is static (i.e. there is no temporal structure) 
* The data is directed 
* The data is unweighted 
* The source column is the first column  
* The destination column is the second column  
* The output will be saved in a file called "nestOutput"
* The dataset is not named
* The output will be in PDF 

If these defaults are not correct, each of these options can be configured
using `nest` command line options. 


If we would like to save the output in a file called FILENAME, we could like to
name the dataset EXAMPLE we would use the following command: 

.. code-block:: console

   nest --data_file exampleData.csv --output_file FILENAME --data_name EXAMPLE


If instead source column is named "Col2" and the destination column is "Col3"  
then we would run the following: 

.. code-block:: console

   nest --data_file exampleData.csv --src Col2 --dst Col3 

Further, if the source and destination columns are combinations of multiple
columns, we can specify this as a list of columns in either the source or
destination columns. 

.. code-block:: console

   nest --data_file exampleData.csv --src Col1,Col2 --dst Col3,Col4 

If the graph is either temporal or weighted, it is as simple as telling  `nest`
which column has the temporal, or weight information: 

.. code-block:: console

   nest --data_file exampleData.csv --src Col1,Col2 --dst Col3,Col4 --weight Col10 --time time 

By specifying the time column `nest` will then include additional temporal
statistics.  

We can also specify the type of output we want, the current options are PDF 
(either from reportlab or pandoc) or HTML (from pandoc). The default is a
reportlab PDF. 

If you would like to have a html output you can use the command below. 

**However, to run this you need to have the pandoc library and the python
pandoc library installed, which is not installed by default by Nest, and needs
to be installed separately.**


.. code-block:: console

   nest --data_file exampleData.csv --src Col1,Col2 --dst Col3,Col4 --output_type pandocHTML



Command line options 
---------------------

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

