# Работаем с эмоциями
from emoji import emojize
from random import choice
import settings
# Reply keyboard, Получение геолокации и контактных данных пользователя
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']
        
def get_keybard():
    contact_button = KeyboardButton('Send me user contact', request_contact=True)
    location_button = KeyboardButton('Send me geolocation', request_location=True)
 
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Send me a cat', 'Change ava'],
                                        [contact_button, location_button]
                                      ], resize_keyboard=True
                                      )