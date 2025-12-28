# Подключаем необходимые библиотеки
from fastapi import FastAPI
import redis
import psycopg2

# Создаем объект приложения FastAPI
app = FastAPI()

# Главная страница — проверка работы backend
@app.get("/")
def root():
    return {"message": "Backend is alive!"}

# Запрос к Redis: устанавливаем и получаем значение из кэша
@app.get("/cache")
def cache():
    # Подключаемся к Redis, контейнер называется "redis"
    r = redis.Redis(host="redis", port=6379)

    # Устанавливаем ключ "hello" в Redis с значением "world"
    r.set("hello", "world")

    # Получаем значение по ключу "hello"
    return {"cached": r.get("hello").decode()}  # Декодируем байтовую строку в обычную

# Запрос к базе данных PostgreSQL
@app.get("/db")
def db():
    # Подключаемся к базе данных PostgreSQL
    conn = psycopg2.connect(
        host="postgres",  # Имя контейнера для PostgreSQL
        user="postgres",
        password="postgres",
        dbname="appdb"
    )

    # Создаем курсор для выполнения SQL-запросов
    cur = conn.cursor()

    # Выполняем SQL-запрос для получения текущего времени базы данных
    cur.execute("SELECT now();")

    # Извлекаем результат запроса
    date = cur.fetchone()[0]

    # Возвращаем текущее время из базы данных
    return {"postgres_time": str(date)}
