import os
import logging
from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.ext import Dispatcher

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = FastAPI()
application = Application.builder().token(TOKEN).build()

# פקודה התחלתית
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הבוט של יוסי מוכן לפעולה 🔥")

# כל הודעה אחרת
async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("קיבלתי אותך 🔥")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))

@app.post("/")
async def handle_update(request: Request):
    json_data = await request.json()
    update = Update.de_json(json_data, bot)
    await application.process_update(update)
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "YossBoss bot system is ready!"}
