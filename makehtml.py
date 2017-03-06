#!/usr/bin/env python
import sys
import os
import datetime
import pandas

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

def collect_status_column(loglines):
    status_tag = " ... "
    testcase_status = [line.split(status_tag) for line in loglines if status_tag in line]
    functional = [t[0].split('_')[-1] for t in testcase_status]
    status = [t[1] for t in testcase_status]
    return pandas.Series(status, index=functional)

def collect_status_table(*logs):
    series = [collect_status_column(open(log)) for log in logs]
    df = pandas.concat(series, axis=1)
    df.columns=logs
    return df

def get_git_revision(lines):
    for line in lines:
        if "Git" in line:
            return line.split('|')[1].strip()
    

def main(logfiles):
    tmp = os.environ['TMPDIR']

    dirs = get_dirs(logfiles)
    allfiles = [open('hf_availfun')] + [open(log) for log in logfiles]




    header = ["Functional"] + ['<a href="%s">%s</a>'%(tail(log), short(log)) for log in logfiles]

    htmlfile = open('test_findif.html', 'w')
    htmlfile.write('''\
<!DOCTYPE html>
<html>
  <head>
    <title>Finite differend tests</title>
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

    <h1>Dalton testing</h1>
    <h2>Finite field tests of DFT response functions</h2>
''')

    with open(root(logfiles[0]) + ".d/hf.out") as hfout:
        git_revision = get_git_revision(hfout)
                
    htmlfile.write("Calculated at %s <br>" % str(datetime.datetime.now()))
    htmlfile.write('Git revision: %s<br>' % git_revision)
    htmlfile.write('<table class="table table-bordered table-hover table-condensed">\n')
    htmlfile.write('<tr><th>' + '</th><th>'.join(header) + '</th></tr>\n')
    for ijk in zip(*allfiles):
        spl = [ line.split('...')[-1].strip() for line in ijk ]
        dal = spl[0].strip('*').replace('/', '_').replace('-','_').lower()
        for i, stat_dir in enumerate(zip(spl[1:], dirs)):
            stat, _dir = stat_dir
            if "FAIL" in stat:
                spl[i+1] = "<a href=%s/%s.out>FAIL</a>" % (_dir, dal)
            if "ERROR" in stat:
                spl[i+1] = "<a href=%s/%s.out>ERROR</a>" % (_dir, dal)
                
        htmlfile.write('<tr><td>' + '</td><td>'.join(spl) + '</td></tr>\n')
    htmlfile.write('</table>')
    htmlfile.write('*A fraction of HF exchange was used to aid SCF convergence<br>')
    htmlfile.write('''
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://code.jquery.com/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="dist/js/bootstrap.min.js"></script>
  </div></body>
</html>
''')
    htmlfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
