import os
import pytest


def pytest_addoption(parser):
    parser.addoption('--with-functionals', action='append', default=[])


@pytest.fixture
def suppdir():
    n, e = os.path.splitext(__file__)
    suppdir = n + ".d"
    if not os.path.isdir(suppdir):
        os.mkdir(suppdir)
    os.chdir(suppdir)
