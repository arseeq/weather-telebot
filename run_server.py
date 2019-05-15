import flask
from telebot import types
from config import *
from bot_handlers import bot
import os
import pyowm, telebot

owm = pyowm.OWM(OWM_API_KEY)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_weather(message):
    place = message.text
    try:
        w = observation.get_weather()
    except:
        bot.reply_to(message, 'Not found')
        return
    temp = w.get_temperature('celsius')['temp']
    answer = f'Weather in {place}: \n{temp} °C, ' + w.get_detailed_status() + '\n'
    bot.reply_to(message, answer)

server = flask.Flask(__name__)

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
    return "Hello from Heroku!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))