import telegram
import logging
from environs import Env
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

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


def echo(update: Update, _):
    update.message.reply_text(update.message.text)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)


updater.start_polling()
