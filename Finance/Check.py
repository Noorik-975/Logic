import sqlite3

connect = sqlite3.connect('Finance.db')
cur = connect.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS exppenses(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(20),
        Sum INTEGER,
        Consumer VARCHAR(25),
        Comment VARCHAR(200),
        Category TEXT,
        Date TEXT
    )
''')


cur.execute('SELECT * FROM exppenses')
result = cur.fetchall()

for i in result:
    print(i)






connect.commit()
connect.close()
