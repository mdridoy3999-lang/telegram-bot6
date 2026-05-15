from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "8907472855:AAEfLZdmfBMEbxE8Vv2jN1bGUOZgPt8Uf5k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot Online")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pair = random.choice([
        "BTC/USD",
        "EUR/USD",
        "GBP/USD"
    ])

    direction = random.choice([
        "📈 UP",
        "📉 DOWN"
    ])

    msg = f"""
🔥 SIGNAL

{pair} 2M
{direction}
"""

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot Running...")
app.run_polling()
