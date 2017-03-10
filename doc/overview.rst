Overview
********

This suite of tests does finite-difference tests of DFT response functions calculated by Dalton.  The following files are given::

    submitall
    makefile
    fdrsp/
        gen_findif_all.py
        common_findif.py
        mol.py
        findif.py
        makehtml.py


The user interface is ``submitall``::

    submitall <functional_name|file_name>

A bash script witch takes a functional name or file with list of functionals
in addition to given functionals a reference HF calculation will be done at all levels
::

    makefile
    
performs all tests using a rule for `.py -> .log` files
::

    fdrsp/gen_findif_all.py

contains templates for test cases to be executed with ``pytest``.
Test files are generate by looping over all functional names provided in input
::

    fdrsp/common_findif

contains data common to all tests and Used by ``gen_findif_all.py``
::

    fdrsp/mol.py

A reference molecule used for all calculations
::

    fdrsp/findif.py
defines classes for performing response calculations 

::

    fdrsp/makehtml.py 

Collects resulting log files and presents results in a html format 

::

