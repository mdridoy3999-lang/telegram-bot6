from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "8907472855:AAEfLZdmfBMEbxE8Vv2jN1bGUOZgPt8Uf5k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Running ✅")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    rsi = random.randint(10, 90)

    pair = random.choice([
        pairs = [

    # OTC PAIRS
    "EUR/USD OTC",
    "GBP/USD OTC",
    "USD/JPY OTC",
    "USD/CAD OTC",
    "AUD/USD OTC",
    "NZD/USD OTC",

    "EUR/JPY OTC",
    "GBP/JPY OTC",
    "AUD/JPY OTC",
    "CAD/JPY OTC",

    "EUR/GBP OTC",
    "EUR/CAD OTC",
    "EUR/AUD OTC",

    "GBP/CAD OTC",
    "GBP/AUD OTC",

    "AUD/CAD OTC",
    "AUD/NZD OTC",

    "NZD/CAD OTC",
    "NZD/JPY OTC",

    "USD/CHF OTC",
    "EUR/CHF OTC",
    "GBP/CHF OTC",

    "CHF/JPY OTC"
]
    ])

    if rsi < 30:
        direction = "📈 UP"

    elif rsi > 70:
        direction = "📉 DOWN"

    else:
        direction = random.choice([
            "📈 UP",
            "📉 DOWN"
        ])

    msg = f"""
🔥 SIGNAL

{pair} 15s
{direction}
"""

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot Running...")
app.run_polling()
