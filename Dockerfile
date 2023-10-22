FROM python:3.10-slim

RUN mkdir "bots"

WORKDIR /bots

COPY ./requirements.txt /bots

RUN pip install -r /bots/requirements.txt

COPY . /bots

CMD ["python", "tg_vk_bot.py"]

