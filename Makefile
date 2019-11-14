all:
	pytest -v --cov=fdrsp --cov run  sample_tests tests --cov-report html
view:
	xdg-open sample_tests/index.html

