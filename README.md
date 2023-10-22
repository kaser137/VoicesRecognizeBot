# VoicesRecognize


## Цели проекта
Создать бот для Телеграма и для ВК, которые будут взаимодействовать с Google Dialogflow

## Как установить и запустить проект

1. Склонировать репозиторий.
2. Создать виртуальное окружение.
```bash
python -m venv env
```
3. Активировать виртуальное окружение:

```bash
. env/bin/activate
```
   
4. Установить зависимости:
```bash
pip install -r requirements.txt
```

5. Создать файл `.env` в рабочей директории.

* TG_BOT_TOKEN = Токен для доступа и управления ботом в Телеграм
* TG_CHAT_ID = Ваш ID в Телеграм
* GOOGLE_APPLICATION_CREDENTIALS = полный путь к файлу с идентификационными данными [credentials.json](https://cloud.google.com/dialogflow/es/docs/quick/setup#sdk)
* VK_TOKEN = Токен для доступа и управления ботом в ВК

6. Запустить программу:
```bash
python3 tg_vk_bot.py
```

![video](https://github.com/kaser137/VoicesRecognizeBot/assets/107580630/7e1d7d30-cd94-4b75-9878-268c7047362b)


7. Примеры рабочих ботов:
* Телеграм: https://t.me/VoicesRecognizeBot
* ВК: https://vk.me/join/AJQ1d4B1FSp5TUCFT4WmQyFW

* иии
[Запись экрана от 22.10.2023 04:10:20.webm](..%2F..%2F%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%2F%D0%97%D0%B0%D0%BF%D0%B8%D1%81%D0%B8%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%2F%D0%97%D0%B0%D0%BF%D0%B8%D1%81%D1%8C%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%2022.10.2023%2004%3A10%3A20.webm)
