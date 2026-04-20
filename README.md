# Тестовый проект для автоматизированного тестирования Яндекс Диска на python

Реализованы автотесты-примеры на в основном положительные сценарии + проверки некоторых полей в ответе

## Структура проекта

```text
Pytest/
├── client/
│   └── resources/
│       └── client.py       # HTTP-клиент для запросов к API
├── model/
│   └── resources/
│       └── response.py     # Pydantic-модели для парсинга ответов
├── tests/
│   └── api/
│       └── resources/
│           ├── copy_resources_test.py
│           ├── create_resources_test.py
│           ├── delete_resources_test.py
│           └── get_resources_test.py
├── utils/
│   ├── config.py           # Загрузка конфигов
│   └── secret.py.example   # Шаблон для secret.py (токен) 
├── .gitignore
├── Makefile                # Удобные команды: make test, make run
├── requirements.txt        # Зависимости
└── secret.py.example       # Шаблон для secret.py
```

## Установка и запуск
создайте виртуальное окружение и установите зависимости
```commandline
python -m venv .venv
source .venv/bin/activate    # macOS/Linux

.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
Также отредоктируйте файл `secret.py.example`, подставив OAuth-токен

Запуск тестов:
```commandline
pytest -v
```