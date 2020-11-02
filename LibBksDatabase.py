import sqlite3
#BACKEND

def ConnectData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, MTy text, Ref text, Title text,\
                       Fna text, Sna text, Adr1 text, Adr2 text, Pcd text, MNo text, BkID text, BkT text, Atr text, \
                       DBo text, Ddu text, sPr text, Lrf text, Dod text, DonL text)''')
    con.commit()
    con.close()


def addDataRec(MTy, Ref, Title,Fna, Sna, Adr1, Adr2, Pcd, MNo, BkID, BkT, Atr, DBo , Ddu, sPr, Lrf, Dod, DonL):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO libbooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (MTy, Ref, Title, Fna, Sna, Adr1, Adr2, Pcd, MNo, BkID, BkT, Atr, DBo, Ddu, sPr, Lrf, Dod, DonL))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("DELETE FROM libbooks WHERE ID=?", (id,))
    con.commit()
    con.close()


def searchData(MTy="", Ref="", Title="", Fna="", Sna="", Adr1="", Adr2="", Pcd="", MNo="", BkID="", BkT="", Atr="", \
               DBo="", Ddu="", sPr="", Lrf="", Dod="", DonL=""):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks WHERE MTy=? OR Ref=? OR Title=? OR Fna=? OR Sna=? OR Adr1=? OR Adr2=? OR Pcd=? \
                 OR MNo=? OR BkID=? OR BkT=? OR Atr=? OR DBo=? OR Ddu=? OR sPr=? OR Lrf=? OR Dod=? OR DonL=?",
                (MTy, Ref, Title, Fna, Sna, Adr1, Adr2, Pcd, MNo, BkID, BkT, Atr, DBo, Ddu, sPr, Lrf, Dod, DonL))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, MTy="", Ref="", Title="", Fna="", Sna="", Adr1="", Adr2="", Pcd="", MNo="", BkID="", BkT="", Atr="",
               DBo="", Ddu="", sPr="", Lrf="", Dod="", DonL=""):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("UPDATE libbooks SET MTy=?, Ref=?, Title=?, Fna=?, Sna=?, Adr1=?, Adr2=?, Pcd=?,MNo=?, BkID=?, \
                 BkT=?, Atr=?, DBo=?, Ddu=?, sPr=?, Lrf=?, Dod=?, DonL=? WHERE id=?",
                (MTy, Ref, Title, Fna, Sna, Adr1, Adr2, Pcd, MNo, BkID, BkT, Atr, DBo, Ddu, sPr, Lrf, Dod, DonL, id))
    con.commit()
    con.close()

ConnectData()
