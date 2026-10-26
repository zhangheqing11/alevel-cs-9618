# The repo folder name contains a space, so the venv lives outside it.
PY := $(HOME)/.venvs/alevel-cs/bin/python
UNIT_TEST_PATHS := pipeline/er pipeline/extract pipeline/mock pipeline/tag tools build/tests

.PHONY: setup check check-all unit-tests check-scope build try

setup:
	python3 -m venv $(HOME)/.venvs/alevel-cs
	$(PY) -m pip install -q -r requirements.txt

check:            ## schema/link/quote checks + changed exercises + project unit tests
	$(PY) tools/check.py
	$(MAKE) unit-tests

check-all:        ## same, but run every exercise and project unit tests
	$(PY) tools/check.py --all-exercises
	$(MAKE) unit-tests

unit-tests:       ## run the non-exercise project unit-test suites
	$(PY) -m pytest -q -p no:cacheprovider --rootdir . $(UNIT_TEST_PATHS)

check-scope:      ## make check-scope TASK=T12
	$(PY) tools/check_scope.py $(TASK)

build:            ## regenerate output/ (implemented by T13)
	@if [ -f build/build.py ]; then $(PY) build/build.py all; else echo "build/build.py not implemented yet (T13)"; fi

try:              ## make try EX=practice/p2/<exercise> [K=1b]
	$(PY) tools/try.py "$(EX)" "$(K)"
