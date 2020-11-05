from contextlib import closing
import sqlite3

DATABASE = "rdbms/mbr.db"

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with closing(connect_db()) as db:
        with open('rdbms/sql/0.DROP_TABLES.sql', encoding='UTF8') as f:
            db.cursor().executescript(f.read())
        db.commit()
        
        with open('rdbms/sql/1.CREATE_TABLES.sql', encoding='UTF8') as f:
            db.cursor().executescript(f.read())
        db.commit()

    db.close()

def excute_sql(sql):
    with closing(connect_db()) as db:
        db.cursor().executescript(sql)
        db.commit()

    db.close()

def checkID(id):
    print("CHECK ID")
    if(id != None):
    with closing(connect_db()) as db:
        cur = db.cursor().execute("select MBR_ID, TALK from MBR_INFO where MBR_ID ='{ID}'".format(ID=id.strip()))
        row = cur.fetchall()
        
        print("!@#!@# row : ", row)
        print("!@#!@# id : ", id)
        if len(row) > 0:
            id = row[0][0]
        else:
            id = None
        
        db.close()
        print("id : ", id)
        if id == None:
            return (False, '')
        else :
            talk = row[0][1]
            return (True, talk)

def selectAll():
    print("select MBR info")
    try:
        with closing(connect_db()) as db:
            cur = db.cursor().execute("select MBR_ID, TALK, COIN, PURCHASE, DEPOSIT, SALE, WITHDRAW, RESERVE, \
                TOTAL_PUR, TOTAL_SAL, REVENUE, RATING, WALLET from MBR_INFO order by TALK")
            row = cur.fetchall()

            return row
        
    except:
        init_db()
        return False

def selectMBR(id):
    print("select MBR info : ", id)
    with closing(connect_db()) as db:
        cur = db.cursor().execute("select MBR_ID, TALK, COIN, PURCHASE, DEPOSIT, SALE, WITHDRAW, RESERVE, \
            TOTAL_PUR, TOTAL_SAL, REVENUE, RATING, WALLET from MBR_INFO where MBR_ID ='{ID}'".format(ID=id.strip()))
        row = cur.fetchall()

        return row[0]

def deleteMBR(id):
    print("delete MBR info")
    with closing(connect_db()) as db:
        cur = db.cursor().execute("delete from MBR_INFO where MBR_ID ='{ID}'".format(ID=id))
        cur.fetchall()
        db.commit()

def selectTalk():
    print("select Talk")
    with closing(connect_db()) as db:
        cur = db.cursor().execute("SELECT DISTINCT TALK from MBR_INFO")
        row = cur.fetchall()

        return row