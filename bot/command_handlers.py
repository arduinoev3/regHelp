from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from shared import CLEAR_FILES, CLEAR_FILES_NO, CLEAR_FILES_YES, WAITING_QUESTION_OR_FILE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text( # Прописать команды
        f"Привет!\nЯ - умный бот, который отвечает по содержанию файлов, которые ты мне пришлёшь.\nЗадай мне любой вопрос или загрузи pdf и docx файлы!"
    )
    return WAITING_QUESTION_OR_FILE

async def clear_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
       [InlineKeyboardButton("Да", callback_data=CLEAR_FILES_YES)],
       [InlineKeyboardButton("Нет", callback_data=CLEAR_FILES_NO)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы точно хотите удалить все файлы?",
        reply_markup=reply_markup
    )
    
    return CLEAR_FILES