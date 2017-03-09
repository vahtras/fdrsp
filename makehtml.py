#!/usr/bin/env python
import sys
import os
import re
import datetime
import pandas
pandas.set_option('display.max_colwidth', -1)


def head(path):
    return os.path.split(path)[0]

def tail(path):
    return os.path.split(path)[1]

def root(path):
    return os.path.splitext(path)[0]

def ext(path):
    return os.path.splitext(path)[1]

def short(log):
   _, log_file = os.path.split(log)
   log_file_root = os.path.splitext(log_file)[0]
   log_header = log_file_root.split('test_findif_')[1]
   return log_header

def get_dirs(logs):
    return [os.path.splitext(log)[0]+'.d' for log in logs]

def canonical(s):
    return s.replace('/', '_')

def collect_status_column_pt(loglines):
    status_tag = "::test_findif_"
    tmppath_testcase_status = [line.split(status_tag) for line in loglines if status_tag in line]
    functionals = [get_functional(line[1]) for line in tmppath_testcase_status]
    testcase = [root(tail(t[0])) + ".d/%s.out" % canonical(f) for t,f in zip(tmppath_testcase_status, functionals)]
    status = [
        '<a href="%s">%s</a>' % (t, s[1].split()[1])
        for t, s in zip(testcase, tmppath_testcase_status)
        ]
    return pandas.Series(status, index=functionals)

def get_functional(logline):
    import re
    return re.match(r'.*\[([\w/]+\*?)\].*', logline).group(1)

def collect_status_table_pt(*logs):
    series = [collect_status_column_pt(open(log)) for log in logs]
    df = pandas.concat(series, axis=1)
    df.columns=logs
    return df

def get_git_revision(lines):
    for line in lines:
        if "Git" in line:
            return line.split('|')[1].strip()
    

def main(*logfiles):
    tmp = os.environ['TMPDIR']

    dirs = get_dirs(logfiles)
    allfiles = [open('hf_availfun')] + [open(log) for log in logfiles]

    header = ["Functional"] + ['<a href="%s">%s</a>'%(tail(log), short(log)) for log in logfiles]

    with open('test_findif.html', 'w') as htmlfile:
        htmlfile.write(html_head('Dalton testing', 'Finite field tests of DFT response functions'))
        htmlfile.write("Calculated at %s <br>" % str(datetime.datetime.now()))
        with open(root(logfiles[0]) + ".d/HF.out") as hfout:
            htmlfile.write('Git revision: %s<br>' % get_git_revision(hfout))
        df = collect_status_table_pt(*logfiles)
        df.columns = header[1:]
        htmlfile.write(df.to_html(classes="table table-striped", escape=False))
        htmlfile.write('*A fraction of HF exchange was used to aid SCF convergence<br>')
        htmlfile.write(html_tail())

def html_head(h1="", h2=""):
    return """
<!DOCTYPE html>
<html>
  <head>
    <title>Finite different tests</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>
  <body><div class="container">
    <h1>%s</h1><h2>%s</h2>
""" % (h1, h2)

def html_tail():
    return '''
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://code.jquery.com/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="dist/js/bootstrap.min.js"></script>
  </div></body>
</html>
'''


if __name__ == "__main__":
    main(*sys.argv[1:])
