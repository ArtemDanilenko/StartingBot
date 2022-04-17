import telebot
from telebot import types

bot = telebot.TeleBot('5309333497:AAHvsGabgw83zQbYLTMiI2suX6ThFsO_LhA')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode = ['html'])

# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hello":
#       bot.send_message(message.chat.id, "Я тебе тоже привет!", parse_mode = ['html'])
#     elif message.text == "id":
#       bot.send_message(message.chat.id, f"Твой id:{message.from_user.id}", parse_mode = ['html'])
    
#     elif message.text == "photo":
#         photo = open('coolface.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
    
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Класное фото!')

@bot.message_handler(commands=['website'])
def website(message):

    marcup = types.InlineKeyboardMarkup()
    marcup.add(types.InlineKeyboardButton('Website', url='https://www.youtube.com/watch?v=GsZl0-G4k0c'))
    bot.send_message(message.chat.id, 'Website',reply_markup=marcup)

@bot.message_handler(commands=['help'])
def help(message):
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('start')
    website = types.KeyboardButton('/website')
    marcup.add(start, website)
    bot.send_message(message.chat.id, 'Ok',reply_markup=marcup)










bot.polling(non_stop=True)
