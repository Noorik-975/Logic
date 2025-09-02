import sqlite3

connect = sqlite3.connect('MyDateBase.db')
cur = connect.cursor()

cur.execute('SELECT * FROM record')
x = cur.fetchall()

for i in x:
    print(i)

connect.commit()
connect.close()