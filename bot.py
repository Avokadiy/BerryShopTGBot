from telegram import Update
from telegram.ext import Application, CommandHandler
import logging
import os

# Настройка логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context):
    args = context.args
    if args:
        try:
            phone, code = args[0].split('_')
            await update.message.reply_text(f"Пожалуйста вернитесь на сайт и введите код: {code}")
        except:
            await update.message.reply_text("❌ Неверный формат. Используйте: /start номер_код")
    else:
        await update.message.reply_text("ℹ️ Для получения кода перейдите по ссылке с сайта")

def main():
    # Берем токен из переменных окружения
    token = os.environ.get('BOT_TOKEN')
    if not token:
        logger.error("BOT_TOKEN не установлен!")
        return

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    logger.info("Бот запущен")
    application.run_polling()

if __name__ == "__main__":
    main()