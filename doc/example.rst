Examples
********

Before running any test, check that ``dalton`` is in your path

Hartree-Fock only
-----------------
The results will be the file `test_findif.html <_static/hf/test_findif.html>`_


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

    For an overview of results open file:///tmp/fdrsp/test_findif.html in your browser
    Results, output and logfiles are saved in compressed archive test_findif.tgz

Hartree-Fock and LDA
--------------------

The results will be the file `test_findif.html <_static/lda/test_findif.html>`_
Here a failing test generates a link to the corresponding output file.

::

    ./submitall LDA
    nosetests -v test_findif_ev_closed_singlet.py 2>&1 | tee test_findif_ev_closed_singlet.log
    test_findif_ev_closed_singlet.test_findif_HF ... ok
    test_findif_ev_closed_singlet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 14.239s

    OK
    nosetests -v test_findif_ev_open_singlet.py 2>&1 | tee test_findif_ev_open_singlet.log
    test_findif_ev_open_singlet.test_findif_HF ... ok
    test_findif_ev_open_singlet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 26.278s

    OK
    nosetests -v test_findif_lr_closed_singlet.py 2>&1 | tee test_findif_lr_closed_singlet.log
    test_findif_lr_closed_singlet.test_findif_HF ... ok
    test_findif_lr_closed_singlet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 15.838s

    OK
    nosetests -v test_findif_lr_open_singlet.py 2>&1 | tee test_findif_lr_open_singlet.log
    test_findif_lr_open_singlet.test_findif_HF ... ok
    test_findif_lr_open_singlet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 19.845s

    OK
    nosetests -v test_findif_lr_open_triplet.py 2>&1 | tee test_findif_lr_open_triplet.log
    test_findif_lr_open_triplet.test_findif_HF ... ok
    test_findif_lr_open_triplet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 19.687s

    OK
    nosetests -v test_findif_qr_closed_singlet.py 2>&1 | tee test_findif_qr_closed_singlet.log
    test_findif_qr_closed_singlet.test_findif_HF ... ok
    test_findif_qr_closed_singlet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 20.313s

    OK
    nosetests -v test_findif_qr_closed_triplet.py 2>&1 | tee test_findif_qr_closed_triplet.log
    test_findif_qr_closed_triplet.test_findif_HF ... ok
    test_findif_qr_closed_triplet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 21.235s

    OK
    nosetests -v test_findif_qr_open_singlet.py 2>&1 | tee test_findif_qr_open_singlet.log
    test_findif_qr_open_singlet.test_findif_HF ... ok
    test_findif_qr_open_singlet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 43.218s

    OK
    nosetests -v test_findif_qr_open_triplet.py 2>&1 | tee test_findif_qr_open_triplet.log
    test_findif_qr_open_triplet.test_findif_HF ... ok
    test_findif_qr_open_triplet.test_findif_LDA ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 37.765s

    OK
    nosetests -v test_findif_cr_closed_singlet.py 2>&1 | tee test_findif_cr_closed_singlet.log
    test_findif_cr_closed_singlet.test_findif_HF ... ok
    test_findif_cr_closed_singlet.test_findif_LDA ... ERROR

    ======================================================================
    ERROR: test_findif_cr_closed_singlet.test_findif_LDA
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/usr/lib/python2.7/dist-packages/nose/case.py", line 197, in runTest
        self.test(*self.arg)
      File "/tmp/fdrsp/test_findif_cr_closed_singlet.py", line 41, in test_findif_LDA
        cr = RspCalc('XXQUADRU', 'YYQUADRU', 'ZZQUADRU', 'YDIPLEN', wf=wf, dal=dal, mol=inp["h2o"]).exe()
      File "/tmp/fdrsp/findif.py", line 200, in exe
        raise ValueError
    ValueError: 
    -------------------- >> begin captured stdout << ---------------------
    Dalton called OK
    Dalton called OK
    Dalton called OK

    --------------------- >> end captured stdout << ----------------------

    ----------------------------------------------------------------------
    Ran 2 tests in 31.149s

    FAILED (errors=1)
    ./makehtml.py test_findif_ev_closed_singlet.log test_findif_ev_open_singlet.log test_findif_lr_closed_singlet.log test_findif_lr_open_singlet.log test_findif_lr_open_triplet.log test_findif_qr_closed_singlet.log test_findif_qr_closed_triplet.log test_findif_qr_open_singlet.log test_findif_qr_open_triplet.log test_findif_cr_closed_singlet.log
    tar cfz test_findif.tgz test_findif.html test_findif_ev_closed_singlet.log test_findif_ev_open_singlet.log test_findif_lr_closed_singlet.log test_findif_lr_open_singlet.log test_findif_lr_open_triplet.log test_findif_qr_closed_singlet.log test_findif_qr_closed_triplet.log test_findif_qr_open_singlet.log test_findif_qr_open_triplet.log test_findif_cr_closed_singlet.log test_findif_ev_closed_singlet.d test_findif_ev_open_singlet.d test_findif_lr_closed_singlet.d test_findif_lr_open_singlet.d test_findif_lr_open_triplet.d test_findif_qr_closed_singlet.d test_findif_qr_closed_triplet.d test_findif_qr_open_singlet.d test_findif_qr_open_triplet.d test_findif_cr_closed_singlet.d dist

    For an overview of results open file:///tmp/fdrsp/test_findif.html in your browser
    Results, output and logfiles are saved in compressed archive test_findif.tgz

