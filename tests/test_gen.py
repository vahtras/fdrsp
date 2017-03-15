
import fdrsp.gen_findif_all

def test_main():
    pass


def test_generate_templates():
    templates = fdrsp.gen_findif_all.generate_templates('A', 'B', 'C', 'D')

    first_template = """
@pytest.fixture(params=[%s])
def run_response(request):
    functional = request.param
    wf=dft(functional)
    dal=functional
    escf = FinDif(RspCalc(wf=wf, dal=dal, mol=inp["h2o"], field='D', delta=0.001)).first() 
    ev = RspCalc('D', wf=wf, dal=dal, mol=inp["h2o"]).exe()
    return (escf, ev)
"""
    assert templates['ev_closed_singlet'] == first_template
