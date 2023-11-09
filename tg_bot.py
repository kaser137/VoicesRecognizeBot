import telegram
import logging
from environs import Env
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from google.api_core.exceptions import RetryError
from google_dialogflow_api import detect_intent_texts

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, _):
    update.message.reply_text('Здравствуйте')


def answer(update: Update, _):
    text = update.message.text
    session_id = update.message.from_user.id
    answer, _ = detect_intent_texts(project_id, session_id=session_id, text=text, language_code=language_code)
    update.message.reply_text(answer)


def main():
    try:
        updater = Updater(token=bot_token)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(answer_handler)
        updater.start_polling()
    except RetryError:
        bot.send_message(tg_chat_id, 'while invoking dialogflow was raised exception RetryError')


if __name__ == "__main__":
    env = Env()
    env.read_env()
    bot_token = env('TG_BOT_TOKEN')
    tg_chat_id = env('TG_CHAT_ID')
    project_id = env('DIALOGFLOW_PROJECT_ID')
    language_code = env('LANGUAGE_CODE', 'ru')
    bot = telegram.Bot(bot_token)
    main()

