Command Line Tool
=================

As part of our package we include a command line tool in addition to the python interface.

The command for this is `nest`. This command will take a dataset and will then
produce a report summarising your dataset. 

The command line tool takes the following arguments:

============ ==================================
Arguments    Description
============ ==================================
-h, –help    show this help message and exit
–data_file   Csv file path
–src         Source Columns separated by commas
–dst         Dest Columns separated by commas
–weight      Weight Column
–time        Time Column
–output_file Output file
–data_name   Data set name
============ ==================================

Examples
~~~~~~~~

Specify a data file (represented as an edge list)..

.. code:: bash

   nest --data_file exampleData.csv 

Specify columns that make up the source node . The combination of
columns are used the source ID.

.. code:: bash

   nest --src F,G 

Specify columns that make up the destination. The combination of columns
are used the source ID.

.. code:: bash

   nest --dst F,G 

