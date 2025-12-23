import telebot

api = "8389217347:AAG_S9-Pcm5p0YRUGN5oNjgrZvhS_wzPGsQ"
bot_username = "CopIEM_bot"

bot = telebot.TeleBot(api)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, f"Kya be bhikmangya(Rut)")

def notify(message):
    bot.send_message(message.chat.id, message.text)
bot.polling()
