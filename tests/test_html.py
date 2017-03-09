import pytest
import pandas as pd
import pandas.util.testing as pdt

from . import fdrsp
from fdrsp import makehtml

def  test_head():
    assert makehtml.head('/a/b/c') == '/a/b'

def  test_tail():
    assert makehtml.tail('/a/b/c') == 'c'

def test_root():
    assert makehtml.root('/a/b.c') == '/a/b'

def test_ext():
    assert makehtml.ext('/a/b.c') == '.c'

def test_short():
    assert makehtml.short('/tmp/qwerty/test_findif_calc') == 'calc'

def test_dirs():
    logs = ["/c/a.log", "/c/b.log"]
    assert makehtml.get_dirs(logs) == ["/c/a.d", "/c/b.d"]


def test_collect_status_column_pt():
    input_lines = """
collecting ... collected 2 items

.../test_findif_ev_closed_singlet.py::test_findif_generic[HF] PASSED
.../test_findif_ev_closed_singlet.py::test_findif_generic[LDA] PASSED

=========================== 2 passed in 3.63 seconds ===========================
""".strip().split('\n')

    ref_status = pd.Series(
        ['<a href="test_findif_ev_closed_singlet.d/HF.out">PASSED</a>', 
         '<a href="test_findif_ev_closed_singlet.d/LDA.out">PASSED</a>'],
        index=["HF", "LDA"]
    )

    status = makehtml.collect_status_column_pt(input_lines)
    pdt.assert_series_equal(status, ref_status)


def test_git_revision():
    lines = ("before", "Git | 7.2", "after")
    assert makehtml.get_git_revision(lines) == "7.2"

def test_get_functional_lda():
    assert makehtml.get_functional("...[LDA]...") == "LDA"

def test_get_functional_with_hfx():
    assert makehtml.get_functional("...[LDA*]...") == "LDA*"

def test_get_functional_14():
    assert makehtml.get_functional("...[1/4]...") == "1/4"

def test_canonical():
    assert makehtml.canonical('1/4') == '1_4'
