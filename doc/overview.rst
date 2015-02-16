Overview
********

This suite of tests does finite-difference tests of DFT response functions calculated by Dalton.  The following files are given::

    submitall
    gen_findif_all.py
    common_findif.py
    mol.py
    findif.py
    makefile
    makehtml.py


The user interface is ``submitall``::

    submitall <functional_name|file_name>

A bash script witch takes a functional name or file with list of functionals
in addition to given functionals a reference HF calculation will be done at all levels
::

    gen_findif_all.py

contains templates for test cases to be executed with ``nosetests``.
Test files are generate by looping over all functional names provided in input
::

    common_findif

contains data commot to all tests and Used by ``gen_findif_all.py``
::

    mol.py

A reference molecule used for all calculations
::

    makefile
    
performs all tests providing a rule for getting a logfile depening on a file with unit tests

::

    findif.py
defines classes for performing response calculations 

::

    makehtml.py 

Collects resulting log files and presents results in a html format 

::

