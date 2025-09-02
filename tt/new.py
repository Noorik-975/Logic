import pygame
import random
import sqlite3
import sys

# ---------- Настройки ----------
WIDTH, HEIGHT = 800, 600
FPS = 30
FONT_SIZE = 36

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Математическая игра")
font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()

# ---------- База данных ----------
def save_score(Name, New_score):
    connect = sqlite3.connect('MyDateBase.db')
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS record(
            Player TEXT NOT NULL,
            Best1 INTEGER,
            Best2 INTEGER,
            Best3 INTEGER,
            Best4 INTEGER,
            Best5 INTEGER
        )
    ''')
    cursor.execute('SELECT Best1, Best2, Best3, Best4, Best5 FROM record WHERE Player = ?', (Name,))
    result = cursor.fetchone()

    if result is None:
        scores = [New_score]
        scores.extend([None] * 4)
        cursor.execute('INSERT INTO record (Player, Best1, Best2, Best3, Best4, Best5) VALUES (?, ?, ?, ?, ?, ?)', (Name, *scores))
    else:
        scores = [score for score in result if score is not None]
        scores.append(New_score)
        scores = sorted(scores, reverse=True)[:5]
        while len(scores) < 5:
            scores.append(None)
        cursor.execute('''
            UPDATE record
            SET Best1 = ?, Best2 = ?, Best3 = ?, Best4 = ?, Best5 = ?
            WHERE Player = ?
        ''', (*scores, Name))
    connect.commit()
    connect.close()

# ---------- Игровая функция ----------
def game(player_name):
    points = 0
    question_num = 1
    user_input = ""
    
    z, g = random.randint(1, 99), 0
    while g <= z:
        g = random.randint(2, 100)

    running = True
    while running:
        screen.fill((30, 30, 30))
        
        # Текст вопроса
        question_text = font.render(f"Вопрос {question_num}/10", True, (255, 255, 255))
        frac_text = font.render(f"{z}/{g}  Сколько это в % ?", True, (255, 255, 0))
        answer_text = font.render(f"Ваш ответ: {user_input}", True, (0, 255, 0))

        screen.blit(question_text, (WIDTH//2 - question_text.get_width()//2, 50))
        screen.blit(frac_text, (WIDTH//2 - frac_text.get_width()//2, 150))
        screen.blit(answer_text, (WIDTH//2 - answer_text.get_width()//2, 250))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.strip():
                        try:
                            ans = float(user_input)
                            res = int(1000 / (1 + abs(ans - z / g * 100)))
                            points += res
                            question_num += 1

                            if question_num > 10:
                                save_score(player_name, points)
                                return points
                            else:
                                user_input = ""
                                z, g = random.randint(1, 99), 0
                                while g <= z:
                                    g = random.randint(2, 100)
                        except ValueError:
                            user_input = ""  # если ввели не число
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isdigit() or event.unicode == ".":
                    user_input += event.unicode
        
        clock.tick(FPS)

# ---------- Экран приветствия ----------
def start_screen():
    name = ""
    while True:
        screen.fill((0, 0, 50))
        title = font.render("Математическая игра", True, (255, 255, 255))
        name_text = font.render(f"Введите имя: {name}", True, (255, 255, 0))
        info = font.render("Нажмите Enter для начала", True, (200, 200, 200))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        screen.blit(name_text, (WIDTH//2 - name_text.get_width()//2, 300))
        screen.blit(info, (WIDTH//2 - info.get_width()//2, 400))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isalnum():
                    name += event.unicode

# ---------- Экран окончания ----------
def end_screen(score):
    while True:
        screen.fill((50, 0, 0))
        text1 = font.render(f"Игра окончена! Ваш счет: {score}", True, (255, 255, 255))
        text2 = font.render("Нажмите ESC для выхода", True, (255, 255, 0))
        screen.blit(text1, (WIDTH//2 - text1.get_width()//2, 200))
        screen.blit(text2, (WIDTH//2 - text2.get_width()//2, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

# ---------- Запуск игры ----------
player = start_screen()
final_score = game(player)
end_screen(final_score)
