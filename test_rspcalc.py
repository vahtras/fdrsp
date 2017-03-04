import pytest
import mock
from findif import RspCalc
from errors import MolError


def test_z_setup():
    zcalc = RspCalc("ZDIPLEN")
    assert zcalc.parallel
    assert zcalc.wf == 'HF'
    assert zcalc.delta == 0
    assert zcalc.ops == ("ZDIPLEN",)
    assert not zcalc.triplet
    assert zcalc.aux == "#"
    assert zcalc.dal == zcalc.wf
    assert zcalc.mol == None

def test_z_exe_without_mol():
    zcalc = RspCalc("ZDIPLEN")
    with pytest.raises(MolError):
        zcalc.exe()


def test_set_field_none():
    zcalc = RspCalc("ZDIPLEN")
    assert zcalc.finite_field() == "###"

def test_set_field():
    zcalc = RspCalc("ZDIPLEN", field="XDIPLEN")
    assert zcalc.finite_field(0.0005) == "*HAMILTON\n.FIELD\n0.0005\nXDIPLEN"

def test_wavinp():
    zcalc = RspCalc("ZDIPLEN")
    assert zcalc.wavinp() == """\
**WAVE FUNCTION
.HF
*SCF INPUT
.NOQCSCF
.THRESHOLD
1e-11
###"""

def test_wavinp_with_field():
    zcalc = RspCalc("ZDIPLEN", field="YDIPLEN")
    assert zcalc.wavinp(0.001) == """\
**WAVE FUNCTION
.HF
*SCF INPUT
.NOQCSCF
.THRESHOLD
1e-11
*HAMILTON
.FIELD
0.001
YDIPLEN"""
    
    
