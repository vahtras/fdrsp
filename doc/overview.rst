Overview
********

This suite of tests does finite difference test of DFT response functions calculated by Dalton
The following files are given::

    common_findif.py
    doc
    findif.py
    genall
    gen_findif_all.py
    makefile
    makehtml.py
    mol.py
    README
    submitall


The user interface is ``submitall``::

    submitall <functional_name|file_name>

A bash script witch takes a functional name or file with list of functionals
in addition to given functionals a reference HF calculation will be done at all levels
::
    genall
    



