Installation
============

The most direct way to install the package to use it directly is to install it
via pip. For now it can be directly installed from github, and in future it
will be available on directly on PyPI

.. code-block:: bash 

   pip install git+https://github.com/alan-turing-institute/nestpackage


The package can also just be clone directly from our github package, which is
the recommended route if you wish to add additional statistics. 

Requirements
------------

The following packages are needed for NEST. They can be installed either via
pip, or conda or by any alternative package manager (poetry etc). 


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

