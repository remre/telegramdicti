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


def translatetext(text, src, dest):
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text

k = translatetext('mummy i want to eat','en','es')
print(k)


def dictionary(word):

  url_merriam = 'https://www.merriam-webster.com/dictionary/'
  
  page = requests.get(url_merriam+ word)
  soup = bs(page.content, 'html.parser')
  m = soup.find_all('span', class_='dtText')[:3]
  dict = []
  if m == []:
      m = soup.find('p',class_='spelling-suggestion-text')
      return [print(mm.text) for mm in m]
  else:
    [dict.append(c.text.split(':')[1].strip()) for c in m]
    return dict
# structure will be constituded in the following way

token = "5390988406:AAGZpy9maBTXPphCxwNdqRjTib3uLCrme4U"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


m_help = "You can use the following commands:\n"\
"/practiceword : First select the destination language then select the right answer\n"\
"/practicenumber : First select the destination language then select the hardness level of the practice then guess the right answer\n"\
"/dictionary : English dictioanary give the word you want to see definition.\n"\
"/translate : Translates the text you enter. select destination and source languages \n"\

logger = logging.getLogger(__name__)
level = ['en','de','es']

markup = ReplyKeyboardMarkup(level, one_time_keyboard=True)

def start(update: Update, context: CallbackContext):

    """Start the conversation and ask user for input."""
    update.message.reply_text(
    "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
    "Why don't you tell me something about yourself?",
    
)


def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(m_help)
    
    
def dictitele(update: Update, context: CallbackContext):
    
    # update.send_message(update.chat.id, 'Give me the word YOu want to see definition')
    message_id = update.message.message_id
    chat_id = update.message.chat.id
    # replytext = update.message.text
    replytext = 'Give me the word You want to see definition'
    context.bot.send_message(chat_id, replytext, reply_to_message_id=message_id)
    context.bot.register_next_step_handler(update.message, sendd_message)
    """Send a message when the command /help is issued."""
def sendd_message(update: Update, context: CallbackContext):
    replytext = dictionary(update.message.text)
    update.message.reply_text(replytext)
def translatetele(update: Update, context : CallbackContext):
  replytext = 'Give the source language then destination language and at least your text that want to translete'
  update.message.reply_text(replytext,reply_markup=markup)



def main():
    """Main."""

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))



    # dispatcher.add_handler(CommandHandler("practiceword", create_audio_word))
    # dispatcher.add_handler(CommandHandler("practicenumber", create_audio_number))
    dispatcher.add_handler(CommandHandler("dictionary", dictitele))
    dispatcher.add_handler(MessageHandler(Filters.text, sendd_message))
    # dispatcher.add_handler(CommandHandler("translate", translatetext))

    updater.start_polling()
    updater.idle()
    while True:
        schedule.run_pending()
        # The sleep prevents the CPU to work unnecessarily.
        time.sleep(1)
    updater.idle()

    # Declaration of the schedule
    # schedule.every().day.at(deliver_time).do(job)
if __name__ == "__main__":
    main()
  