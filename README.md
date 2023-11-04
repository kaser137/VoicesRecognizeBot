# VoicesRecognize

## Цели проекта
Создать бот для Телеграма и для ВК, которые будут взаимодействовать с [Google](https://www.google.com/) [DialogFlow.](https://dialogflow.cloud.google.com/)

## Как установить и запустить проект

1. Склонировать репозиторий.
2. Создать виртуальное окружение в директории проекта:
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

5. Создать файл `.env` в рабочей директории

* TG_BOT_TOKEN = Токен для доступа и управления ботом в Телеграм
* TG_CHAT_ID = Ваш ID в Телеграм
* GOOGLE_APPLICATION_CREDENTIALS = полный путь к файлу с идентификационными данными [credentials.json](https://cloud.google.com/dialogflow/es/docs/quick/setup#sdk)
* VK_TOKEN = Токен для доступа и управления ботом в ВК
* DIALOGFLOW_PROJECT_ID = id Google проекта в DialogFlow
* LANGUAGE_CODE = код языка на котором будут отвечать боты (по умолчанию - русский) 

6. Запустить программу:  

телеграм-бот:
```bash
python3 tg_bot.py
```
вк-бот:
```bash
python3 vk_bot.py
```
оба бота:
```bash
python3 both_bots.py
```

7. Для тренировки программы DialogFlow и создания intents (смыслов разговора):
```bash
python3 create_intent.py --intent full_path
```
где full_path полный путь (с названием) к json файлу с данными intents, которые нужно создать
(по умолчанию прописан файл в репозитории questions.json).  
пример содержания файла:
```json
{
  "Погода": {
    "questions": [
      "Какая погода?",
      "Солнечно?",
      "Холодно?",
      "Что одеть?"
    ],
    "answer": "Для погодных условий обратитесь на сайт https://www.wunderground.com"
  }
}
```


8. Примеры рабочих ботов:
* Телеграм: https://t.me/VoicesRecognizeBot
* ВК: https://vk.me/join/AJQ1d4B1FSp5TUCFT4WmQyFW

Видео работы бота ВК:


https://github.com/kaser137/VoicesRecognizeBot/assets/107580630/1a7f004c-2376-4a19-9cdd-9973f0e5b1c0







