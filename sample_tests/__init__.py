import numpy as np


def assert_(num, ana):
    atol = 1e-8
    print("Numerical ", num)
    print("Analytical", ana)
    print("Difference ", abs(num - ana))
    print("Target diff", atol + 0.001000 * abs(ana))
    assert np.allclose(num, ana, rtol=0.001000)


def dft(functional):
    if functional.upper() == "HF":
        return functional
    elif "*" in functional:
        return "DFT\nGGAKey hf=0.5 %s=0.5" % functional.strip("*")
    else:
        return "DFT\n%s" % functional
