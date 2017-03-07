import common_findif
import mock

@mock.patch('common_findif.open')
def test_hf_only(mock_open):
    runfile = mock.MagicMock()
    templates = {"key": "<%s|%s|%s>"}
    mock_open().__enter__.return_value = runfile

    common_findif.process(templates, [])

    runfile.write.assert_has_calls([
        mock.call(common_findif.setup),
        mock.call('<HF|HF|hf>'),
        mock.call(common_findif.main)
        ])

@mock.patch('common_findif.open')
def test_hf_lda(mock_open):
    runfile = mock.MagicMock()
    templates = {"key": "<%s|%s|%s>"}
    mock_open().__enter__.return_value = runfile

    common_findif.process(templates, ["LDA", "LYP*"])

    runfile.write.assert_has_calls([
        mock.call(common_findif.setup),
        mock.call('<HF|HF|hf>'),
        mock.call('<LDA|DFT\\nLDA|lda>'),
        mock.call('<LYP|DFT\\nGGAKey hf=0.500000 LYP=0.500000|lyp>'),
        mock.call(common_findif.main)
        ])

@mock.patch('common_findif.open')
def test_hf_dft(mock_open):
    runfile = mock.MagicMock()
    templates = {'key': '@pytest.mark.parametrize("functional", [%s])<...>'}
    mock_open().__enter__.return_value = runfile

    common_findif.process_pt(templates, ["LDA", "LYP*"])

    runfile.write.assert_has_calls([
        mock.call(common_findif.setup),
        mock.call('@pytest.mark.parametrize("functional", ["HF", "LDA", "LYP*"])<...>'),
        #mock.call(common_findif.main)
        ])
