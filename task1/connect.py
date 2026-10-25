from contextlib import contextmanager

import psycopg2


@contextmanager
def create_connection():
    """Створює з'єднання з базою даних PostgreSQL."""
    conn = psycopg2.connect(
        host="localhost", port=5433, dbname="task_manager", user="postgres", password="postgres"
    )
    yield conn
    conn.rollback()
    conn.close()
