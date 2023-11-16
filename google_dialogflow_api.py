import logging
from google.cloud import dialogflow
from environs import Env


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def detect_intent_texts(session_id='123456789', text='ока'):
    env = Env()
    env.read_env()
    project_id = env('DIALOGFLOW_PROJECT_ID')
    language_code = env('LANGUAGE_CODE', 'ru')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input},
    )
    return response.query_result.fulfillment_text, response.query_result.intent.is_fallback
