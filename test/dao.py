import connect


def insert_all(**data):
    sql = "INSERT INTO seoulair(msrdt, msrrgn_nm, msrste_nm, pm10, pm25, o3, no2, co, so2, idex_nm, idex_mvl, arplt_main) VALUES(%(MSRDT)s, %(MSRRGN_NM)s, %(MSRSTE_NM)s, %(PM10)s,%(PM25)s,%(O3)s,%(NO2)s,%(CO)s,%(SO2)s,%(IDEX_NM)s, %(IDEX_MVL)s,%(ARPLT_MAIN)s )"
    try:
        connect.cursor.execute(sql, data)
    except Exception as e:
        connect.conn.rollback()
        return -1
    connect.conn.commit()
    return 1
