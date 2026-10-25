from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://localhost:27018/", serverSelectionTimeoutMS=5000)
db = client.book


def create_cats():
    """Додає тестових котів у колекцію."""
    try:
        result = db.cats.insert_many([
            {"name": "barsik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]},
            {"name": "Lama", "age": 2, "features": ["ходить в лоток", "не дає себе гладити", "сірий"]},
            {"name": "Liza", "age": 4, "features": ["ходить в лоток", "дає себе гладити", "білий"]},
        ])
        print(result.inserted_ids)
    except PyMongoError as e:
        print(e)


def read_all():
    """Виводить усі записи з колекції."""
    try:
        for cat in db.cats.find({}):
            print(cat)
    except PyMongoError as e:
        print(e)


def read_by_name(name):
    """Виводить інформацію про кота за ім'ям."""
    try:
        print(db.cats.find_one({"name": name}) or "Кота не знайдено")
    except PyMongoError as e:
        print(e)


def update_age(name, age):
    """Оновлює вік кота за ім'ям."""
    try:
        result = db.cats.update_one({"name": name}, {"$set": {"age": age}})
        print("Оновлено" if result.matched_count else "Кота не знайдено")
    except PyMongoError as e:
        print(e)


def add_feature(name, feature):
    """Додає нову характеристику коту за ім'ям."""
    try:
        result = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
        print("Оновлено" if result.matched_count else "Кота не знайдено")
    except PyMongoError as e:
        print(e)


def delete_by_name(name):
    """Видаляє кота за ім'ям."""
    try:
        result = db.cats.delete_one({"name": name})
        print("Видалено" if result.deleted_count else "Кота не знайдено")
    except PyMongoError as e:
        print(e)


def delete_all():
    """Видаляє всі записи з колекції."""
    try:
        result = db.cats.delete_many({})
        print(f"Видалено: {result.deleted_count}")
    except PyMongoError as e:
        print(e)


if __name__ == "__main__":
    while True:
        command = input("\n1-всі, 2-знайти, 3-вік, 4-характеристика, 5-видалити, 6-видалити всіх, 7-тестові дані, 0-вихід: ")
        if command == "1":
            read_all()
        elif command == "2":
            read_by_name(input("Ім'я: "))
        elif command == "3":
            name = input("Ім'я: ")
            try:
                update_age(name, int(input("Вік: ")))
            except ValueError:
                print("Вік має бути числом")
        elif command == "4":
            add_feature(input("Ім'я: "), input("Характеристика: "))
        elif command == "5":
            delete_by_name(input("Ім'я: "))
        elif command == "6":
            delete_all()
        elif command == "7":
            create_cats()
        elif command == "0":
            break
