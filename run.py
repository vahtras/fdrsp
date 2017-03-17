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

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('xc', nargs='*', default=[], help='Exchange-correlation functionals')
    parser.add_argument('-f', '--file', help='Exchange-correlation functionals')

    args = parser.parse_args()


    if args.file:
        with open(args.file) as f:
            funcs = f.read()
        with open('hf_availfun', 'w') as hf_funcs:
            hf_funcs.write(funcs)
    elif args.xc:
        with open('hf_availfun', 'w') as funcs:
            funcs.write('\n'.join(args.xc))
    else:
        with open('hf_availfun', 'w') as funcs:
            pass


    # generate test files
    config = {'tmp': tempfile.mkdtemp()}
    fdrsp.gen_findif_all.main('XXQUADRU','YYQUADRU','ZZQUADRU','YDIPLEN','hf_availfun', **config)
        
    # runtests
    tests = glob.glob(os.path.join(config['tmp'], 'test_findif*.py'))
    logs = [os.path.splitext(test)[0] + '.log' for test in tests]
    for test, log in zip(tests, logs):
        pytest.main([test, '-v', '--resultlog', log])

    # get files to html
    fdrsp.makehtml.main(*logs, **config)

    # copy stylefiles
    shutil.copytree(
        os.path.join(
            os.path.dirname(os.path.abspath(fdrsp.__file__)),
            'data'
        ),
        os.path.join(config['tmp'], 'data')
    )
    
    


if __name__ == "__main__":
    sys.exit(main())
