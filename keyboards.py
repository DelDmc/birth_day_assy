from telebot import types


def greeting_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    add_friend = types.KeyboardButton("Add new friend")
    update_friend = types.KeyboardButton("Update friend")
    remove_friend = types.KeyboardButton("Delete friend")
    all_friends = types.KeyboardButton("List of friends")
    markup.row(add_friend)
    markup.row(update_friend, remove_friend)
    markup.row(all_friends)
    return markup

def confirmation_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    correct_data = types.KeyboardButton("Correct")
    wrong_data = types.KeyboardButton("Wrong")
    cancel_entry = types.KeyboardButton("Cancel entry")

    markup.row(correct_data, wrong_data)
    markup.row(cancel_entry)
    return markup
