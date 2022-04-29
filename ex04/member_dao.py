# dao(data access object)

from db import connect as db


# insert_one(username="ssar", password="1234")
def insert_one(**data):  # {"username":"ssar", "password":"1234"}
    sql = "INSERT INTO my_member(username, password) VALUES(%(username)s, %(password)s)"
    try:
        db.cursor.execute(sql, data)  # 자동으로 딱딱맞춰서 바인딩됨
    except Exception as e:
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def select_all():
    sql = "SELECT * FROM my_member"
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()
    return rows


def select_one(**data):
    sql = "SELECT * FROM my_member where id = %(id)s"
    db.cursor.execute(sql, data)
    row = db.cursor.fetchone()
    return row


def update_one(**data):
    sql = "UPDATE my_member SET username=%(username)s, password=%(password)s WHERE id=%(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def delete_one(**data):
    sql = "DELETE FROM my_member WHERE id = %(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1
