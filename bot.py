from telebot import TeleBot, types
from decouple import config

from keyboards import greeting_reply_keyboard, confirmation_reply_keyboard
from mongo import db
bot = TeleBot(config("TELEGRAM_TOKEN"))


@bot.message_handler(commands=["start"])
def start_handler(message):
    user_id = message.chat.id
    reply_markup = greeting_reply_keyboard()

    bot.send_message(
        chat_id=message.chat.id,
        text="Welcome to Bday Bot",
        reply_markup=reply_markup
    )


@bot.message_handler(func=lambda message: message.text == "Add new friend")
def add_new_friend_handler(message):
    msg = bot.send_message(chat_id=message.chat.id, text="Enter your friend's first name")
    bot.register_next_step_handler(msg, first_name_handler)


@bot.message_handler(regexp="/^[a-z ,.'-]+$/i")
def first_name_handler(message):
    data = {"first_name": message.text}
    msg = bot.send_message(chat_id=message.chat.id, text="Enter your friend's last name")
    bot.register_next_step_handler(msg, last_name_handler, data=data)


@bot.message_handler(regexp="/^[a-z ,.'-]+$/i")
def last_name_handler(message, data):
    data["last_name"] = message.text
    msg = bot.send_message(chat_id=message.chat.id, text="Enter your friend's bday in format ddmmyy. Ex.: 250199")
    bot.register_next_step_handler(msg, bday_handler, data=data)


@bot.message_handler(regexp="^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{1})?[0-9]{1}$")
def bday_handler(message, data):
    data["birthday"] = message.text
    first_name = data["first_name"]
    last_name = data["last_name"]
    birthday = data["birthday"]
    markup = confirmation_reply_keyboard()
    msg = bot.send_message(
        chat_id=message.chat.id,
        text=f"Please, confirm data.\n"
             f"First name: {first_name}\n"
             f"Last name: {last_name}\n"
             f"Birthday: {birthday}",
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, new_entry_confirmation_handler, data=data)


def new_entry_confirmation_handler(message, data):
    collection_name = message.chat.id
    collection = exec(f"db.{collection_name}")
    print(collection)
    collection.insert_one(data)


bot.infinity_polling()

