.PHONY: help install install-dev clean run setup-uv

help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install all dependencies including dev"
	@echo "  make clean        - Remove virtual environment and cache"
	@echo "  make run          - Run the main script"
	@echo "  make setup-uv     - Install UV package manager"

setup-uv:
	@echo "Installing UV..."
	@curl -LsSf https://astral.sh/uv/install.sh | sh || \
		(echo "Failed to install UV via curl. Please install manually from https://github.com/astral-sh/uv" && exit 1)
	@echo "UV installed successfully!"

install:
	@echo "Creating virtual environment and installing dependencies..."
	@uv venv --python 3.13 || python3.13 -m venv .venv
	@uv pip sync requirements.txt || .venv/bin/pip install -r requirements.txt
	@echo "Installation complete! Activate with: source .venv/bin/activate"

install-dev:
	@echo "Creating virtual environment and installing all dependencies..."
	@uv venv --python 3.13 || python3.13 -m venv .venv
	@uv pip sync requirements.txt requirements-dev.txt || \
		(.venv/bin/pip install -r requirements.txt && .venv/bin/pip install -r requirements-dev.txt)
	@echo "Installation complete! Activate with: source .venv/bin/activate"

clean:
	@echo "Cleaning up..."
	@rm -rf .venv __pycache__ .pytest_cache .mypy_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Cleanup complete!"

run:
	@if [ ! -d ".venv" ]; then \
		echo "Virtual environment not found. Running 'make install' first..."; \
		$(MAKE) install; \
	fi
	@.venv/bin/python main.py
