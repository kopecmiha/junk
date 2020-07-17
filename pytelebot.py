import telebot
hi_dict = ["Привет", "/start", "Хелло"]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in hi_dict:
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

bot.polling()
