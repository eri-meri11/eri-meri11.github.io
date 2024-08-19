from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text('Welcome! Connect your crypto wallet and start mining.')

if __name__ == '__main__':
    app = ApplicationBuilder().token('7306348951:AAFHoBEcpu_bJ2ig4uAuepvdvB-JoK-SA4g').build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
