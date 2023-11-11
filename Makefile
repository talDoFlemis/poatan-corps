env:
	@echo "Activating virtual environment..."
	poetry shell

install:
	@echo "Installing dependencies..."
	poetry install

setup:
	@echo "Setting up project..."
	poetry run python -m src.setup

consults:
	@echo "Running consults..."
	poetry run python -m src.consults

transaction:
	@echo "Running transaction..."
	poetry run python -m src.transaction

stored_procedure:
	@echo "Running stored_procedure..."
	poetry run python -m src.stored_procedure

trigger:
	@echo "Running trigger..."
	poetry run python -m src.trigger

cleanup:
	@echo "Cleaning up..."
	poetry run python -m src.cleanup

.PHONY: env install setup cleanup transaction stored_procedure trigger
