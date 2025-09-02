import sqlite3

connect = sqlite3.connect('Finance.db')
cursor = connect.cursor()

cursor.execute('''
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



Name = input('Название: ')
Sum = int(input('Сумма: '))
Consumer = input('Потребитель: ')
Comment = input('Комментарий: ')
Category = input('Категория: ')
Date = input('Дата: ')
Dates = [Name, Sum, Consumer, Comment, Category, Date]

cursor.execute("INSERT INTO exppenses(Name, Sum, Consumer, Comment, Category, Date) VALUES(?, ?, ?, ?, ?, ?)", (*Dates,))

connect.commit()
connect.close()