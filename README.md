# goit-cs-hw-03

Домашнє завдання до модуля «Вступ до вивчення систем управління базами даних».

## Структура

```
task1/
  connect.py        # підключення до PostgreSQL
  create_table.py   # створення таблиць users, status, tasks
  seed.py           # наповнення таблиць випадковими даними (Faker)
  queries.sql       # 14 SQL-запитів
task2/
  main.py           # CRUD-операції з MongoDB через PyMongo
docker-compose.yml  # PostgreSQL + MongoDB локально
```

## Запуск

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
```

### Завдання 1 — PostgreSQL

```bash
cd task1
python create_table.py
python seed.py
psql -h localhost -p 5433 -U postgres -d task_manager -f queries.sql   # пароль: postgres
```

Схема:
- `users(id SERIAL PK, fullname VARCHAR(100), email VARCHAR(100) UNIQUE)`
- `status(id SERIAL PK, name VARCHAR(50) UNIQUE)` — `new`, `in progress`, `completed`
- `tasks(id SERIAL PK, title VARCHAR(100), description TEXT, status_id → status.id, user_id → users.id ON DELETE CASCADE)`

### Завдання 2 — MongoDB

```bash
cd task2
python main.py
```

Меню: усі коти, пошук за ім'ям, оновлення віку, додавання характеристики, видалення за ім'ям, видалення всіх, тестові дані.
