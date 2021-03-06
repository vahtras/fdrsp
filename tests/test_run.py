import os
import sys
from unittest import mock

import pytest

import run
import fdrsp


def test_in_path():
    os.environ['PATH'] = ""
    with pytest.raises(SystemExit):
        run.assert_dalton()


def test_select_functionals_in_arg():
    sys.argv[1:] = ['slater']
    args = run.parse_input()
    m = mock.mock_open()
    with mock.patch('run.open', m, create=True):
        run.save_selected_functionals(args)
        m.assert_called_with('tested_functionals', 'w')
        m().write.assert_called_with('slater')


def test_select_functionals_on_file():
    sys.argv[1:] = ['-f', 'ffile']
    args = run.parse_input()
    with mock.patch(
            'run.open', mock.mock_open(read_data='foo'), create=True
            ) as m:
        run.save_selected_functionals(args)
        m.assert_called_with('ffile')
        m().write.assert_called_with('foo')
