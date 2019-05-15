import pyowm, telebot

token = '741003962:AAFY4fv2AzQpnqIiF_p2dRy55Tn_m1Vma6o'
owm = pyowm.OWM('2618f435b3b06d26a5a2033df700f582')

bot = telebot.TeleBot(token)

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

bot.polling()