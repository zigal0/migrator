# SETUP
.PHONY: setup
setup:
	poetry install

# CHECK
.PHONY: lint
lint:
	poetry run mypy --strict migrator
	poetry run pylint migrator
	poetry run flake8 migrator

.PHONY: test
test:
	poetry run pytest --cov

.PHONY: check
check:
	make test
	make lint


