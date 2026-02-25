import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔑 Apna Bot Token Yahan Paste Karna
TOKEN = "8767739250:AAEaL1fvmN9A_W0aouLesfUcBK6CEYYiYgk"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome!\nMovie ya series ka naam likho, main link bhej dunga."
    )

# Movie Search Logic (Demo)
async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()

    movie_db = {
        "avatar": "https://t.me/yourchannel/avatar",
        "kgf": "https://t.me/yourchannel/kgf",
        "pushpa": "https://t.me/yourchannel/pushpa"
    }

    if query in movie_db:
        await update.message.reply_text(
            f"✅ Found!\nWatch here:\n{movie_db[query]}"
        )
    else:
        await update.message.reply_text(
            "❌ Movie not found.\nAdmin se request karo."
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
