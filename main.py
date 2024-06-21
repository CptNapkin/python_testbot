import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6510748134:AAE0JDtjRJ_SUH1HD_mRccstueZFXHJJ5Js')


# обработка запроса на ссылки
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://youtube.com')


# обработка команд
@bot.message_handler(commands=['start', 'hello'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Открыть Youtube')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}',
                     reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Открыть Youtube':
        bot.send_message(message.chat.id, 'Используй команду /buttons')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Пока</b> <em><u>ничего</u></em>', parse_mode='html')


# обработка фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Найс фото!')

# создание кнопок
@bot.message_handler(commands=['buttons'])
def link(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Открыть Youtube', url='https://youtube.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Ссылка на Youtube', reply_markup=markup)


# настройка кнопок
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 3)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


# обработка сообщений, текста
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)