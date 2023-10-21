import telegram
import logging
from environs import Env
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from dialog import detect_intent_texts

env = Env()
env.read_env()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
bot_token = env('TG_BOT_TOKEN')
bot = telegram.Bot(bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def start(update: Update, _):
    update.message.reply_text('Здравствуйте')


def answer(update: Update, _):
    text = update.message.text
    session_id = update.message.from_user.id
    answer = detect_intent_texts(session_id=session_id, text=text)
    update.message.reply_text(answer)


start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)


updater.start_polling()
