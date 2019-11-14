import os
import pytest
from fdrsp.findif import FinDif, RspCalc
from fdrsp.mol import inp

from . import assert_, dft

tested_functionals = ["HF"] + open("tested_functionals").read().split()


@pytest.fixture
def suppdir():
    suppdir = os.path.splitext(__file__)[0] + '.d'
    if not os.path.isdir(suppdir):
        os.mkdir(suppdir)
    os.chdir(suppdir)


@pytest.mark.parametrize("functional", tested_functionals)
def test_run_response(functional, suppdir):
    wf = dft(functional)
    dal = functional
    lr = FinDif(
        RspCalc(
            "XXQUADRU",
            "YYQUADRU",
            wf=wf,
            dal=dal,
            mol=inp["h2o+"],
            field="YDIPLEN",
            delta=0.001000,
        )
    ).first()
    qr = RspCalc(
        "XXQUADRU",
        "YYQUADRU",
        "YDIPLEN",
        wf=wf,
        dal=dal,
        mol=inp["h2o+"],
        parallel=False,
    ).exe()
    assert_(lr, qr)
