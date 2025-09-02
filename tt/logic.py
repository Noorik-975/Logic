import random

import sqlite4

connect = sqlite3.connect("MyDateBase.db")
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS record(
        Player TEXT NOT NULL,
        Best1 INTEGER,
        Best2 INTEGER,
        Best3 INTEGER,
        Best4 INTEGER,
        Best5 INTEGER
    )
""")

connect.commit()
connect.close()


def save_score(Name, New_score):
    connect = sqlite3.connect("MyDateBase.db")
    cursor = connect.cursor()

    cursor.execute(
        "SELECT Best1, Best2, Best3, Best4, Best5 FROM record WHERE Player = ?", (Name,)
    )
    result = cursor.fetchone()

    if result is None:
        scores = [New_score]
        scores.extend([None] * 4)

        cursor.execute(
            "INSERT INTO record (Player, Best1, Best2, Best3, Best4, Best5) VALUES (?, ?, ?, ?, ?, ?)",
            (Name, *scores),
        )

    else:
        scores = [score for score in result if score is not None]
        scores.append(New_score)

        scores = sorted(scores, reverse=True)[:5]
        while len(scores) < 5:
            scores.append(None)

        cursor.execute(
            """
            UPDATE record
            SET Best1 = ?, Best2 = ?, Best3 = ?, Best4 = ?, Best5 = ?
            WHERE Player = ?
            """,
            (*scores, Name),
        )

    connect.commit()
    connect.close()


imya = input("Your name: ")
points = 0
for i in range(10):
    z = random.randint(1, 99)
    g = random.randint(z + 1, 100)
    print(f"{z}/{g}\nСколько это в процентах?")
    ansver = float(input("Ваш ответ:"))
    res = int(1000 / (1 + abs(ansver - z / g * 100)))
    points += res
    print(f"Правильный ответ: {round(z / g * 100, 2)}\nВы получили {res} балла.")

print("Ваш счет: ", points)

save_score(imya, points)
