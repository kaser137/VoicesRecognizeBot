import random
import vk_api as vk
import telegram
import logging
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow
from google.api_core.exceptions import RetryError

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main(project_id, language_code, vk_api):
    def detect_intent_texts(project_id=project_id, session_id='123456789', text='ока', language_code=language_code):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input},
        )
        return response.query_result.fulfillment_text, response.query_result.intent.is_fallback

    def reply(event, vk_api=vk_api):
        text = event.text
        session_id = event.chat_id
        message, is_fallback = detect_intent_texts(session_id=session_id, text=text)
        if not is_fallback:
            vk_api.messages.send(
                chat_id=event.chat_id,
                message=message,
                random_id=random.randint(1, 1000)
            )

    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply(event, vk_api=vk_api)


if __name__ == "__main__":
    print('vk')
    env = Env()
    env.read_env()
    bot_token = env('TG_BOT_TOKEN')
    tg_chat_id = env('TG_CHAT_ID')
    vk_token = env('VK_TOKEN')
    project_id = env('DIALOGFLOW_PROJECT_ID')
    language_code = env('LANGUAGE_CODE', 'ru')
    bot = telegram.Bot(bot_token)
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    try:
        main(project_id, language_code, vk_api)
    except RetryError:
        bot.send_message(tg_chat_id, 'while invoking dialogflow was raised exception RetryError')
