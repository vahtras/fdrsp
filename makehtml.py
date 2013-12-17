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
htmlfile.write(str(datetime.datetime.now()))
htmlfile.write('<table border="1">\n')
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
htmlfile.write('*A fraction of HF exchange was used to aid SCF convergence')
htmlfile.close()

