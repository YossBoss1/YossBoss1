from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "YossBoss bot system is ready!"}
rom fastapi import FastAPI, Request
import uvicorn
import requests
import os

app = FastAPI()

BOT_TOKEN = "הכנס_כאן_את_הטוקן_שלך"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def read_root():
    return {"message": "YossBoss bot system is ready!"}

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if chat_id and text:
        response_text = "הבוט שלך חי ובועט 💥"
        send_message(chat_id, response_text)

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if _name_ == "_main_":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
