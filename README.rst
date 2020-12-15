bids-scan
=========
A quick one-liner tool to extract site metadata from a `BIDS <https://bids.neuroimaging.io/>`_ dataset.
The resulting output can be directly used for a publication, or a website for example.

.. warning::
   We suppose that each patient from the same site (and same modality, task) will have the same parameters.

Input
:::::

A `BIDS <https://bids.neuroimaging.io/>`_ compatible f-mri data directory.

Output
::::::

The sites parameters matrix as a csv table in the `reStructured Text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format.

For example for f-MRI:

.. csv-table:: f-MRI sites parameters
   :header: "Site", "Field Strength (T)", "Voxel size (mm3)", "Matrix size", "Flip Angle", "TE (s)", "TR (s)", "Volumes", "Scan slices order", "Scan time (min)"
   :widths: 30, 5, 5, 5, 5, 5, 5, 5, 30, 5

   "THE_OTTAWA_HOSPITAL_CIVIC", 3, 3.5, 64x64, 70, 0.03, 2.11, 250, "sequential decreasing", 8.79

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
* nibabel 3.2.1

`pybids <https://github.com/bids-standard/pybids>`_ is the python wrapper aroung the bids dataset.
`nibabel <https://github.com/nipy/nibabel>`_ get the imaging parameters (number of volumes, resolution, slice order method and scan time) directly from the `NIfTI <https://nifti.nimh.nih.gov/>`_ file if not correctly gathered.
