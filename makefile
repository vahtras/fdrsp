TESTFILES = $(wildcard test_findif_*.py)
PYCFILES=$(patsubst %.py, %.pyc, $(TESTFILES))
LOGFILES=$(patsubst %.py, %.log, $(TESTFILES))
DIRFILES=$(patsubst %.py, %.d, $(TESTFILES))



test_findif.tgz: test_findif.html $(LOGFILES)
	tar cfz $@ test_findif.html $(LOGFILES) $(DIRFILES) dist

test_findif.html: $(LOGFILES) hf_availfun
	./makehtml.py $(LOGFILES)

.SUFFIXES: .py .log

.py.log:
	nosetests -v $? 2>&1 | tee $@

clean:
	rm  -vf $(TESTFILES)
	rm  -vf $(LOGFILES)
	rm  -vf $(PYCFILES)
	rm  -rvf $(DIRFILES)
 
test:
	python -m pytest test_rspcalc.py
debug:
	python -m pytest test_rspcalc.py --pdb
