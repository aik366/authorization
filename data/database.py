import sqlite3 as sq


def db_start():
    # Устанавливаем соединение с базой данных
    connection = sq.connect('user.db')
    cur = connection.cursor()

    # Создаем таблицу
    cur.execute("""CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT,
                    password TEXT)""")

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def db_insert(login, password):
    # Устанавливаем соединение с базой данных
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    # Проверяем, существует ли уже запись с таким же названием
    if not cur.execute("SELECT * FROM user WHERE login = ?", (login,)).fetchone():
        cur.execute(
            f"INSERT INTO user (login, password) VALUES (?, ?)",
            (login, password))

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
        return True

    connection.close()
    return False


def db_check(login, password):
    # Устанавливаем соединение с базой данных
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    # Проверяем, существует ли уже запись с таким же названием
    if cur.execute("SELECT * FROM user WHERE login = ? AND password = ?", (login, password)).fetchone():
        connection.close()
        return True
    connection.close()
    return False


def login_exist(login):
    # Устанавливаем соединение с базой данных
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    # Проверяем, существует ли уже запись с таким же названием
    if cur.execute("SELECT * FROM user WHERE login = ?", (login,)).fetchone():
        connection.close()
        return True
    connection.close()
    return False


def db_select():
    connection = sq.connect('user.db')
    cur = connection.cursor()

    users = cur.execute("SELECT * FROM user").fetchall()

    connection.close()
    return users


if __name__ == '__main__':
    db_start()
    # print(db_insert("admin1234", "12345678"))
    # print(login_exist("admin"))
    print(db_select())
