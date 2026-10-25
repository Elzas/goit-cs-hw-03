from psycopg2 import Error

from connect import create_connection


def create_table(conn, create_table_sql):
    """Створює таблиці за SQL-запитом."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == "__main__":
    sql_create_tables = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status (id),
        user_id INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE
    );
    """

    with create_connection() as conn:
        create_table(conn, sql_create_tables)
