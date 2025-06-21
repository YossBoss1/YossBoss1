from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "7440166734:AAGu2xCPp2690WuU8levE31lQHEDfCi6kck"

@app.get("/")
def root():
    return {"message": "YossBoss bot system is ready!"}

@app.post("/")
async def receive_update(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        response_text = "👑 ברוך הבא ליוסבוס!"
        send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(send_url, json={"chat_id": chat_id, "text": response_text})
    
    return {"ok": True}
