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
Описание содержимого:
`
* TG_BOT_TOKEN = Токен для доступа и управления ботом в Телеграм
* TG_CHAT_ID = Ваш ID в Телеграм
* GOOGLE_APPLICATION_CREDENTIALS = полный путь к файлу с идентификационными данными [credentials.json](https://cloud.google.com/dialogflow/es/docs/quick/setup#sdk)
* VK_TOKEN = Токен для доступа и управления ботом в ВК

6. Запустить программу:
```bash
python3 tg_vk_bot.py
```

7. Примеры рабочих ботов:
Телеграм: https://t.me/VoicesRecognizeBot
ВК: https://vk.me/join/AJQ1d4B1FSp5TUCFT4WmQyFW