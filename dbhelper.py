import sqlite3


def insertdata(sql, data):
    con = sqlite3.connect("testdb.db")
    cursorobj = con.cursor()
    cursorobj.executemany(sql, data)
    con.commit()
    con.close()


def getdata(sql):
    con = sqlite3.connect("testdb.db")
    cursorobj = con.cursor()
    cursorobj.execute(sql)
    rows = cursorobj.fetchall()
    con.close()
    return rows
