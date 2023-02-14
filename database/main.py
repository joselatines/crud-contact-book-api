import sqlite3

tables = {"contacts": "Contacts"}


def get_db():
    db = sqlite3.connect("database/my_db.db")
    return db


def query_db(query, args=(), commit=False, one=False):
    print(f"📚: {query}")
    connection = get_db()
    cursor = connection.execute(query, args)

    # commit the transaction if specified
    if commit:
        connection.commit()

    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv
