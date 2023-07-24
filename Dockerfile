FROM python:3

FROM gorialis/discord.py

RUN mkdir -p /usr/src/bot

RUN pip3 install python-dotenv

WORKDIR /usr/src/bot

COPY . .

CMD [ "python3", "bot.py" ]