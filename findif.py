import os
import math
import multiprocessing
#import dalinp

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
        #print ret1, ret2
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

    def exe(self, delta=None):

        global ncpu
        #Wave function
        if self.field and delta:
            ff = "*HAMILTON\n.FIELD\n%f\n%s"%(delta, self.field)
        else:
            ff = "###"


        wavinp = """**WAVE FUNCTIONS
.%s
*SCF INPUT
.NOQCSCF
.THRESHOLD
1e-11
%s""" % (self.wf, ff)

        #Response
        if self.triplet:
            trpflg = ".TRPFLG"
        else:
            trpflg = "#"

        rsp_order = len(self.ops)

        if (rsp_order == 0):
            rspinp = "###"
        elif (rsp_order == 1):
            A, = self.ops
            rspinp = """**RESPONSE
%s
.PROPAV
%s""" % (trpflg, A)

        elif (rsp_order == 2):
            A, B = self.ops
            rspinp = """**RESPONSE
%s
*LINEAR
.THCLR
1e-10
.PROPRT
%s
.PROPRT
%s
%s """ % (trpflg, A, B, self.aux)

        elif rsp_order == 3:
            if not self.parallel: ncpu = 1
            A, B, C = self.ops
            rspinp = """**RESPONSE
%s
*QUADRATIC
.THCLR
1e-10
.APROP 
%s
.BPROP
%s
.CPROP
%s
%s """ % (trpflg, A, B, C, self.aux)

        elif rsp_order == 4:
            A, B, C, D = self.ops
            rspinp = """**RESPONSE
%s
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
%s
%s""" % (trpflg, A, B, C, D, self.aux)

        else:
            raise RuntimeError("Response order %d not implemented" % rsp_order)

        dalinp = """**DALTON INPUT
.RUN RESPONSE
.DIRECT
%s
%s
**END OF DALTON
""" % (wavinp, rspinp)

        dal = self.dal.split('\n')[-1].replace(' ','_').replace('/','_')
        dalfile = open(dal + ".dal", 'w')
        dalfile.write(dalinp)
        dalfile.close()
    
        molfile = open(dal + ".mol", 'w')
        molfile.write(self.mol)
        molfile.close()

        cmd = "dalton -N %d -d -t /tmp/ExpVal_%s %s > log 2>&1 " % (ncpu, dal, dal)
        os.system(cmd)

        result = None
        if rsp_order > 0:
            A  = A.split()[0]
        if rsp_order > 1:
            B = B.split()[0]
        if rsp_order > 2:
            C = C.split()[0]
        for line in open(dal + ".out"):
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
            #import pdb; pdb.set_trace()
            raise ValueError
        return result


