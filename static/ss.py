from sqlite3 import *
with connect('aneki.db') as db:
    c=db.cursor()
    c.execute("INSERT INTO storage(text,likes,dis) VALUES(?,?,?)",('''— Изя, я слышал, твоя тёща умерла. А что у нее было?
— Да так, ерунда – старый сервант и телевизор''',0,0))
    db.commit()
