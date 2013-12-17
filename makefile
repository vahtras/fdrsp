LOGFILES = test_findif_ev_closed_singlet.log test_findif_ev_open_singlet.log test_findif_lr_closed_singlet.log test_findif_lr_open_singlet.log test_findif_lr_open_triplet.log test_findif_qr_closed_singlet.log test_findif_qr_closed_triplet.log test_findif_qr_open_singlet.log test_findif_qr_open_triplet.log test_findif_cr_closed_singlet.log
DIRFILES = test_findif_ev_closed_singlet.d test_findif_ev_open_singlet.d test_findif_lr_closed_singlet.d test_findif_lr_open_singlet.d test_findif_lr_open_triplet.d test_findif_qr_closed_singlet.d test_findif_qr_closed_triplet.d test_findif_qr_open_singlet.d test_findif_qr_open_triplet.d test_findif_cr_closed_singlet.d

TESTFILES = test_findif_ev_open_singlet.py test_findif_ev_closed_singlet.py test_findif_lr_closed_singlet.py test_findif_lr_open_singlet.py test_findif_lr_open_triplet.py test_findif_qr_closed_singlet.py test_findif_qr_closed_triplet.py test_findif_qr_open_singlet.py test_findif_qr_open_triplet.py test_findif_cr_closed_singlet.py


test_findif.tgz: test_findif.html $(LOGFILES)
	tar cfz $@ test_findif.html $(LOGFILES) $(DIRFILES)

test_findif.html: $(LOGFILES) hf_availfun
	./makehtml.py $(LOGFILES)

.SUFFIXES: .py .log

.py.log:
	nosetests -v $? 2>&1 | tee $@
