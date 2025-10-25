.PHONY: setup test lint clean

setup:
	./scripts/setup_workspace.sh

test:
	python3 -m pytest -q

clean:
	./scripts/cleanup_workspace.sh