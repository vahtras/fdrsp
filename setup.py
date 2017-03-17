from setuptools import setup

setup(
name='fdrsp',
packages=['fdrsp'],
pagkage_data={'fdrsp': ['data/*/*']},
scripts=["run.py"],
author="Olav Vahtras",
author_email="vahtras@kth.se",
description='Finite difference testing of DFT response',
install_requires = ["pytest", "pandas", "mock"],
)
