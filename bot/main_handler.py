from telegram.ext import (
    CommandHandler, MessageHandler, filters,
    ConversationHandler, CallbackQueryHandler
)

from callback_handlers import clear_files_handler
from message_handlers import answer_question, load_file
from command_handlers import clear_files, start
from shared import CLEAR_FILES, WAITING_QUESTION_OR_FILE

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        WAITING_QUESTION_OR_FILE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, answer_question),
            MessageHandler(filters.Document.PDF, load_file),
            MessageHandler(filters.Document.DOCX, load_file),
        ],
        CLEAR_FILES: [
            CallbackQueryHandler(clear_files_handler)
        ]
    },
    fallbacks=[
        CommandHandler('start', start),
        CommandHandler('clear_files', clear_files)
    ],
)