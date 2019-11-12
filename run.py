#!/usr/bin/env python
import sys
import os
import shutil
import pytest
import tempfile
import glob
import fdrsp.gen_findif_all
import fdrsp.makehtml
import fdrsp

FUNCTIONALS = "tested_functionals"


def main():

    config = {"tmp": fdrsp.TmpDir(), "functional_file": FUNCTIONALS}

    args = parse_input()

    assert_dalton()

    save_selected_functionals(args)

    generate_test_files(**config)

    # runtests
    tests = glob.glob(os.path.join(config["tmp"], "test_findif*.py"))
    logs = [os.path.splitext(test)[0] + ".log" for test in tests]
    for test, log in zip(tests, logs):
        pytest.main([test, "-v", "--resultlog", log])

    # get files to html
    fdrsp.makehtml.main(*logs, **config)

    # copy stylefiles
    shutil.copytree(
        os.path.join(os.path.dirname(os.path.abspath(fdrsp.__file__)), "data"),
        os.path.join(config["tmp"], "data"),
    )


def parse_input():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "xc", nargs="*", default=[], help="Exchange-correlation functionals"
    )
    parser.add_argument(
        "-f", "--file", help="Exchange-correlation functionals"
    )

    args = parser.parse_args()
    return args


def assert_dalton():
    if not shutil.which("dalton"):
        print("Dalton not in PATH")
        sys.exit(1)


def save_selected_functionals(args):
    with open(FUNCTIONALS, 'w') as funcs:
        if args.file:
            with open(args.file) as f:
                funcs.write(f.read())
        elif args.xc:
            funcs.write("\n".join(args.xc))


def generate_test_files(**config):
    # generate test files
    fdrsp.gen_findif_all.main(
        "XXQUADRU", "YYQUADRU", "ZZQUADRU", "YDIPLEN", **config
    )


if __name__ == "__main__":
    sys.exit(main())
