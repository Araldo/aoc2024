setup:
	pyenv install 3.12.7
	pyenv virtualenv 3.12.7 aoc2024

install:
	pip install uv
	uv pip compile requirements.in > requirements.txt
	uv pip install -r requirements.txt
