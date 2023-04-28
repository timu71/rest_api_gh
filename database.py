import sqlite3
import json
conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE books
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         title           TEXT    NOT NULL,
         year_written            INT     NOT NULL,
         author        TEXT
         );''')

for i in range(30):
    conn.execute("INSERT INTO books ( title, year_written, author) \
        VALUES ('tales' + ?, '1998' + ?, 'Akira' )", (str(i), str(i))); 
db_cursor = db_connection.cursor()


# cursor = conn.execute("SELECT * from books")
# for row in cursor:
#     print(row[0])
#     print(row[1])
#     print(row[2])
#     print(row[3])

# def get_books_db_all(conn):
#     books = []

#     cursor = conn.execute("SELECT * from books")
#     for row in cursor:  
#         print(row[0])
#         print(row[1])
#         print(row[2])
#         print(row[3])
#         book = {'ID' : row[0], 'title' : row[1], 'year_written' : row[2], 'author' : row[3]}
#         books.append(book)
#         print(book)
#     return books
# print(json.dump(get_books_db_all(conn)))
conn.commit()
conn.close()