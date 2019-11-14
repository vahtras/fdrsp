import fdrsp


def test_singleton():
    tmp1 = fdrsp.TmpDir()
    tmp2 = fdrsp.TmpDir()
    assert tmp1 is tmp2
