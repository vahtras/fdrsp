## Overview

This suite of tests does finite difference test of DFT response functions calculated by Dalton
The following files are given::

    submitall
    gen_findif_all.py
    common_findif.py
    mol.py
    findif.py
    makefile
    makehtml.py

### The user interface is `submitall`

A bash script which takes a functional name or file with list of functionals

    submitall <functional_name|file_name>

In addition to given functionals a reference HF calculation will be done at all levels

### Python script `gen_findif_all.py`

contains templates for test cases to be executed with `nosetests`.
Test files are generate by looping over all functional names provided in input


### `common_findif`

Contains data common to all tests and Used by `gen_findif_all.py`

### `mol.py`

A reference molecule used for all calculations


### `makefile`
    
Performs all tests providing a rule for getting a logfile depening on a file with unit tests

### `findif.py`

Defines classes for performing response calculations 

### `makehtml.py`

Collects resulting log files and presents results in a html format 


