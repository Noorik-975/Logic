`.gitignore` - название файлов, которые не затрагиваются GIT 
- `*.log` - ignore all `.log` files
- `node_modules/` - ignore files in dir

`git remote set-url origin git@github.com:UrikUp/Repo.git`
`git remote add origin git@github.com:UrikUp/SimulatorForFriends.git`

 # 💡 Git + GitHub Шпаргалка


## 🔧 Настройка Git (один раз)
```bash
git config --global user.name "Твоё Имя"
git config --global user.email "you@example.com"
```

## 📁 Работа с репозиторием
| Действие           | Команда                                                      |
| ------------------ | ------------------------------------------------------------ |
| Клонировать репо   | `git clone https://github.com/user/repo.git`                 |
| Инициализировать   | `git init`                                                   |
| Проверить статус   | `git status`                                                 |
| Добавить файл      | `git add файл` или `git add .` (всё)                         |
| Зафиксировать      | `git commit -m "Комментарий"`                                |
| Отправить в GitHub | `git push` (если первая отправка: `git push -u origin main`) |
| Получить изменения | `git pull`                                                   |
| Посмотреть логи    | `git log` (или `git log --oneline`)                          |
| Отмена изменений   | `git checkout -- файл`                                       |
| Удалить файл       | `git rm файл` → `git commit`                                 |

## 🌿 Ветки (branches)
| Действие                  | Команда                              |
| ------------------------- | ------------------------------------ |
| Посмотреть ветки          | `git branch`                         |
| Создать ветку             | `git branch имя-ветки`               |
| Переключиться             | `git checkout имя-ветки`             |
| Создать и переключиться   | `git checkout -b имя-ветки`          |
| Отправить ветку           | `git push -u origin имя-ветки`       |
| Удалить ветку (локально)  | `git branch -d имя-ветки`            |
| Удалить ветку (на GitHub) | `git push origin --delete имя-ветки` |

## 🔄 Слияние (merge) и конфликты
| Действие             | Команда                                  |
| -------------------- | ---------------------------------------- |
| Переключиться в main | `git checkout main`                      |
| Объединить ветку     | `git merge имя-ветки`                    |
| Разрешить конфликт   | Правим файл → `git add .` → `git commit` |

## 📦 Работа с удалёнными репозиториями
| Действие           | Команда                                                  |
| ------------------ | -------------------------------------------------------- |
| Добавить origin    | `git remote add origin https://github.com/user/repo.git` |
| Посмотреть remotes | `git remote -v`                                          |
| Изменить ссылку    | `git remote set-url origin новая_ссылка`                 |

## 👨‍💻 Совместная работа
| Действие                  | Команда                                                |
| ------------------------- | ------------------------------------------------------ |
| Форк репозитория          | На GitHub: нажми "Fork"                                |
| Склонировать форк         | `git clone https://github.com/you/forked-repo.git`     |
| Создать новую ветку       | `git checkout -b feature-name`                         |
| Отправить ветку           | `git push -u origin feature-name`                      |
| Сделать Pull Request      | На GitHub → кнопка "New Pull Request"                  |
| Обновить форк с оригинала | добавить `upstream` и сделать `git pull upstream main` |

### Пример обновления форка:
```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main
```

- git rebase - ветка базируется на самой новой версии ветки.
  Где запускаешь, там и меняется. Если на feature, то feature берет с master. Если на master, то ветка продолжает ветку.
- git merge - слияет все ветки в одно (messy)
- git squash - соберает всю ветку в одно, а потом продолжает main
> Чаще используют squash, чтобы не засорять историю.
