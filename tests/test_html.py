import mock
import tempfile

import pandas as pd
import pandas.util.testing as pdt

import fdrsp.makehtml as fm


def test_tail():
    assert fm.tail('/a/b/c') == 'c'


def test_root():
    assert fm.root('/a/b.c') == '/a/b'


def test_short():
    assert fm.short('/tmp/qwerty/test_findif_calc') == 'calc'


def test_dirs():
    logs = ["/c/a.log", "/c/b.log"]
    assert fm.get_dirs(logs) == ["/c/a.d", "/c/b.d"]


@mock.patch('fdrsp.makehtml.files_to_html')
def test_collect_status_column_pt(mock_to_html):
    status = {".": "PASSED", "F": "FAILED", "E": "ERROR"}
    log_lines = """<?xml version="1.0" encoding="utf-8"?>
    <testsuites>
        <testsuite errors="0" failures="0" hostname="work" name="pytest" skipped="0" tests="2" time="1.403" timestamp="2019-11-14T10:25:36.528243">
            <testcase classname="dev.py.fdrsp.sample_tests.test_findif_ev_closed_singlet" file="dev/py/fdrsp/sample_tests/test_findif_ev_closed_singlet.py" line="9" name="test_run_response[HF]" time="0.440">
                <system-out>Dalton called OK
                    Dalton called OK
                    Dalton called OK
                    Numerical  -1.0370241299995087
                    Analytical -1.03702475
                    Difference  6.20000491391437e-07
                    Target diff 0.00103703475
                </system-out>
            </testcase>
            <testcase classname="dev.py.fdrsp.sample_tests.test_findif_ev_closed_singlet" file="dev/py/fdrsp/sample_tests/test_findif_ev_closed_singlet.py" line="9" name="test_run_response[slater]" time="0.954">
                <system-out>Dalton called OK
                    Dalton called OK
                    Dalton called OK
                    Numerical  -0.9706091749990264
                    Analytical -0.97061019
                    Difference  1.0150009736031862e-06
                    Target diff 0.0009706201900000001
                </system-out>
            </testcase>
            <testcase classname="dev.py.fdrsp.sample_tests.test_findif_ev_closed_singlet" file="dev/py/fdrsp/sample_tests/test_findif_ev_closed_singlet.py" line="9" name="test_run_response[b3lyp]" time="0.954">
                <failure message="AssertionError">
                </failure>
                <system-out>Dalton called OK
                    Dalton called OK
                    Dalton called OK
                    Numerical  -0.9706091749990264
                    Analytical -0.97061019
                    Difference  1.0150009736031862e-06
                    Target diff 0.0009706201900000001
                </system-out>
            </testcase>
        </testsuite>
    </testsuites>
"""
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(log_lines)
    status = fm.collect_status_column_pt(f.name, tmp='...')

    ref_status = pd.Series(
            ['<a href="test_findif_ev_closed_singlet.d/HF.out.html" style="color: green;">PASSED</a>',
         '<a href="test_findif_ev_closed_singlet.d/slater.out.html" style="color: green;">PASSED</a>',
         '<a href="test_findif_ev_closed_singlet.d/b3lyp.out.html" style="color: red;">FAILED</a>'
         ],
        index=["HF", "slater", "b3lyp"]
    )

    pdt.assert_series_equal(status, ref_status)
    mock_to_html.assert_has_calls([
        mock.call(
            '.../test_findif_ev_closed_singlet.d/HF.out',
            '.../test_findif_ev_closed_singlet.d/HF.out.0',
            '.../test_findif_ev_closed_singlet.d/HF.out.1'
        ),
        mock.call(
            '.../test_findif_ev_closed_singlet.d/slater.out',
            '.../test_findif_ev_closed_singlet.d/slater.out.0',
            '.../test_findif_ev_closed_singlet.d/slater.out.1'),
    ])


def test_git_revision():
    lines = ("before", "Git | 7.2", "after")
    assert fm.get_git_revision(lines) == "7.2"


def test_get_functional_lda():
    assert fm.get_functional("...[LDA]...") == "LDA"


def test_get_functional_with_hfx():
    assert fm.get_functional("...[LDA*]...") == "LDA*"


def test_get_functional_14():
    assert fm.get_functional("...[1/4]...") == "1/4"


def test_canonical():
    assert fm.canonical('1/4') == '1_4'


@mock.patch('fdrsp.makehtml.open')
def test_file_to_html(mock_open):
    mock_html = mock.MagicMock()
    mock_open().__enter__.return_value = mock_html

    mock_open().read.return_value = "file contents"
    fm.file_to_html('yo')

    mock_html.write.assert_has_calls([
        mock.call(fm.html_head(h2='yo')),
        mock.call("<pre>"),
        mock.call("file contents"),
        mock.call("</pre>"),
        mock.call(fm.html_tail()),
        ])


@mock.patch('fdrsp.makehtml.open')
def test_files_to_html(mock_open):
    mock_html = mock.MagicMock()
    mock_open().__enter__.return_value = mock_html

    mock_open().read.side_effect = [
        "file1 contents", "file2 contents", "file3 contents"
        ]
    fm.files_to_html('yo1', 'yo2', 'yo3')

    mock_html.write.assert_has_calls([
        mock.call(fm.html_head(container="-fluid")),
        mock.call(
            "<div class='col-md-4'><h2>yo1</h2><pre>file1 contents</pre></div>"
        ),
        mock.call(
            "<div class='col-md-4'><h2>yo2</h2><pre>file2 contents</pre></div>"
            ),
        mock.call(
            "<div class='col-md-4'><h2>yo3</h2><pre>file3 contents</pre></div>"
            ),
        mock.call(fm.html_tail()),
        ])
