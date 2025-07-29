from telegram import Update
from telegram.ext import ContextTypes

from shared import WAITING_QUESTION_OR_FILE, client
from files.transfer_file_to_embeddings import transfer_file_to_embeddings

async def load_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    file = await context.bot.get_file(document.file_id)
    file_path = f"{document.file_name}"
    await transfer_file_to_embeddings(file=file, file_path=file_path)
    await update.message.reply_text(
        f"Файл {file_path} был успешно добавлен!"
    )
    return WAITING_QUESTION_OR_FILE

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    # Получаем ответ от GigaChat
    answer = await client.get_answer(user_question)
    await update.message.reply_text(answer)
    return WAITING_QUESTION_OR_FILE

