import telebot
bot = telebot.TeleBot("621638068:AAHwqVgQo3xd0kh0VM3b1zl5svyViOkW0es")


@bot.message_handler(content_types=['text'])
def send_text(message):
    
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message,chat.id, 'Прощай, создатель')

def send_sticker(message):

    if message.text == 'Отправь сасный стикер' :
        bot.send_sticker("CAADAgADSskAAnlc4glshq449fyDqAl")
bot.polling()