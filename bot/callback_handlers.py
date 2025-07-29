from telegram import Update
from telegram.ext import ContextTypes
from shared import CLEAR_FILES_NO, CLEAR_FILES_YES, client, WAITING_QUESTION_OR_FILE


async def clear_files_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('In button handler')
    query = update.callback_query
    await query.answer()
    print('In button handler', query.data)
    if query.data == CLEAR_FILES_YES:
        client.delete_index('db') # Изменить на актуальный id пространства
        await query.edit_message_text(text="Файлы были успешно удалены!")
    elif query.data == CLEAR_FILES_NO:
        await query.edit_message_text(text="Удаление отменено!")

    return WAITING_QUESTION_OR_FILE