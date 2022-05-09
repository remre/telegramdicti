# from imaplib import _AnyResponseData
import telebot 


import requests
from bs4 import BeautifulSoup as bs
from google.cloud import texttospeech
import re
from random_word import RandomWords

import inflect
import pandas

from googletrans import Translator
import requests
from bs4 import BeautifulSoup as bs
from google.cloud import texttospeech
import re
from random_word import RandomWords

import inflect
import pandas
import numpy as np

import logging
from telegram.ext import (
    CommandHandler,
    Updater,
    MessageQueue,
    MessageHandler,
    Filters,
    ExtBot,
    Defaults,
    ChatMemberHandler,
    InlineQueryHandler,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler,
)
from telegram import (
    ParseMode,
    Bot,
    
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    BotCommandScopeAllPrivateChats, 
    BotCommandScopeChat,
    BotCommandScopeAllGroupChats,
    BotCommandScopeChatAdministrators,
    ReplyKeyboardMarkup
)
from typing import Tuple, Dict, Any
from telebot import types

import numpy
import schedule
import time
import os

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/emreb/Documents/projects/secret/projecttelebotapi-cafc88105725.json'


logger = logging.getLogger(__name__)
level = [['tr'],['de'],['es']]

markup = ReplyKeyboardMarkup(level, one_time_keyboard=True)





def translatetext(text,*args):
    translator = Translator()
    if args != ():
        if len(args) == 1:
            result = translator.translate(text, dest=args[0])
        if len(args) == 2:
            result = translator.translate(text, src=args[1], dest=args[0])
        return result.text
    else:
        result = translator.translate(text)
        return result.text, args

# k = translatetext('Wilkommen')
# print(k)


def dictionary(word):

  url_merriam = 'https://www.merriam-webster.com/dictionary/'
  
  page = requests.get(url_merriam+ word)
  soup = bs(page.content, 'html.parser')
  m = soup.find_all('span', class_='dtText')[:3]
  dict = []
  if m == []:
      m = soup.find('p',class_='spelling-suggestion-text')
      return [mm.text for mm in m]
  else:
    [dict.append(c.text.split(':')[1].strip()) for c in m]
    return dict
# structure will be constituded in the following way

# This program is dedicated to the public domain under the CC0 license.
with open('token.txt', 'r') as f:
    token = f.read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

IN, out, tolang= range(3)

m_help = "You can use the following commands:\n"\
"/practiceword : First select the destination language then select the right answer\n"\
"/practicenumber : First select the destination language then select the hardness level of the practice then guess the right answer\n"\
"/dictionary : English dictioanary give the word you want to see definition.\n"\
"/translate : Translates the text you enter. select destination and source languages \n"\

#one_time_keyboard Requests clients to hide the keyboard as soon as it’s been used. 


# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
def start(update: Update, context: CallbackContext):

    """Start the conversation and ask user for input."""
    update.message.reply_text(
    """Hi! My name is Doctor LAng. You can go translation or dictionary\n
     moreover you can practice easy words and numbers""",reply_markup=markup)
    # return tolang


# @bot.message_handler(commands=['help'])
def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(m_help)
    


# @bot.message_handler(commands=['dictionary'])
def dictitele(update: Update, context: CallbackContext):
    
    
    message_id = update.message.message_id
    # chat_id = update.message.chat.id

    
    # replytext = update.message.text
    replytext = 'Give me the word You want to see definition'
    update.message.reply_text(replytext, reply_to_message_id = message_id)
    # update.message.reply_to_message(replytext, reply_to_message_id=message_id)
    # context.bot.register_next_step_handler(update.message, sendd_message_dict)
    """Send a message when the command /help is issued."""
    return out
# @bot.message_handler(content_types=['text'])
def sendd_message_dict(update: Update, context: CallbackContext):
    replytext = dictionary(update.message.text)
    update.message.reply_text(replytext)


# @bot.message_handler(commands=['translate'])






def translatetele(update: Update, context : CallbackContext):
    texti = update.message.text

    replytext = '''send the text you want to translate and specify the  then destination language by writing tolang then destination language code like 'en' 'de' 'es' 'tr' 'ar' 'it' \n
    Ex: Life is just a chance to grow a soul tolang en'''
    m_id = update.message.message_id
    update.message.reply_text(replytext, reply_to_message_id=m_id,)#reply_markup=markup
    # bot.register_next_step_handler(update.message, send_to_trans, message_id = m_id)
    return IN
# def destination_language()

# def echo(update: Update, context: CallbackContext):
#     # update.message.reply_text(update.message.text)
#     context.user_data['destlang'] = update.message.text
    
#     return IN
    
def send_to_trans(update: Update, context: CallbackContext):
    textt = update.message.text
    destlang = textt.split('tolang ')[1]
    maintext = textt.split('tolang ')[0] 
    dest = textt.split()[-1]
    if destlang == dest:

    # if 'src' in textt:
    #     pass

    # if 'destlang' in textt:
    #     pass
    # query = update.callback_query

    # await textt.answer()
        # update.message.reply_text(context.user_data['destlang'])
        replytextt = translatetext(maintext,destlang)
        update.message.reply_text(replytextt)
    else:
        replytextt = translatetext(maintext)
        update.message.reply_text("this is not proper usage but maybe this is the translation you desire to english" + replytextt)
    # await query.edit_message_text(replytextt)
    



def cancel(update, context):
    ''' to cancel the conversation'''
    update.message.reply_text('Thank you! I hope we can talk again some day.\n')
    return ConversationHandler.END






def main():
    """Main."""

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))



    # dispatcher.add_handler(CommandHandler("practiceword", create_audio_word))
    # dispatcher.add_handler(CommandHandler("practicenumber", create_audio_number))
    # dispatcher.add_handler(CommandHandler('translate', translatetele) )




    conv_handler = ConversationHandler (
        entry_points=[CommandHandler('translate', translatetele)],

        states={
            IN: [MessageHandler(Filters.text , send_to_trans)],
            # tolang: [MessageHandler(Filters.text,echo)]
        },

        fallbacks=[CommandHandler('cancel', cancel)] ,)


    conv_handlerr = ConversationHandler(
        entry_points=[CommandHandler("dictionary", dictitele)],

        states={
            out: [MessageHandler(Filters.text, sendd_message_dict)]},
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(conv_handlerr)
    # dispatcher.add_handler(CommandHandler("dictionary", dictitele))
    # dispatcher.add_handler(MessageHandler(Filters.text, sendd_message_dict))
    updater.start_polling()
    updater.idle()
    while True:
        schedule.run_pending()
        # The sleep prevents the CPU to work unnecessarily.
        time.sleep(1)
    # updater.idle()

    # Declaration of the schedule
    # schedule.every().day.at(deliver_time).do(job)



if __name__ == "__main__":
    # bot.polling()
    main()