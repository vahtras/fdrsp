import os
from . import TmpDir
#
# Finite field strength
#
delta = 0.001
rtol = 1e-3
hfweight = 0.5
#
# Top part of script: setup
#

setup = """
import pytest
import os
import shutil
import numpy as np
from fdrsp.findif import *
from fdrsp.mol import inp

def assert_(num,ana):
    atol = 1e-8
    print("Numerical ", num)
    print("Analytical", ana)
    print("Difference ", abs(num-ana))
    print("Target diff", atol + %f*abs(ana))
    assert np.allclose(num, ana, rtol=%f)

def setup_module():
    global suppdir
    n, e = os.path.splitext(__file__)
    suppdir = n + ".d"
    if os.path.isdir(suppdir):
        #shutil.rmtree(suppdir)
        pass
    else:
        os.mkdir(suppdir)
    os.chdir(suppdir)
""" % (rtol, rtol)

setup += """
def dft(functional):
    if functional.upper() == 'HF':
        return functional
    elif '*' in functional:
        return 'DFT\\nGGAKey hf=%g %%s=%g' %% functional.strip('*')
    else:
        return 'DFT\\n%%s' %% functional

""" % (hfweight, 1-hfweight)

generic_test = """
def test_findif_generic(run_response):
    e1, e2 = run_response
    assert_(e1, e2)
"""


#
# Process all runtypes and functionals defined in input file
#
def process_pt(template, functionals, **config):
    tmp = config.get('tmp', TmpDir())
    quoted = ['"%s"' % f for f in functionals]
    for runtype in template:
        with open(
            os.path.join(tmp, "test_findif_" + runtype + ".py"), 'w'
                ) as runfile:
            runfile.write(setup)
            runfile.write(template[runtype] % ", ".join(['"HF"'] + quoted))
            runfile.write(generic_test)
