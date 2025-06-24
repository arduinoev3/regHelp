import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler
)

from ai import GigaChatClient

# Загрузка переменных окружения
load_dotenv()
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
# Настройка логов
logging.basicConfig(level=logging.INFO)

client = GigaChatClient()

# Состояния ConversationHandler
WAITING_QUESTION = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # При старте или сбросе очищаем историю
    context.user_data['history'] = []
    await update.message.reply_text(
        f"Привет! Задай мне любой вопрос по менеджменту. Я буду помнить контекст до команды /reset"
    )
    return WAITING_QUESTION

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    # Получаем ответ от GigaChat
    response = await client.get_answer(user_question)
    answer = response['answer']

    await update.message.reply_text(answer)
    return WAITING_QUESTION

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['history'] = []
    await update.message.reply_text(
        "Контекст сброшен. Можешь задать новый вопрос.",
        reply_markup=ReplyKeyboardRemove()
    )
    return WAITING_QUESTION

def main():
    app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            WAITING_QUESTION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, answer_question)
            ],
        },
        fallbacks=[
            CommandHandler('reset', reset),
            CommandHandler('start', start)
        ],
    )
    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == '__main__':
    main()
