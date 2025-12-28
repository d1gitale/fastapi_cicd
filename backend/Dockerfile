#Используем базовый образ python3.10
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
#Данная команда установит зависимости для запуска кода
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Данная команда запустит сервер uvicorn "наружу" (так как указан интерфейс 0.0.0.0) на порту 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
