Nest
====


The NEtwork Statistic (**NEST**) generation package is designed to give a quick
and easy way to produce in depth initial exploratory analysis of a network
dataset.


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

The outputs are designed to allow a reseacher/data scientist to quickly
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



Indices and tables
==================

* :ref:`modindex`
* :ref:`search`

Quick links
-----------

.. toctree::
    :maxdepth: 1

    installation
    quickstart
    commandline
    technicaldetails 
    extendingnest
    contributors
    api


.. automodule:: nest 
          :members:

