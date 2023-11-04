import random
import telegram
import logging
from environs import Env
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from google.cloud import dialogflow
from google.api_core.exceptions import RetryError

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main(project_id, language_code, bot_token):
    def detect_intent_texts(project_id=project_id, session_id='123456789', text='ока', language_code=language_code):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input},
        )
        return response.query_result.fulfillment_text, response.query_result.intent.is_fallback

    def start(update: Update, _):
        update.message.reply_text('Здравствуйте')

    def answer(update: Update, _):
        text = update.message.text
        session_id = update.message.from_user.id
        answer, _ = detect_intent_texts(session_id=session_id, text=text)
        update.message.reply_text(answer)

    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(answer_handler)
    updater.start_polling()


if __name__ == "__main__":
    print('tg')
    env = Env()
    env.read_env()
    bot_token = env('TG_BOT_TOKEN')
    tg_chat_id = env('TG_CHAT_ID')
    project_id = env('DIALOGFLOW_PROJECT_ID')
    language_code = env('LANGUAGE_CODE', 'ru')
    print(language_code)
    bot = telegram.Bot(bot_token)
    try:
        main(project_id, language_code, bot_token)
    except RetryError:
        bot.send_message(tg_chat_id, 'while invoking dialogflow was raised exception RetryError')
