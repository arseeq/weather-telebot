import pyowm
from bot import bot
from config import OWM_API_KEY

owm = pyowm.OWM(OWM_API_KEY)

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

if __name__ == '__main__':
    bot.polling(none_stop=True)