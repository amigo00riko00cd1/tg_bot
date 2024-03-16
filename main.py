from background import keep_alive
import telebot
from fuzzywuzzy import fuzz
import threading
from datetime import datetime, timedelta
a=''
a1=''
bot= telebot.TeleBot('6350777078:AAFhYz_Y2MpqVt7qp5_61G2rlEIwOY_sm_0')



threshold = 75

with open("bad_words.txt",'r') as f:
    words = f.read()
    bad_words = words.split()

num_to_let = {
    '1': 'i',
    '4': 'a',
    '3': 'e',
    '0': 'o',
}

def is_bad(message):
    current_severity = 0
    words_inmessage = message.split()
    for word in words_inmessage:
        for bad_word in bad_words:
            if bad_word in word.lower():
                current_severity = 2
                return current_severity
        if word.lower() in bad_words:
            current_severity = 2
            return current_severity
        if [w for w in bad_words if fuzz.ratio(word, w) >= threshold]:
            current_severity = 1
        else:
            pass
    return current_severity


@bot.message_handler()
def frz (message):
    a=message.text.lower()
    a1=is_bad(a)
    if a1 == 0:
        pass
    elif a1 == 1:
        chat_id = message.chat.id
        message_id = message.message_id
        bot.delete_message(chat_id, message_id)
        bot.send_message(message.chat.id,f'{message.from_user.first_name} Your message may be inappropriate, please message admins if you think it was a mistake')
        with open('logs.txt', 'a') as f:
            f.write(f"{message.from_user.id} {a} {message.from_user.first_name} {datetime.now()}\n")
    elif a1 == 2:
        chat_id = message.chat.id
        message_id = message.message_id
        bot.delete_message(chat_id, message_id)
        bot.send_message(message.chat.id,f'{message.from_user.first_name} Your message contained inappropriate words, please be respectful and kind to other members.')
        with open('logs.txt', 'a') as f:
            f.write(f"{message.from_user.id} {a} {message.from_user.first_name} {datetime.now()}\n")


keep_alive()

bot.polling(none_stop=True)