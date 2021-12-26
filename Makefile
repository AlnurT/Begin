install_pre_commit:
	pre-commit install
	pre-commit install --hook-type commit-msg
	pre-commit autoupdate

lint:
	black .
	isort .
	flake8 .
	mypy .
