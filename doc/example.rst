Examples
********

Before running any test, chech that `dalton` is in your path

Hartree-Fock only
-----------------
The results will be the file test_findif.html_

.. _test_findif.html: _static/hf/test_findif.html

::

    $ ./submitall
    nosetests -v test_findif_ev_closed_singlet.py 2>&1 | tee test_findif_ev_closed_singlet.log
    test_findif_ev_closed_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 4.324s

    OK
    nosetests -v test_findif_ev_open_singlet.py 2>&1 | tee test_findif_ev_open_singlet.log
    test_findif_ev_open_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 4.601s

    OK
    nosetests -v test_findif_lr_closed_singlet.py 2>&1 | tee test_findif_lr_closed_singlet.log
    test_findif_lr_closed_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 5.798s

    OK
    nosetests -v test_findif_lr_open_singlet.py 2>&1 | tee test_findif_lr_open_singlet.log
    test_findif_lr_open_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 5.680s

    OK
    nosetests -v test_findif_lr_open_triplet.py 2>&1 | tee test_findif_lr_open_triplet.log
    test_findif_lr_open_triplet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 5.764s

    OK
    nosetests -v test_findif_qr_closed_singlet.py 2>&1 | tee test_findif_qr_closed_singlet.log
    test_findif_qr_closed_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 4.638s

    OK
    nosetests -v test_findif_qr_closed_triplet.py 2>&1 | tee test_findif_qr_closed_triplet.log
    test_findif_qr_closed_triplet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 4.620s

    OK
    nosetests -v test_findif_qr_open_singlet.py 2>&1 | tee test_findif_qr_open_singlet.log
    test_findif_qr_open_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 7.031s

    OK
    nosetests -v test_findif_qr_open_triplet.py 2>&1 | tee test_findif_qr_open_triplet.log
    test_findif_qr_open_triplet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 2.554s

    OK
    nosetests -v test_findif_cr_closed_singlet.py 2>&1 | tee test_findif_cr_closed_singlet.log
    test_findif_cr_closed_singlet.test_findif_HF ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 9.719s

    OK
    ./makehtml.py test_findif_ev_closed_singlet.log test_findif_ev_open_singlet.log test_findif_lr_closed_singlet.log test_findif_lr_open_singlet.log test_findif_lr_open_triplet.log test_findif_qr_closed_singlet.log test_findif_qr_closed_triplet.log test_findif_qr_open_singlet.log test_findif_qr_open_triplet.log test_findif_cr_closed_singlet.log
    tar cfz test_findif.tgz test_findif.html test_findif_ev_closed_singlet.log test_findif_ev_open_singlet.log test_findif_lr_closed_singlet.log test_findif_lr_open_singlet.log test_findif_lr_open_triplet.log test_findif_qr_closed_singlet.log test_findif_qr_closed_triplet.log test_findif_qr_open_singlet.log test_findif_qr_open_triplet.log test_findif_cr_closed_singlet.log test_findif_ev_closed_singlet.d test_findif_ev_open_singlet.d test_findif_lr_closed_singlet.d test_findif_lr_open_singlet.d test_findif_lr_open_triplet.d test_findif_qr_closed_singlet.d test_findif_qr_closed_triplet.d test_findif_qr_open_singlet.d test_findif_qr_open_triplet.d test_findif_cr_closed_singlet.d

    For an overview of results open test_findif.html in your browser



