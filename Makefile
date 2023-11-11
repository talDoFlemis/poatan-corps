env:
	@echo "Activating virtual environment..."
	poetry shell

install:
	@echo "Installing dependencies..."
	poetry install

.PHONY: env install
