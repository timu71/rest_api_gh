
import pymysql.cursors

db_charset = 'utf8mb4'


db_connection = pymysql.connect(
host  = 'database-books.cp0xsjmsqygl.eu-central-1.rds.amazonaws.com',
user='admin', 
password='******', 
database = 'database-books',
charset=db_charset,
cursorclass=pymysql.cursors.DictCursor
)


db_connection.execute('''CREATE TABLE books
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         title           TEXT    NOT NULL,
         year_written            INT     NOT NULL,
         author        TEXT
         );''')

db_cursor = db_connection.cursor()
for i in range(30):
    db_cursor.execute("INSERT INTO books ( title, year_written, author) \
        VALUES ('tales' + ?, '1998' + ?, 'Akira' )", (str(i), str(i))); 