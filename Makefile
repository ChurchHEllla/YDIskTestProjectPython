# Создание окружения и установка зависимостей
setup-mac:
	python3 -m venv .venv
	pip install --upgrade pip
	pip install -r requirements.txt

setup-win:
	python -m venv .venv
	pip install --upgrade pip
	pip install -r requirements.txt

# Запуск тестов с тегом resources
test:
	pytest -v -m resources

# Очистка кэша и окружения
clean:
	rm -rf .venv .pytest_cache __pycache__