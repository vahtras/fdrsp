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
    
def test_rspinp_none():
    calc = RspCalc()
    assert calc.rspinp() == "###"


def test_triplet_label_default():
    zcalc = RspCalc("ZDIPLEN")
    assert zcalc.triplet_label() == "#"

def test_triplet_label_true():
    zcalc = RspCalc("ZDIPLEN", triplet=True)
    assert zcalc.triplet_label() == ".TRPFLG"
    
    
def test_evinp():
    zcalc = RspCalc("ZDIPLEN")
    assert zcalc.evinp() == """\
.PROPAV
ZDIPLEN"""

def test_rspinp_ev():
    zcalc = RspCalc("ZDIPLEN")
    assert zcalc.rspinp() == """\
**RESPONSE
#
.PROPAV
ZDIPLEN"""

def test_rspinp_ev_triplet():
    zcalc = RspCalc("ZDIPLEN", triplet=True)
    assert zcalc.rspinp() == """\
**RESPONSE
.TRPFLG
.PROPAV
ZDIPLEN"""

def test_lrinp():
    calc = RspCalc("XDIPLEN", "YDIPLEN")
    assert calc.lrinp() == """\
*LINEAR
.THCLR
1e-10
.PROPRT
XDIPLEN
.PROPRT
YDIPLEN"""

def test_rsp_lrinp():
    calc = RspCalc("XDIPLEN", "YDIPLEN")
    assert calc.rspinp() == """\
**RESPONSE
#
*LINEAR
.THCLR
1e-10
.PROPRT
XDIPLEN
.PROPRT
YDIPLEN"""

def test_qrinp():
    calc = RspCalc("XDIPLEN", "YDIPLEN", "ZDIPLEN")
    assert calc.qrinp() == """\
*QUADRATIC
.THCLR
1e-10
.APROP
XDIPLEN
.BPROP
YDIPLEN
.CPROP
ZDIPLEN"""

def test_rsp_qrinp():
    calc = RspCalc("XDIPLEN", "YDIPLEN", "ZDIPLEN")
    assert calc.rspinp() == """\
**RESPONSE
#
*QUADRATIC
.THCLR
1e-10
.APROP
XDIPLEN
.BPROP
YDIPLEN
.CPROP
ZDIPLEN"""

def test_qrinp_trip():
    calc = RspCalc("XDIPLEN", "YDIPLEN", "ZDIPLEN", triplet=True)
    assert calc.qrinp() == """\
*QUADRATIC
.THCLR
1e-10
.APROP
XDIPLEN
.BPROP
YDIPLEN
.CPROP
ZDIPLEN
.ISPABC
 1 1 0"""

def test_crinp():
    calc = RspCalc("XDIPLEN", "YDIPLEN", "ZDIPLEN", "ZDIPLEN")
    assert calc.crinp() == """\
*CUBIC
.THCLR
1e-10
.APROP
XDIPLEN
.BPROP
YDIPLEN
.CPROP
ZDIPLEN
.DPROP
ZDIPLEN"""

def test_rsp_crinp():
    calc = RspCalc("XDIPLEN", "YDIPLEN", "ZDIPLEN", "ZDIPLEN")
    assert calc.rspinp() == """\
**RESPONSE
#
*CUBIC
.THCLR
1e-10
.APROP
XDIPLEN
.BPROP
YDIPLEN
.CPROP
ZDIPLEN
.DPROP
ZDIPLEN"""

