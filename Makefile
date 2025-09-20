.PHONY: init lint run

init:
	uv tool run pre-commit install
	uv sync --dev

lint:
	uv tool run ruff check --fix src
	uv tool run ruff format src

run:
	uv run -m src.main

streamlit:
	uv run -m streamlit run src/streamlit_ui.py