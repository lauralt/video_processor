PYTHON=python3
MAIN=main.py

run:
	$(PYTHON) $(MAIN)

test:
	pytest tests/

# Format the code.
format:
	black .

# Lint the code.
lint:
	ruff check .

# Remove temporary files.
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -f output.mp4
