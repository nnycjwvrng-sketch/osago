import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
MINI_APP_URL = "https://nnycjwvrng-sketch.github.io/osago/index.html"  # ← сюда вставь ссылку на мини-приложение

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            text="Калькулятор осаго 🚗",
            web_app=WebAppInfo(url=MINI_APP_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = (
        "ОСАГО онлайн за 5 минут.\n"
        "Особые условия для клиентов бота.\n"
        "Рассчитайте и сравните!"
    )

    # Картинку положи в репозиторий с именем welcome.jpg
    with open("IMG_8565.JPG", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()")
MINI_APP_URL = "https://nnycjwvrng-sketch.github.io/osago/index.html"  # ← сюда вставь ссылку на мини-приложение

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            text="Калькулятор осаго 🚗",
            web_app=WebAppInfo(url=MINI_APP_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = (
        "ОСАГО онлайн за 5 минут.\n"
        "Особые условия для клиентов бота.\n"
        "Рассчитайте и сравните!"
    )

    # Картинку положи в репозиторий с именем welcome.jpg
    with open("IMG_8565.JPG", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
