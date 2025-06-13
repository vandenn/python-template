.PHONY: init setup run

init:
	uv tool run pre-commit install

lint:
	uv tool run ruff check --fix src
	uv tool run ruff format src

run:
	uv run src/main.py