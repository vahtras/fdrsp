import os
import pytest


def pytest_addoption(parser):
    parser.addoption('--with-functionals', action='append', default=[])


@pytest.fixture
def suppdir():
    suppdir = 'sample_tests'
    if not os.path.isdir(suppdir):
        os.mkdir(suppdir)
    os.chdir(suppdir)
