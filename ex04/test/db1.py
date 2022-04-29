# python -m pip install pymysql

from db import connect as db

insert_sql = "INSERT INTO my_member(username, password) VALUES(%s, %s)"
db.cursor.execute(insert_sql, ["ssar", "1234"])
db.conn.commit()
