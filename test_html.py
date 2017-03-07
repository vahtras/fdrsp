import pytest
import mock
import pandas as pd
import pandas.util.testing as pdt
import makehtml

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


def test_collect_status_column():
    input_lines = """
test_findif_ev_closed_singlet.test_findif_HF ... ok
test_findif_ev_closed_singlet.test_findif_lda ... ok
----------------------------------------------------------------------
Ran 2 tests in 3.728s

OK
""".strip().split('\n')

    s = pd.Series(
        ['<a href="test_findif_ev_closed_singlet.d/hf.out">ok</a>', 
         '<a href="test_findif_ev_closed_singlet.d/lda.out">ok</a>'],
        index=["HF", "lda"]
    )

    pdt.assert_series_equal(makehtml.collect_status_column(input_lines), s)

#@pytest.mark.skip('hold')
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


@mock.patch('makehtml.open')
def test_collect_status_table(mock_open):

    input_lines1 =  """
test_findif_ev_closed_singlet.test_findif_HF ... ok
test_findif_ev_closed_singlet.test_findif_lda ... ok
----------------------------------------------------------------------
Ran 2 tests in 3.728s

OK
""".strip().split('\n')

    input_lines2 =  """
test_findif_ev_open_singlet.test_findif_HF ... ok
test_findif_ev_open_singlet.test_findif_lda ... ok
----------------------------------------------------------------------
Ran 2 tests in 3.728s

OK
""".strip().split('\n')

    logfiles = ("logfile1", "logfile2")
    mock_open.side_effect = [input_lines1, input_lines2]

    ref_df = pd.DataFrame([
        ['<a href="test_findif_ev_closed_singlet.d/hf.out">ok</a>', 
         '<a href="test_findif_ev_open_singlet.d/hf.out">ok</a>'
        ],
        ['<a href="test_findif_ev_closed_singlet.d/lda.out">ok</a>', 
         '<a href="test_findif_ev_open_singlet.d/lda.out">ok</a>'
        ],
        ],
        index=["HF", "lda"],
        columns=["logfile1", "logfile2"]
    )
    df = makehtml.collect_status_table(*logfiles)

    pdt.assert_frame_equal(df, ref_df)

def test_git_revision():
    lines = ("before", "Git | 7.2", "after")
    assert makehtml.get_git_revision(lines) == "7.2"

def test_get_functional():
    assert makehtml.get_functional("...[LDA]...") == "LDA"
