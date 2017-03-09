"""Pytest style tests for findif module"""

import pytest
import mock

from . import fdrsp
from fdrsp.findif import RspCalc, last_float
from fdrsp.errors import MolError


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

def test_dalinp_ev():
    zcalc = RspCalc("YDIPLEN")
    assert zcalc.dalinp() == """\
**DALTON INPUT
.RUN RESPONSE
.DIRECT
**WAVE FUNCTION
.HF
*SCF INPUT
.NOQCSCF
.THRESHOLD
1e-11
###
**RESPONSE
#
.PROPAV
YDIPLEN
**END OF DALTON
"""

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


def test_dal_under():
    assert RspCalc(wf='1/4')._dal_ == '1_4'
    assert RspCalc(wf='1 4')._dal_ == '1_4'

@mock.patch('fdrsp.findif.open')
@mock.patch('fdrsp.findif.subprocess.call')
def test_call(mock_call, mock_open):
    calc = RspCalc(wf='yo', mol='yo')

    mock_call.return_value = 0
    mock_file = mock.MagicMock()
    mock_open().__enter__.return_value = mock_file

    calc.run()

    mock_call.assert_called_once_with(
        'dalton -N 8 -d -t /tmp/ExpVal_yo yo',
        stdout=mock_file, stderr=mock_file, shell=True)


@mock.patch('fdrsp.findif.open')
def test_read_energy(mock_open):

    output_line = "Final energy: 3.14"
    mock_open.return_value = mock_loop(output_line)

    calc = RspCalc()
    assert calc.get_output() ==  3.14

def mock_loop(output_line):

    mock_file = mock.MagicMock(name='file')
    mock_iter= mock.MagicMock(name='iter')
    mock_iterable= mock.MagicMock(name='iterable')
    mock_next = mock.MagicMock(name='next')

    mock_file.__iter__ = mock_iter
    mock_iter.return_value = mock_iterable
    mock_iterable.__next__ = mock_next
    mock_next.return_value = output_line

    return mock_file


@mock.patch('fdrsp.findif.open')
def test_read_z(mock_open):

    output_line = "YDIPLEN  total        :    -1.03702475"
    mock_open.return_value = mock_loop(output_line)

    calc = RspCalc('YDIPLEN')
    assert calc.get_output() ==  -1.03702475

@mock.patch('fdrsp.findif.open')
def test_read_yz(mock_open):

    output_line = "@ -<< XXQUADRU ; YDIPLEN  >> =  4.395689062431D-01"
    mock_open.return_value = mock_loop(output_line)

    calc = RspCalc('XXQUADRU', 'YDIPLEN')
    assert calc.get_output() == -4.395689062431e-01

@mock.patch('fdrsp.findif.open')
def test_read_xyz(mock_open):

    output_line = "@ omega B, omega C, QR value :     0.00000000     0.00000000 3.68627919"
    mock_open.return_value = mock_loop(output_line)

    calc = RspCalc('XDIPLEN', 'YDIPLEN', 'ZDIPLEN')
    assert calc.get_output() ==  3.68627919

@mock.patch('fdrsp.findif.open')
def test_read_xyz(mock_open):

    output_line = "@ << A; B, C, D >>  =         -30.99202444"
    mock_open.return_value = mock_loop(output_line)

    calc = RspCalc('XDIPLEN', 'YDIPLEN', 'ZDIPLEN', 'WDIPLEN')
    assert calc.get_output() ==  -30.99202444

def test_line_float():
    assert last_float('X = 1.4D0') == 1.4
    assert last_float('Y : 1.2e0') == 1.2
