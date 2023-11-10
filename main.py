import telebot

from joke.joke.jokes import chucknorris

bot = telebot.TeleBot("6608715523:AAF9rMJd4RPqsLgFxaVTiu9-O0L9sfGLhHE")


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, chucknorris())
    bot.register_next_step_handler(message, main)


bot.polling(none_stop=True)
