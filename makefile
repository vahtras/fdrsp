TESTFILES = $(TMPDIR)/test_findif_ev_closed_singlet.py $(TMPDIR)/test_findif_ev_open_singlet.py $(TMPDIR)/test_findif_lr_closed_singlet.py $(TMPDIR)/test_findif_lr_open_singlet.py $(TMPDIR)/test_findif_lr_open_triplet.py $(TMPDIR)/test_findif_qr_closed_singlet.py $(TMPDIR)/test_findif_qr_closed_triplet.py $(TMPDIR)/test_findif_qr_open_singlet.py $(TMPDIR)/test_findif_qr_open_triplet.py $(TMPDIR)/test_findif_cr_closed_singlet.py
PYCFILES=$(patsubst %.py, %.pyc, $(TESTFILES))
LOGFILES=$(patsubst %.py, %.log, $(TESTFILES))
DIRFILES=$(patsubst %.py, %.d, $(TESTFILES))


test_findif.tgz: test_findif.html $(LOGFILES)
	cp test_findif.html $(TMPDIR)
	cp -r dist $(TMPDIR)
	tar -C $(TMPDIR) -caf $@ .
	

test_findif.html: $(LOGFILES) hf_availfun
	./makehtml.py $(LOGFILES)

.SUFFIXES: .py .log

.py.log:
	python -m pytest  -v $? 2>&1 | tee $@

clean:
	rm  -vf $(TESTFILES)
	rm  -vf $(LOGFILES)
	rm  -vf $(PYCFILES)
	rm  -rvf $(DIRFILES)
 
test:
	python -m pytest test_rspcalc.py test_html.py
debug:
	python -m pytest test_rspcalc.py test_html.py --pdb
