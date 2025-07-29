from server.server import GigaChatClient


client = GigaChatClient()

# Состояния ConversationHandler
WAITING_QUESTION_OR_FILE, CLEAR_FILES = range(2)

# Callback-data для clear_files
CLEAR_FILES_YES = 'clear_files_yes'
CLEAR_FILES_NO = 'clear_files_no'