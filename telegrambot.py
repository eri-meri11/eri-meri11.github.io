from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# /app komutu tetiklendiğinde çalışacak fonksiyon
def app(update: Update, context: CallbackContext) -> None:
    # Düğme oluşturma
    keyboard = [
        [InlineKeyboardButton("Click To Start the App", url="https://eri-meri11.github.io/")]
    ]

    # Düğme yerleşimi
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Mesaj gönderme
    update.message.reply_text("Waste time on clicking on buttons? Nah! Just leave your phone AFK and see your earnings.", reply_markup=reply_markup)

def main():
    # API tokeninizi buraya girin
    updater = Updater("7306348951:AAFHoBEcpu_bJ2ig4uAuepvdvB-JoK-SA4g", use_context=True)

    dp = updater.dispatcher

    # /app komutunu ekleyin
    dp.add_handler(CommandHandler("app", app))

    # Botu başlat
    updater.start_polling()

    # Botun sürekli çalışmasını sağla
    updater.idle()

if __name__ == '__main__':
    main()
