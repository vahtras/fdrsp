"""
Utility module for setting up Dalton response calculations calculations
with finite field differentiation
"""

import subprocess
import math
import multiprocessing
from .errors import MolError


class FinDif(object):
    """Take objects with an exe method taking a
    float argument returning a numerical object supporting subtraction
    and scalar multiplication allowing for finite differetiation"""

    def __init__(self, obj):
        self.obj = obj

    def first(self):
        """First finite-field derivative of object method exe"""
        delta = self.obj.delta
        exe = self.obj.exe
        return  (1/delta) * (exe(0.5*delta) - exe(-0.5*delta))

    def second(self):
        """Second finite-field derivative of object method exe"""
        delta = self.obj.delta
        exe = self.obj.exe
        return  (4/delta**2) * (exe(0.5*delta) + exe(-0.5*delta)- 2*exe())

class RspCalc(object):
    """Execute dalton LR"""
    def __init__(self, *args, **kwargs):
        self.parallel = kwargs.get('parallel', True)

        self.wf = kwargs.get('wf', 'HF')
        self.field = kwargs.get('field', None)
        self.delta = kwargs.get('delta', 0)

        self.ops = args
        self.triplet = kwargs.get('triplet', False)
        self.aux = kwargs.get('aux', '#')

        self.dal = kwargs.get('dal', self.wf)
        self.mol = kwargs.get('mol', None)

    @property
    def _dal_(self):
        return self.dal.split('\n')[-1].replace(' ', '_').replace('/', '_')

    def exe(self, delta=None):
        """Method supporting optional differential parameter"""

        if self.mol is None:
            raise MolError

        with open(self._dal_ + ".dal", 'w') as dalfile:
            dalfile.write(self.dalinp(delta))

        with open(self._dal_ + ".mol", 'w') as molfile:
            molfile.write(self.mol)

        self.run()

        return self.get_output()

    def dalinp(self, delta=None):
        """Setup Dalton input"""

        _dalinp = """\
**DALTON INPUT
.RUN RESPONSE
.DIRECT
%s
%s
**END OF DALTON
""" % (self.wavinp(delta), self.rspinp())
        return _dalinp

    def wavinp(self, delta=None):
        """Setup Dalton WaveFunction input"""
        _wavinp = """\
**WAVE FUNCTION
.%s
*SCF INPUT
.NOQCSCF
.THRESHOLD
1e-11
%s""" % (self.wf, self.finite_field(delta))
        return  _wavinp

    def finite_field(self, delta=None):
        """Finite field section of Dalton intput"""

        if self.field and delta:
            ff_input = "*HAMILTON\n.FIELD\n%g\n%s"%(delta, self.field)
        else:
            ff_input = "###"
        return ff_input

    def rspinp(self):
        """Response section of Daltin input"""

        if self.is_response():
            _rspinp = """\
**RESPONSE
%s""" % self.triplet_label()
        else:
            _rspinp = "###"

        if self.is_expectation_value():
            _rspinp += "\n%s" % self.evinp()

        if self.is_lr():
            _rspinp += "\n%s" % self.lrinp()

        if self.is_qr():
            _rspinp += "\n%s" % self.qrinp()

        if self.is_cr():
            _rspinp += "\n%s" % self.crinp()

        return _rspinp

    def is_response(self):
        """Calculation involves response"""
        return len(self.ops) > 0

    def is_expectation_value(self):
        """Calculation involves expectaion value"""
        return len(self.ops) == 1

    def is_lr(self):
        """Calculation involves linear response"""
        return len(self.ops) == 2

    def is_qr(self):
        """Calculation involves quadratic response"""
        return len(self.ops) == 3

    def is_cr(self):
        """Calculation involves cubic response"""
        return len(self.ops) == 4

    def triplet_label(self):
        """Triplet input label"""

        if self.triplet:
            return ".TRPFLG"
        else:
            return "#"

    def evinp(self):
        """Expectation value input"""

        return ".PROPAV\n%s" % self.ops[0]

    def lrinp(self):
        """Linear response input section"""
        _lrinp = """\
*LINEAR
.THCLR
1e-10
.PROPRT
%s
.PROPRT
%s""" % tuple(self.ops[:2])
        return _lrinp

    def qrinp(self):
        """Quadratic response input section"""
        _qrinp = """\
*QUADRATIC
.THCLR
1e-10
.APROP
%s
.BPROP
%s
.CPROP
%s""" % tuple(self.ops[:3])
        if self.triplet:
            _qrinp += """
.ISPABC
 1 1 0"""
        return _qrinp

    def crinp(self):
        """Cubic response input section"""
        _crinp = """\
*CUBIC
.THCLR
1e-10
.APROP
%s
.BPROP
%s
.CPROP
%s
.DPROP
%s""" % tuple(self.ops[:4])
        return _crinp

    def run(self):
        """
        Interface method for executing Dalton

        dalton should be in the $PATH environment variable
        will run in parallel unless self.parallel is False
        """

        if self.parallel:
            ncpu = multiprocessing.cpu_count()
        else:
            ncpu = 1

        cmd = "dalton -N %d -d -t /tmp/ExpVal_%s %s" % (ncpu, self._dal_, self._dal_)
        try:
            with open('log', 'w') as log:
                retval = subprocess.call(cmd, stdout=log, stderr=log, shell=True)
            if retval == 0:
                print("Dalton called OK")
            else:
                raise OSError(open('log').read())
        except OSError as error:
            print(error)
            raise


    def get_output(self):
        """Collect results from output files after successful calculation"""

        result = None
        rsp_order = len(self.ops)

        filename = self._dal_ + ".out"
        for line in open(filename):
            if rsp_order == 0:
                if "Final" in line and "energy" in line:
                    result = last_float(line)
                    break
            elif rsp_order == 1:
                if "total" in line and self.ops[0] in line:
                    result = last_float(line)
                    break
            elif rsp_order == 2:
                if "@" in line and self.ops[0].split()[0] in line and self.ops[1].split()[0] in line:
                    result = -last_float(line)
                    break
            elif rsp_order == 3:
                if "@ omega" in line:
                    result = last_float(line)
                    break
            elif rsp_order == 4:
                if "@ << A; B, C, D >>" in line:
                    result = last_float(line)
                    break
            else:
                raise RuntimeError("Response order %d not implemented" % rsp_order)

        if result is None or math.isnan(result):
            raise ValueError

        return result

def last_float(line):
    """Return last element of line input as float"""
    return float(line.split()[-1].replace('D', 'e'))
