import telegram
import logging
from environs import Env
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from google_dialogflow_api import detect_intent_texts, TelegramLogsHandler

logger = logging.getLogger('tg-bot')


def start(update: Update, _):
    update.message.reply_text('Здравствуйте')


def answer(update: Update, _, project_id, language_code):
    text = update.message.text
    session_id = update.message.from_user.id
    answer, _ = detect_intent_texts(
        project_id,
        session_id=session_id,
        text=text,
        language_code=language_code
    )
    update.message.reply_text(answer)


def main():
    env = Env()
    env.read_env()
    bot_token = env('TG_BOT_TOKEN')
    tg_chat_id = env('TG_CHAT_ID')
    project_id = env('DIALOGFLOW_PROJECT_ID')
    language_code = env('LANGUAGE_CODE', 'ru')
    bot = telegram.Bot(bot_token)
    logging.basicConfig(filename='logging.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(bot, tg_chat_id))
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher
    try:
        start_handler = CommandHandler('start', start)
        answer_handler = MessageHandler(
            Filters.text & (~Filters.command),
            callback=lambda update, _: answer(update, _, project_id, language_code)
        )
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(answer_handler)
        updater.start_polling()
        logger.info('tg_bot start polling')
    except Exception as err:
        logger.error(err, exc_info=True)


if __name__ == '__main__':
    main()
