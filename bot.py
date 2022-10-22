from telebot import TeleBot
from decouple import config


bot = TeleBot(config("TELEGRAM_TOKEN"))


@bot.message_handler(commands=["start"])
def start_handler(message):

    bot.send_message(
        chat_id=message.chat.id,
        text=f"date:{message.date},\n"
             f"message_id:{message.id},\n"
             f"chat_id:{message.chat.id},\n"
             f"Username:{message.chat.username},\n"
             f"First_name:{message.chat.first_name},\n"
             f"Last_name:{message.chat.last_name}, \n"
             f"Photo:{message.chat.photo}",
    )


bot.infinity_polling()

