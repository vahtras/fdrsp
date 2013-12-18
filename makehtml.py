#!/usr/bin/env python
import sys
import os
import datetime

logfiles = sys.argv[1:]
dirs = [ os.path.splitext(log)[0]+'.d' for log in logfiles ]
allfiles = [open('hf_availfun')] + [open(log) for log in logfiles]

def short(log):
   return os.path.splitext(log)[0].split('_findif_')[1]

header = ["Functional"] + ['<a href="%s">%s</a>'%(log, short(log)) for log in logfiles]

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
with open('./test_findif_lr_closed_singlet.d/hf.out') as hfout:
    for line in hfout:
        if "Git" in line:
            git_revision = line.split('|')[1]
            break
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
htmlfile.write("Calculated at %s <br>" % str(datetime.datetime.now()))
htmlfile.write('''
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://code.jquery.com/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="dist/js/bootstrap.min.js"></script>
  </div></body>
</html>
''')
htmlfile.close()

