.PHONY: init setup run

init:
	`which python3.11` -m venv venv
	venv/bin/pip install pip==23.2.1 pip-tools wheel --no-cache-dir
	venv/bin/pip-compile -o requirements.txt --no-header --no-emit-index-url --no-emit-trusted-host requirements.in
	venv/bin/pip-compile -o requirements-dev.txt --no-header --no-emit-index-url --no-emit-trusted-host requirements-dev.in

setup: requirements-dev.txt
	venv/bin/pip-sync requirements-dev.txt
	venv/bin/pre-commit install

lint:
	venv/bin/pre-commit run --all-files

run:
	`which python3.11` src/main.py
