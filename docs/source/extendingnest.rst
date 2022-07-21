Extending Nest
=============

We strongly support others taking and extending NEST.  

Adding a new statistic
----------------------

The simplest way to extend Nest is to the add a new statistic. For full details
of the technical details of adding a statistic please see the technical
documentation.

Adding a new scalar statistic as simple as adding the following code to any one
of the statistics modules in `nest/graphstatistics`. 

.. code-block:: python

   class myNewStatistic(baseStatClass):
      def __init__(self, G, optionsDict):
         self.data = computeMyNewStatistic(G)

Just adding this will make Nest compute your new statistic and include it in
all of the reports as an output 


Adding a new statistic module
-----------------------------

