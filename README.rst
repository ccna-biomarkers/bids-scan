bids-scan
=========
A quick one-liner tool to extract metadata from a `BIDS <https://bids.neuroimaging.io/>`_ dataset.
The resulting output can be directly used for a publication, or a website for example.

Input
:::::

A `BIDS <https://bids.neuroimaging.io/>`_ compatible f-mri data directory.

Output
::::::

The f-MRI sites parameters matrix as a csv table in the `reStructured Text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format.

For example:

.. csv-table:: MRI sites parameters
   :header: "Site", "Field Strength (T)", "Voxel size (mm3)", "Matrix size", "Flip Angle", "TE (s)", "TR (s)"
   :widths: 30, 10, 10, 10, 10, 10, 10

   "THE_OTTAWA_HOSPITAL_CIVIC", 3, 3, 256x256, 165, 0.091, 3

Usage
:::::

.. code-block:: console
  
  bids_scan.py --data /ccna

Ignore
------

You can append path(s) to ignore with the :code:`--ignore` parameter.

.. code-block:: console
   
  bids_scan.py --data /ccna --ignore /ccna/phenotype --ignore /ccna/sub-XXX0000/

Modality
--------

Select which modality you are interrested in with :code:`--modality`.

.. code-block:: console
   
  bids_scan.py --data /ccna --ignore /ccna/phenotype --modality func

Requirements
------------

* pybids 0.12.3

`pybids <https://github.com/bids-standard/pybids>`_ is the python wrapper aroung the bids dataset.
