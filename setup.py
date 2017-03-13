from setuptools import setup

setup(
name='fdrsp',
packages=["fdrsp"],
scripts=["submitall"],
author="Olav Vahtras",
author_email="vahtras@kth.se",
description='Finite difference testing of DFT response',
install_requires = ["pytest", "pandas"],
)
