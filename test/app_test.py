# app-test.py

import sqlite3

def test_get_book_db_by_id():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT * from books where id = %s" % 1)
    books = []

    for i, row in enumerate(cursor):  

        book = {'ID' : row[0], 'title' : row[1], 'year_written' : row[2], 'author' : row[3]}
        books.append(book)
    assert row[0] == i 