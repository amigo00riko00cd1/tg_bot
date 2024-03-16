import telebot

t_bot = telebot.TeleBot('6350777078:AAFhYz_Y2MpqVt7qp5_61G2rlEIwOY_sm_0')


@t_bot.message_handler(commands=['start'])
def start(message):
    t_bot.send_message(message.chat.id,'150 + 150')
@t_bot.message_handler()
def ss(message):
    a = t_bot.message.text.id
    if a == 300:
        t_bot.send_message(message.chat.id,'+')
    else:
        t_bot.send_message(message.chat.id,'-')

@t_bot.message_handler()
def eho(message):
    msg = message.text
    t_bot.send_message(message.chat.id,msg)




t_bot.polling(none_stop=True)