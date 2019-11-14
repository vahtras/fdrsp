#!/usr/bin/env python
import re
import sys
import os
import datetime
import pandas

pandas.set_option("display.max_colwidth", -1)


def main(*logfiles, **config):
    tmp = config["tmp"]

    header = ["Functional"] + [
        '<a href="%s">%s</a>' % (
            file_to_html(log), short(log)
        ) for log in logfiles
    ]

    with open(os.path.join(tmp, "test_findif.html"), "w") as htmlfile:
        htmlfile.write(html_head(
            "Dalton testing", "Finite field tests of DFT response functions"
            )
        )
        htmlfile.write("Calculated at %s <br>" % str(datetime.datetime.now()))
        with open(root(logfiles[0]) + ".d/HF.out") as hfout:
            htmlfile.write("Git revision: %s<br>" % get_git_revision(hfout))
        df = collect_status_table_pt(*logfiles, **config)
        df.columns = header[1:]
        htmlfile.write(df.to_html(classes="table table-striped", escape=False))
        htmlfile.write(
            "*A fraction of HF exchange was used to aid SCF convergence<br>"
            )
        htmlfile.write(html_tail())


def get_dirs(logs):
    return [os.path.splitext(log)[0] + ".d" for log in logs]


def tail(path):
    return os.path.split(path)[1]


def file_to_html(fname):
    hname = fname + ".html"
    with open(hname, "w") as html:
        html.write(html_head(h2=tail(fname)))
        html.write("<pre>")
        html.write(open(fname).read())
        html.write("</pre>")
        html.write(html_tail())
    return os.path.basename(hname)


def short(log):
    _, log_file = os.path.split(log)
    log_file_root = os.path.splitext(log_file)[0]
    log_header = log_file_root.split("test_findif_")[1]
    return log_header


def html_head(h1="", h2="", container=""):
    return """
<!DOCTYPE html>
<html>
  <head>
    <title>Finite different tests</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="data/css/bootstrap.min.css" rel="stylesheet">
    <link href="../data/css/bootstrap.min.css" rel="stylesheet">

  </head>
  <body>
      <div class="container%s">
          <h1>%s</h1>
          <h2>%s</h2>
""" % (
        container,
        h1,
        h2,
    )


def root(path):
    return os.path.splitext(path)[0]


def get_git_revision(lines):
    for line in lines:
        if "Git" in line:
            return line.split("|")[1].strip()


def collect_status_table_pt(*logs, **config):
    series = [collect_status_column_pt(log, **config) for log in logs]
    df = pandas.concat(series, axis=1)
    df.columns = logs
    return df


def collect_status_column_pt(log, **config):
    import xml.etree.ElementTree as ET

    tree = ET.parse(log)
    testsuites = tree.getroot()

    statuses = []
    testcases = []
    functionals = []
    for testsuite in testsuites:
        for testcase in testsuite:
            if 'error' in testcase.attrib:
                status = 'ERROR'
            elif 'failure' in [t.tag for t in testcase]:
                status = 'FAILED'
            else:
                status = 'PASSED'
            statuses.append(status)
            testcases.append(testcase.attrib['classname'].split('.')[-1])
            functionals.append(get_functional(testcase.attrib['name']))

    outputs = [
        root(t) + ".d/%s.out" % canonical(f)
        for t, f in zip(testcases, functionals)
    ]
    generate_outputs_side_by_side_as_html(*outputs, **config)
    outputs_html = [o + ".html" for o in outputs]
    status = [
        '<a href="%s">%s</a>' % (o, s)
        for o, s in zip(outputs_html, statuses)
    ]
    return pandas.Series(status, index=functionals)


def generate_outputs_side_by_side_as_html(*outputs, **config):
    for o in outputs:
        fo = os.path.join(config["tmp"], o)
        files_to_html(fo, fo + ".0", fo + ".1")


def files_to_html(*fnames):
    hname = fnames[0] + ".html"
    col_width = 12 // len(fnames)
    with open(hname, "w") as html:
        html.write(html_head(container="-fluid"))
        for f in fnames:
            html.write(
                "<div class='col-md-%d'>" % col_width
                + "<h2>%s</h2>" % tail(f)
                + "<pre>"
                + open(f).read()
                + "</pre></div>"
            )
        html.write(html_tail())
    return hname


def get_functional(logline):
    import re

    return re.match(r".*\[([\w/]+\*?)\].*", logline).group(1)


def canonical(s):
    return s.replace("/", "_")


def html_tail():
    return """
    <script src="https://code.jquery.com/jquery.js"></script>
    <script src="data/js/bootstrap.min.js"></script>
  </div></body>
</html>
"""


if __name__ == "__main__":
    main(*sys.argv[1:], tmp='sample_tests')
