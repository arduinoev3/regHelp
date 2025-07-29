import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from main_handler import conv_handler
from shared import client

# Загрузка переменных окружения
load_dotenv()
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
# Настройка логов
logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
    app.add_handler(conv_handler)
    app.run_polling()
    client.close()

if __name__ == '__main__':
    main()


await file.download_to_drive(file_path)