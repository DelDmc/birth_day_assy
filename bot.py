from telebot import TeleBot
from decouple import config

from mongo import db, users


bot = TeleBot(config("TELEGRAM_TOKEN"))


@bot.message_handler(commands=["start"])
def start_handler(message):
    if not db.users.find(
            {
                "_id": message.chat.id
            }
    ):
        users.insert_one(
            {
                "_id": message.chat.id,
                "name": message.chat.username,
                "friends": {},
            }
        )
    print(dir(db.users.database))
    # print(list(db.users.find({})))
    db.users.update_one(
        {
            "_id": message.chat.id
        },
        {
            "$set": {
                "friends": "No friends"
            }
        }
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f"date:{message.date},\n"
             f"message_id:{message.id},\n"
             f"chat_id:{message.chat.id},\n"
             f"Username:{message.chat.username},\n"
             f"First_name:{message.chat.first_name},\n"
             f"Last_name:{message.chat.last_name}, \n"
             f"Photo:{message.chat.photo},\n"
             f"Friends:{list(db.users.find({'_id':message.chat.id}))[0]['friends']}",
    )
    print(list(db.users.find({})))


bot.infinity_polling()

