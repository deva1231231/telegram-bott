import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8688177518:AAGTlUdXZQf1l_iYykz7ZpW9R27FA9jyBII")

answers = {
    "q1": "Shrishti (obviously 😌)",
    "q2": "Shrishti — best smile award goes here",
    "q3": "Shrishti makes everything better instantly",
    "q4": "Shrishti 😎 (no debate allowed)",
    "q5": "Shrishti… go talk to her 👀"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
Welcome 😄

/q1 - Most beautiful girl?
/q2 - Best smile?
/q3 - Who makes your day better?
/q4 - Coolest person?
/q5 - Who should you talk to?
"""
    await update.message.reply_text(text)

async def q1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(answers["q1"])

async def q2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(answers["q2"])

async def q3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(answers["q3"])

async def q4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(answers["q4"])

async def q5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(answers["q5"])

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("q1", q1))
app.add_handler(CommandHandler("q2", q2))
app.add_handler(CommandHandler("q3", q3))
app.add_handler(CommandHandler("q4", q4))
app.add_handler(CommandHandler("q5", q5))

app.run_polling()
