import telebot
import webbrowser

bot = telebot.TeleBot('6510748134:AAE0JDtjRJ_SUH1HD_mRccstueZFXHJJ5Js')

# обработка запроса на ссылку
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://youtube.com')

# обработка команд
@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Пока</b> <em><u>ничего</u></em>', parse_mode='html')

# обработка сообщений, текста
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)