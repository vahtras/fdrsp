import pytest
import mock
import pandas as pd
import pandas.util.testing as pdt

from . import fdrsp
from fdrsp import makehtml

def  test_tail():
    assert makehtml.tail('/a/b/c') == 'c'

def test_root():
    assert makehtml.root('/a/b.c') == '/a/b'

def test_short():
    assert makehtml.short('/tmp/qwerty/test_findif_calc') == 'calc'

def test_dirs():
    logs = ["/c/a.log", "/c/b.log"]
    assert makehtml.get_dirs(logs) == ["/c/a.d", "/c/b.d"]


@mock.patch('fdrsp.makehtml.files_to_html')
def test_collect_status_column_pt(mock_to_html):
    input_lines = """
collecting ... collected 2 items

.../test_findif_ev_closed_singlet.py::test_findif_generic[HF] PASSED
.../test_findif_ev_closed_singlet.py::test_findif_generic[LDA] PASSED

=========================== 2 passed in 3.63 seconds ===========================
""".strip().split('\n')

    ref_status = pd.Series(
        ['<a href="test_findif_ev_closed_singlet.d/HF.out.html">PASSED</a>', 
         '<a href="test_findif_ev_closed_singlet.d/LDA.out.html">PASSED</a>'],
        index=["HF", "LDA"]
    )

    status = makehtml.collect_status_column_pt(input_lines)
    pdt.assert_series_equal(status, ref_status)
    mock_to_html.assert_has_calls([
        mock.call(
            'test_findif_ev_closed_singlet.d/HF.out',
             'test_findif_ev_closed_singlet.d/HF.out.0',
             'test_findif_ev_closed_singlet.d/HF.out.1'
        ),
        mock.call(
            'test_findif_ev_closed_singlet.d/LDA.out',
            'test_findif_ev_closed_singlet.d/LDA.out.0',
            'test_findif_ev_closed_singlet.d/LDA.out.1'),
    ])


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

@mock.patch('fdrsp.makehtml.open')
def test_file_to_html(mock_open):
    mock_html = mock.MagicMock()
    mock_open().__enter__.return_value = mock_html

    mock_open().read.return_value = "file contents"
    html = makehtml.file_to_html('yo')

    mock_html.write.assert_has_calls([
        mock.call(makehtml.html_head(h2='yo')),
        mock.call("<pre>"),
        mock.call("file contents"),
        mock.call("</pre>"),
        mock.call(makehtml.html_tail()),
        ])

@mock.patch('fdrsp.makehtml.open')
def test_files_to_html(mock_open):
    mock_html = mock.MagicMock()
    mock_open().__enter__.return_value = mock_html

    mock_open().read.side_effect = ["file1 contents", "file2 contents", "file3 contents"]
    html = makehtml.files_to_html('yo1', 'yo2', 'yo3')

    mock_html.write.assert_has_calls([
        mock.call(makehtml.html_head()),
        mock.call("<div class='col-md-4'><h2>yo1</h2><pre>file1 contents</pre></div>"),
        mock.call("<div class='col-md-4'><h2>yo2</h2><pre>file2 contents</pre></div>"),
        mock.call("<div class='col-md-4'><h2>yo3</h2><pre>file3 contents</pre></div>"),
        mock.call(makehtml.html_tail()),
        ])
