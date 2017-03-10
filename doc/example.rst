Examples
********

Before running any test, check that ``dalton`` is in your path

Hartree-Fock only
-----------------
The results will be the file `test_findif.html <_static/hf/test_findif.html>`_


::

    $ ./submitall

    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_ev_closed_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_ev_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_ev_closed_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.97 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_ev_open_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_ev_open_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_ev_open_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.67 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_lr_closed_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_lr_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_lr_closed_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.72 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_lr_open_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_lr_open_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_lr_open_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.76 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_lr_open_triplet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_lr_open_triplet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_lr_open_triplet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.75 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_qr_closed_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_qr_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_qr_closed_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.86 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_qr_closed_triplet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_qr_closed_triplet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_qr_closed_triplet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.94 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_qr_open_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_qr_open_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_qr_open_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.86 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_qr_open_triplet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_qr_open_triplet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_qr_open_triplet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 0.85 seconds ===========================
    python -m pytest  -v /tmp/tmpgqMM9I/test_findif_cr_closed_singlet.py 2>&1 | tee /tmp/tmpgqMM9I/test_findif_cr_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpgqMM9I/.cache
    rootdir: /tmp/tmpgqMM9I, inifile: 
    collecting ... collected 1 items

    ../../../../tmp/tmpgqMM9I/test_findif_cr_closed_singlet.py::test_findif_generic[HF] PASSED

    =========================== 1 passed in 1.10 seconds ===========================
    python -m fdrsp.makehtml  /tmp/tmpgqMM9I/test_findif_ev_closed_singlet.log  /tmp/tmpgqMM9I/test_findif_ev_open_singlet.log  /tmp/tmpgqMM9I/test_findif_lr_closed_singlet.log  /tmp/tmpgqMM9I/test_findif_lr_open_singlet.log  /tmp/tmpgqMM9I/test_findif_lr_open_triplet.log  /tmp/tmpgqMM9I/test_findif_qr_closed_singlet.log  /tmp/tmpgqMM9I/test_findif_qr_closed_triplet.log  /tmp/tmpgqMM9I/test_findif_qr_open_singlet.log  /tmp/tmpgqMM9I/test_findif_qr_open_triplet.log  /tmp/tmpgqMM9I/test_findif_cr_closed_singlet.log
    cp test_findif.html /tmp/tmpgqMM9I
    cp -r dist /tmp/tmpgqMM9I
    tar -C /tmp/tmpgqMM9I -caf test_findif.tgz .

For an overview of results open file:///home/olav/dev/fdrsp/test_findif.html in your browser
Results, output and logfiles are saved in compressed archive test_findif.tgz

Hartree-Fock and LDA
--------------------

The results will be the file `test_findif.html <_static/lda/test_findif.html>`_
Here a failing test generates a link to the corresponding output file.

::

    $ ./submitall LDA
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_ev_closed_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_ev_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_ev_closed_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_ev_closed_singlet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 2.75 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_ev_open_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_ev_open_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_ev_open_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_ev_open_singlet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 3.59 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_lr_closed_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_lr_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_lr_closed_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_lr_closed_singlet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 3.40 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_lr_open_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_lr_open_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_lr_open_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_lr_open_singlet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 4.54 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_lr_open_triplet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_lr_open_triplet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_lr_open_triplet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_lr_open_triplet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 4.65 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_qr_closed_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_qr_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_qr_closed_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_qr_closed_singlet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 7.24 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_qr_closed_triplet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_qr_closed_triplet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_qr_closed_triplet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_qr_closed_triplet.py::test_findif_generic[LDA] PASSED

    =========================== 2 passed in 6.22 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_qr_open_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_qr_open_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_qr_open_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_qr_open_singlet.py::test_findif_generic[LDA] PASSED

    ========================== 2 passed in 11.64 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_qr_open_triplet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_qr_open_triplet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_qr_open_triplet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_qr_open_triplet.py::test_findif_generic[LDA] PASSED

    ========================== 2 passed in 11.91 seconds ===========================
    python -m pytest  -v /tmp/tmpPGIiKt/test_findif_cr_closed_singlet.py 2>&1 | tee /tmp/tmpPGIiKt/test_findif_cr_closed_singlet.log
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
    cachedir: ../../../../tmp/tmpPGIiKt/.cache
    rootdir: /tmp/tmpPGIiKt, inifile: 
    collecting ... collected 2 items

    ../../../../tmp/tmpPGIiKt/test_findif_cr_closed_singlet.py::test_findif_generic[HF] PASSED
    ../../../../tmp/tmpPGIiKt/test_findif_cr_closed_singlet.py::test_findif_generic[LDA] PASSED

    ========================== 2 passed in 10.07 seconds ===========================
    python -m fdrsp.makehtml  /tmp/tmpPGIiKt/test_findif_ev_closed_singlet.log  /tmp/tmpPGIiKt/test_findif_ev_open_singlet.log  /tmp/tmpPGIiKt/test_findif_lr_closed_singlet.log  /tmp/tmpPGIiKt/test_findif_lr_open_singlet.log  /tmp/tmpPGIiKt/test_findif_lr_open_triplet.log  /tmp/tmpPGIiKt/test_findif_qr_closed_singlet.log  /tmp/tmpPGIiKt/test_findif_qr_closed_triplet.log  /tmp/tmpPGIiKt/test_findif_qr_open_singlet.log  /tmp/tmpPGIiKt/test_findif_qr_open_triplet.log  /tmp/tmpPGIiKt/test_findif_cr_closed_singlet.log
    cp test_findif.html /tmp/tmpPGIiKt
    cp -r dist /tmp/tmpPGIiKt
    tar -C /tmp/tmpPGIiKt -caf test_findif.tgz .

    For an overview of results open file:///home/olav/dev/fdrsp/test_findif.html in your browser
    Results, output and logfiles are saved in compressed archive test_findif.tgz


