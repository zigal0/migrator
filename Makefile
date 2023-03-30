# Migrator
# example: make create-migration db_name=postgres migration_name=init
.PHONY: create-migration
create-migration:
	poetry run python migrator/main.py create $(db_name) $(migration_name)

.PHONY: migrate-up
migrate-up:
	poetry run python migrator/main.py migrate up

.PHONY: migrate-down
migrate-down:
	poetry run python migrator/main.py migrate down

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

# DOCKER
.PHONY: compose-up
compose-up:
	docker compose up -d

.PHONY: compose-down
compose-down:
	docker compose down

.PHONY: compose-rs
compose-rs:
	make compose-down
	make compose-up


