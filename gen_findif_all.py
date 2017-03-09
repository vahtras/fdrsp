#!/usr/bin/env python
"""Generate a set of test scipts to pass through nosetests

Tests finite field tests of expectation values

Usage:
./gen_findif_cr.py A B C X file_of_functionals

Checks d<<A; B, C>>/dx(X) = <<A; B, C, D>>
"""

import sys
from common_findif import delta, process_pt

file_of_functionals = sys.argv.pop()
A, B, C, X = sys.argv[1:]
targs = ("%s", "%s", "%s", A, B, C, X, delta, A, B, C, X)


#
# Template for functional test calling findif module 
#

template = {}


template["ev_closed_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    escf = FinDif(RspCalc(wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    ev = RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    assert_(escf, ev)
""" % ("%s", "%s", "%s", X, delta, X)

template["ev_open_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    escf = FinDif(RspCalc(wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    ev = RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o+"]).exe()
    assert_(escf, ev)
""" % ("%s", "%s", "%s", X, delta, X)

template["lr_closed_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    ev = FinDif(RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    lr = RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    assert_(ev, lr)
""" % ("%s", "%s", "%s", A, X, delta, A, X)

template["lr_open_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    ev = FinDif(RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    lr = RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o+"]).exe()
    assert_(ev, lr)
""" % ("%s", "%s", "%s", A, X, delta, A, X)

template["lr_open_triplet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    ev = FinDif(RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o+"], triplet=True, field='%s', delta=%f)).first() 
    lr = RspCalc('%s 1', '%s', wf=wf, dal=dal, mol=inp["h2o+"], triplet=False).exe()
    assert_(ev, lr)
""" % ("%s", "%s", "%s", A, X, delta, A, X)

template["qr_closed_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    lr = FinDif(RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    assert_(lr, qr)
""" % ("%s", "%s", "%s", A, B, X, delta, A, B, X)

template["qr_closed_triplet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    lr = FinDif(RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], triplet=True, field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], triplet=True, aux=".ISPABC\\n 1 1 0").exe()
    assert_(lr, qr)
""" % ("%s", "%s", "%s", A, B, X, delta, A, B, X)

template["qr_open_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    lr = FinDif(RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o+"], parallel=False).exe()
    assert_(lr, qr)
""" % ("%s", "%s", "%s", A, B, X, delta, A, B, X)

template["qr_open_triplet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    lr = FinDif(RspCalc('%s', '%s 1', wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s 1', '%s', wf=wf, dal=dal, mol=inp["h2o+"], parallel=False).exe()
    assert_(lr, qr)
""" % ("%s", "%s", "%s", A, B, X, delta, A, B, X)

template["cr_closed_singlet"] = """
def test_findif_%s():
    wf='%s'
    dal='%s'
    qr = FinDif(RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    cr = RspCalc('%s', '%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    assert_(qr, cr)
""" % ("%s", "%s", "%s", A, B, C, X, delta, A, B, C, X)

templates_pt = {
"ev_closed_singlet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    escf = FinDif(RspCalc(wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    ev = RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    return (escf, ev)
""" % ("%s", X, delta, X),
#
"ev_open_singlet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    escf = FinDif(RspCalc(wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    ev = RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o+"]).exe()
    return (escf, ev)
""" % ("%s", X, delta, X),
#
"lr_closed_singlet":  """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    ev = FinDif(RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    lr = RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    return (ev, lr)
""" % ("%s", A, X, delta, A, X),
#
"lr_open_singlet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    ev = FinDif(RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    lr = RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o+"]).exe()
    return (ev, lr)
""" % ("%s", A, X, delta, A, X),
#
"lr_open_triplet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    ev = FinDif(RspCalc('%s', wf=wf, dal=dal, mol=inp["h2o+"], triplet=True, field='%s', delta=%f)).first() 
    lr = RspCalc('%s 1', '%s', wf=wf, dal=dal, mol=inp["h2o+"], triplet=False).exe()
    return (ev, lr)
""" % ("%s", A, X, delta, A, X),
#
"qr_closed_singlet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    lr = FinDif(RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    return (lr, qr)
""" % ("%s", A, B, X, delta, A, B, X),
#
"qr_closed_triplet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    lr = FinDif(RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], triplet=True, field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], triplet=True, aux=".ISPABC\\n 1 1 0").exe()
    return (lr, qr)
""" % ("%s", A, B, X, delta, A, B, X),
#
"qr_open_singlet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    lr = FinDif(RspCalc('%s', '%s', wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o+"], parallel=False).exe()
    return (lr, qr)
""" % ("%s", A, B, X, delta, A, B, X),
#
"qr_open_triplet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    lr = FinDif(RspCalc('%s', '%s 1', wf=wf, dal=dal, mol=inp["h2o+"], field='%s', delta=%f)).first() 
    qr = RspCalc('%s', '%s 1', '%s', wf=wf, dal=dal, mol=inp["h2o+"], parallel=False).exe()
    return (lr, qr)
""" % ("%s", A, B, X, delta, A, B, X),
#
"cr_closed_singlet": """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    qr = FinDif(RspCalc('%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"], field='%s', delta=%f)).first() 
    cr = RspCalc('%s', '%s', '%s', '%s', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    return (qr, cr)
""" % ("%s", A, B, C, X, delta, A, B, C, X)
}

functionals = [ line.strip() for line in open(file_of_functionals) ] 

#
# Process all runtypes and functionals defined in input file
#


process_pt(templates_pt, functionals)
