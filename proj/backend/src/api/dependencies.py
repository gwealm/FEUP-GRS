from .db import Database

db = Database()


def get_db():
    return db
