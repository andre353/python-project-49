# Makefile

install:
	poetry install

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

.PHONY: install brain-games build publish package-install	lint
