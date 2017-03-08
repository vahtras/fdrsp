import os
#
# Finite field strength
#
delta = 0.001
rtol=1e-3
hfweight = 0.5
#
# Top part of script: setup
#

setup = """
import pytest
import os
import shutil
import numpy as np
from findif import *
from mol import inp

def assert_(num,ana):
    atol = 1e-8
    print("Numerical ", num)
    print("Analytical", ana)
    print("Difference ", abs(num-ana))
    print("Target diff", atol + %f*abs(ana))
    assert np.allclose(num, ana, rtol=%f)

def setup():
    global suppdir
    n, e = os.path.splitext(__file__)
    suppdir = n + ".d"
    if os.path.isdir(suppdir):
        #shutil.rmtree(suppdir)
        pass
    else:
        os.mkdir(suppdir)
    os.chdir(suppdir)

def teardown():
    #shutil.rmtree(suppdir)
    pass
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

#
# Bottom part of script: main (to invoke inividual tests)
#

main = """
if __name__ == "__main__":
    import sys
    setup()
    eval("test_findif_%s()"%sys.argv[1])
    teardown()
"""

#
# Process all runtypes and functionals defined in input file
#

def process(template, functionals):
    tmp = os.environ.get('TMPDIR', '/tmp')
    for runtype in template:
        with open(os.path.join(tmp, "test_findif_" + runtype + ".py"), 'w') as runfile:
            runfile.write(setup)
            runfile.write( template[runtype]%('HF', 'HF', 'hf'))
            for f in functionals:
                validfname = f.replace('-', '_').replace('/', '_').replace(' ', '_').replace('*', '').replace('=','_')
                dal=validfname.lower()
                if '*' in f: 
                    wf = 'DFT\\nGGAKey hf=%f %s=%f' % (hfweight, f.replace('*', ''), 1-hfweight)
                else:
                    wf = 'DFT\\n%s'%f
                runfile.write(template[runtype]%(validfname, wf, dal))
            runfile.write(main)

def process_pt(template, functionals):
    tmp = os.environ.get('TMPDIR', '/tmp')
    quoted = ['"%s"' % f for f in functionals]
    for runtype in template:
        with open(os.path.join(tmp, "test_findif_" + runtype + ".py"), 'w') as runfile:
            runfile.write(setup)
            runfile.write(template[runtype] % ", ".join(['"HF"'] + quoted))
            #runfile.write(main)
