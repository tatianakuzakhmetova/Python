import logging

# Высылаем котиков
from glob import glob
from random import choice

from utils import get_keybard, get_user_emo


# user_data - это словарь    
def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = "Hello {}".format(emo)
    update.message.reply_text(text, reply_markup=get_keybard())

    

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Hello {} {}! You wrote: {}".format(update.message.chat.first_name, emo, update.message.text, reply_markup=get_keybard())
    logging.info("User: %s, Chat_id: %s, Message: %s", update.message.chat.first_name, update.message.chat.id, update.message.text)
    print(update.message)
    update.message.reply_text(user_text, reply_markup=get_keybard())


def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    # 'rb' = read binary
    bot.send_photo(chat_id=update.message.chat_id, photo=open(cat_pic, 'rb'), reply_markup=get_keybard())

        
def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Done: {}'.format(emo), reply_markup=get_keybard())

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Done: {}'.format(get_user_emo(user_data)), reply_markup=get_keybard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Done: {}'.format(get_user_emo(user_data)), reply_markup=get_keybard())   
