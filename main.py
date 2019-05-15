# import pyowm, telebot
# import

# owm = pyowm.OWM()

# bot = telebot.TeleBot(token)

# @bot.message_handler(content_types=['text'])
# def send_weather(message):
#     place = message.text
#     try:
#         w = observation.get_weather()
#     except:
#         bot.reply_to(message, 'Not found')
#         return
#     temp = w.get_temperature('celsius')['temp']
#     answer = f'Weather in {place}: \n{temp} °C, ' + w.get_detailed_status() + '\n'
#     bot.reply_to(message, answer)