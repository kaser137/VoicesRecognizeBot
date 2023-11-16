import random
import vk_api as vk
import telegram
import logging
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType
from google.api_core.exceptions import RetryError
from google_dialogflow_api import detect_intent_texts, TelegramLogsHandler

logger = logging.getLogger('vk-bot')


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


def main():
    env = Env()
    env.read_env()
    bot_token = env('TG_BOT_TOKEN')
    tg_chat_id = env('TG_CHAT_ID')
    vk_token = env('VK_TOKEN')
    bot = telegram.Bot(bot_token)
    logging.basicConfig(filename='logging.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(bot, tg_chat_id))
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    try:
        longpoll = VkLongPoll(vk_session)
        logger.info('vk_bot start polling')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                reply(event, vk_api=vk_api)
    except RetryError:
        bot.send_message(tg_chat_id, 'while invoking dialogflow was raised exception RetryError')


if __name__ == "__main__":
    main()
