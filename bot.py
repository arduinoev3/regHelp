import os
import logging
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler, CallbackQueryHandler
)

from ai import GigaChatClient

# Загрузка переменных окружения
load_dotenv()
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
# Настройка логов
logging.basicConfig(level=logging.INFO)

client = GigaChatClient()

# Состояния ConversationHandler
WAITING_QUESTION_OR_FILE = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Привет! Задай мне любой вопрос или загрузи pdf и docx файлы"
    )
    return WAITING_QUESTION_OR_FILE

async def load_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Файл pdf был успешно добавлен!"
    )
    return WAITING_QUESTION_OR_FILE

async def load_docx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Файл docx был успешно добавлен!"
    )
    return WAITING_QUESTION_OR_FILE

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    # Получаем ответ от GigaChat
    response = await client.get_answer(user_question)
    answer = response['answer']

    await update.message.reply_text(answer)
    return WAITING_QUESTION_OR_FILE

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"История диалога была успешно сброшена!"
    )
    return WAITING_QUESTION_OR_FILE

async def clear_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
       [InlineKeyboardButton("Да", callback_data='yes')],
       [InlineKeyboardButton("Нет", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы точно хотите удалить все файлы?",
        reply_markup=reply_markup
    )

    return WAITING_QUESTION_OR_FILE

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'yes':
        await query.edit_message_text(text="Файлы были успешно удалены!")
        # Здесь код для удаления файлов
    elif query.data == 'no':
        await query.edit_message_text(text="Удаление отменено!")

def main():
    app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            WAITING_QUESTION_OR_FILE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, answer_question),
                MessageHandler(filters.Document.PDF, load_pdf),
                MessageHandler(filters.Document.DOCX, load_docx)
            ],
        },
        fallbacks=[
            CommandHandler('start', start),
            CommandHandler('reset', reset),
            CommandHandler('clear_files', clear_files)
        ],
    )
    app.add_handler(conv_handler)
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
