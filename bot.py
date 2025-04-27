from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
load_dotenv()

# أخذ التوكن من متغير البيئة
TOKEN = os.getenv('BOT_TOKEN')
# أمر بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('أهلاً! أنا بوت بسيط ✨')

# الرد على أي رسالة
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main():
    # ضع توكن البوت الخاص بك هنا
    TOKEN = '8174177417:AAF-ndZWBfJmwtYHJYHV4gnYhgGk0qdSiHw'
    
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("البوت شغال...")
    app.run_polling()

if __name__ == '__main__':
    main()
