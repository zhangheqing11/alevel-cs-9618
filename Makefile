# The repo folder name contains a space, so the venv lives outside it.
PY := $(HOME)/.venvs/alevel-cs/bin/python

.PHONY: setup check check-all check-scope build try

setup:
	python3 -m venv $(HOME)/.venvs/alevel-cs
	$(PY) -m pip install -q -r requirements.txt

check:            ## schema/link/quote checks + tests of changed exercises
	$(PY) tools/check.py

check-all:        ## same, but run every exercise
	$(PY) tools/check.py --all-exercises

check-scope:      ## make check-scope TASK=T12
	$(PY) tools/check_scope.py $(TASK)

build:            ## regenerate output/ (implemented by T13)
	@if [ -f build/build.py ]; then $(PY) build/build.py all; else echo "build/build.py not implemented yet (T13)"; fi

try:              ## make try EX=practice/p2/<exercise>
	$(PY) tools/try.py "$(EX)"
