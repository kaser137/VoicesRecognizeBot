import random
import vk_api as vk
import telegram
import logging
from environs import Env
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog import detect_intent_texts

env = Env()
env.read_env()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, _):
    update.message.reply_text('Здравствуйте')


def answer(update: Update, _):
    text = update.message.text
    session_id = update.message.from_user.id
    answer, _ = detect_intent_texts(session_id=session_id, text=text)
    update.message.reply_text(answer)


def reply(event, vk_api):
    text = event.text
    session_id = event.chat_id
    message, is_fallback = detect_intent_texts(session_id=session_id, text=text)
    if not is_fallback:
        vk_api.messages.send(
            chat_id=event.chat_id,
            message=message,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    bot_token = env('TG_BOT_TOKEN')
    bot = telegram.Bot(bot_token)
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(answer_handler)
    updater.start_polling()

    vk_token = env('VK_TOKEN')
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply(event, vk_api)
