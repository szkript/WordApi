import sqlite3
from random import randint

conn = None
DATABASE_NAME = "words.db"


def connect_to_db(dbname):
    global conn
    conn = sqlite3.connect(dbname)
    print("Opened database successfully")


def get_max_num_of_id():
    connect_to_db(DATABASE_NAME)

    cur = conn.cursor()
    cur.execute("select COUNT(id) AS maxId from word_collection")
    result = cur.fetchone()
    conn.close()
    return result[0]


def word_already_used(word_id):
    result = False
    connect_to_db(DATABASE_NAME)

    cur = conn.cursor()
    cur.execute("SELECT word_id, user_id FROM processed WHERE user_id="+str(word_id))
    res = cur.fetchone()
    if res is not None:
        result = True
    return result


def get_word_from_db(word_id):
    connect_to_db(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute("SELECT word, meaning FROM word_collection WHERE id="+str(word_id))
    result = cur.fetchone()
    conn.close()
    return result


def get_daily_word():
    max_len = get_max_num_of_id()
    random_word_id = randint(1, max_len)
    if word_already_used(random_word_id):
        get_daily_word()

    daily_word = get_word_from_db(random_word_id)
    return daily_word


def get_data():
    connect_to_db(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from word_collection")
    rows = cur.fetchall()
    conn.close()
    print("db connection closed")
    return rows
