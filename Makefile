# Makefile

install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

.PHONY: install brain-games even-games build publish package-install lint
