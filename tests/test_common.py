import mock
from . import fdrsp


@mock.patch('fdrsp.common_findif.open')
def test_hf_dft(mock_open):
    runfile = mock.MagicMock()
    templates = {'key': '@pytest.mark.parametrize("functional", [%s])<...>'}
    mock_open().__enter__.return_value = runfile

    fdrsp.common_findif.process_pt(templates, ["LDA", "LYP*"])

    runfile.write.assert_has_calls([
        mock.call(fdrsp.common_findif.setup),
        mock.call('@pytest.mark.parametrize("functional", ["HF", "LDA", "LYP*"])<...>'),
        ])
