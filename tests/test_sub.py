import run
import mock
import sys
import pytest


@pytest.mark.skip('wait')
@mock.patch('run.open')
def test_setup_open(mock_open):
    sys.argv[1:] = []

    run.main()

    mock_open.assert_has_calls([mock.call('hf_availfun', 'w')])

@pytest.mark.skip('wait')
@mock.patch('run.open')
def test_setup_noargs(mock_open):
    sys.argv[1:] = []
    mock_file = mock.MagicMock()
    mock_open().__enter__.return_value = mock_file

    run.main()

    mock_file.write.assert_has_calls([mock.call('HF')])

@pytest.mark.skip('wait')
@mock.patch('run.open')
def test_setup_one_arg(mock_open):
    sys.argv[1:] = ['LDA']
    mock_file = mock.MagicMock()
    mock_open().__enter__.return_value = mock_file

    run.main()

    mock_file.write.assert_has_calls([mock.call('HF\nLDA')])

@pytest.mark.skip('wait')
@mock.patch('run.open')
def test_setup_two_args(mock_open):
    sys.argv[1:] = ['LDA', 'B3LYP']
    mock_file = mock.MagicMock()
    mock_open().__enter__.return_value = mock_file

    run.main()

    mock_file.write.assert_has_calls([mock.call('HF\nLDA\nB3LYP')])

@pytest.mark.skip('wait')
@mock.patch('run.open')
def test_setup_file_args(mock_open):
    sys.argv[1:] = ['-f', 'somefile']
    mock_infile = mock.MagicMock()
    mock_infile.read.return_value="F1\nF2"
    mock_outfile = mock.MagicMock()
    mock_open().__enter__.side_effect = [mock_infile, mock_outfile]


    run.main()

    mock_infile.read.assert_called_once_with()
    mock_outfile.write.assert_called_once_with("HF\nF1\nF2")

