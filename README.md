# Репозиторий предназначен для Python Backend Course AITH

## Homework 1

### Описание
Проект "Математическое API" для вычисления факториалов, чисел Фибоначчи и среднего арифметического.
```text
aith_python_backend/
│
├── hw_1/
│   ├── calculations.py
│   ├── main.py
│   ├── routers.py
│   ├── requirements.txt
│   └── test/
│       ├── __init__.py
│       └── test_app.py
│
├── README.md
└── .gitignore
```

### Установка
1. **Клонирование репозитория:**
```bash
   git clone https://github.com/nbusko/aith_python_backend.git
```
2. **Перейти в директорию проекта, настроить окружение:**
```bash
   cd aith_python_backend/hw_1/
   python3 -m venv venv/
   source venv/bin/activate
   pip install -r requirements.txt
```
3. **Запустить сервер:**
```bash
   uvicorn main:app --reload --port=5050
```
4. **Открыть второй терминал, перейти в директорию с тестами и запустить их:**
```bash
   cd aith_python_backend/hw_1/test
   pytest .
```

Сервер доступен на localhost:5050 по умолчанию. При необходимости можно изменить порт в команде запуска и в `aith_python_backend/hw_1/test/test_app.py`.