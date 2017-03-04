import os
import subprocess
import math
import multiprocessing
from errors import MolError

ncpu = multiprocessing.cpu_count()

class FinDif: 
    """Take objects with an exe method taking a 
    float argument returning a numerical object supporting subtraction
    and scalar multiplication allowing for finite differetiation"""

    def __init__(self, obj):
        self.obj = obj

    def first(self):
        d = self.obj.delta
        exe = self.obj.exe
        ret1 = exe(0.5*d)
        ret2 = exe(-0.5*d)
        return  (1/d) * (ret1 - ret2)

    def second(self):
        d = self.obj.delta
        exe = self.obj.exe
        ret1 = exe(0.5*d)
        ret2 = exe(-0.5*d)
        ret0 = exe(0.0)
        return  (4/d**2) * (ret1 - 2*ret0  + ret2)

class RspCalc:
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
        return self.dal.split('\n')[-1].replace(' ','_').replace('/','_')

    def exe(self, delta=None):

        global ncpu
        if self.mol is None:
            raise MolError

        with open(self._dal_ + ".dal", 'w') as dalfile:
            dalfile.write(self.dalinp(delta))
    
        with open(self._dal_ + ".mol", 'w') as molfile:
            molfile.write(self.mol)

        if not self.parallel:
            ncpu = 1

        cmd = "dalton -N %d -d -t /tmp/ExpVal_%s %s" % (ncpu, self._dal_, self._dal_)
        try:
            with open('log', 'w') as log:
                retval = subprocess.call(cmd, stdout=log, stderr=log, shell=True)
            if retval == 0:
                print("Dalton called OK")
            else:
                raise OSError(open('log').read())
        except OSError as e:
            print(e)
            raise

        result = None
        rsp_order = len(self.ops)
        if rsp_order > 0:
            A = self.ops[0].split()[0]
        if rsp_order > 1:
            B = self.ops[1].split()[0]
        if rsp_order > 2:
            C = self.ops[2].split()[0]
        for line in open(self._dal_ + ".out"):
            if rsp_order == 0:
                if "Final" in line and "energy" in line:
                    data = line.split(':')[1].replace('D', 'E')
                    result = float(data)
                    break
            elif rsp_order == 1:
                if "total" in line and A in line:
                    data = line.split(':')[1].replace('D', 'E')
                    result = float(data)
                    break
            elif rsp_order == 2:
                if "@" in line and A in line and B in line:
                    data = line.split('=')[1].replace('D', 'E')
                    result = -float(data)
                    break
            elif rsp_order == 3:
                if "@ omega" in line:
                    data = line.split()[-1]
                    result = float(data)
                    break
            elif rsp_order == 4:
                if "@ << A; B, C, D >>" in line:
                    data = line.split()[-1]
                    result = float(data)
                    break
            else:
                raise RuntimeError("Response order %d not implemented" % rsp_order)

        if result is None or math.isnan(result): 
            raise ValueError
        return result

    def dalinp(self, delta=None):
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
        if self.field and delta:
            ff = "*HAMILTON\n.FIELD\n%g\n%s"%(delta, self.field)
        else:
            ff = "###"
        return ff

    def rspinp(self):

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
        return len(self.ops) > 0

    def is_expectation_value(self):
        return len(self.ops) == 1

    def is_lr(self):
        return len(self.ops) == 2

    def is_qr(self):
        return len(self.ops) == 3

    def is_cr(self):
        return len(self.ops) == 4
        
    def triplet_label(self):
        if self.triplet:
            return ".TRPFLG"
        else:
            return "#"

    def evinp(self):
        return ".PROPAV\n%s" % self.ops[0]

    def lrinp(self):
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
