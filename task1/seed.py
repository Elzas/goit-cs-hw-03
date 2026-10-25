from random import randint, choice

import faker
from psycopg2 import Error

from connect import create_connection

NUMBER_USERS = 10
NUMBER_TASKS = 30
STATUSES = [("new",), ("in progress",), ("completed",)]


def generate_fake_data(number_users, number_tasks):
    """Генерує випадкових користувачів і завдання."""
    fake_data = faker.Faker()

    fake_users = [(fake_data.name(), fake_data.unique.email()) for _ in range(number_users)]

    fake_tasks = []
    for _ in range(number_tasks):
        # останні 2 користувачі залишаються без завдань
        fake_tasks.append((
            fake_data.sentence(nb_words=4),
            choice([fake_data.text(), None]),
            randint(1, len(STATUSES)),
            randint(1, number_users - 2),
        ))

    return fake_users, fake_tasks


def insert_data_to_db(users, tasks):
    """Очищає таблиці та заповнює їх даними."""
    with create_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute("TRUNCATE tasks, users, status RESTART IDENTITY")
            cur.executemany("INSERT INTO status (name) VALUES (%s)", STATUSES)
            cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)
            cur.executemany(
                "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                tasks,
            )
            conn.commit()
        except Error as e:
            print(e)


if __name__ == "__main__":
    insert_data_to_db(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
