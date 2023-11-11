env:
	@echo "Activating virtual environment..."
	poetry shell

install:
	@echo "Installing dependencies..."
	poetry install

setup:
	@echo "Setting up project..."
	poetry run python -m src.setup

cleanup:
	@echo "Cleaning up..."
	poetry run python -m src.cleanup

.PHONY: env install setup cleanup
