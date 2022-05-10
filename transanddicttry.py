# from imaplib import _AnyResponseData
from email.mime import audio
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
    PollHandler,
    ConversationHandler,
)
from telegram import (
    ParseMode,
    Bot,
    Poll,
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

# level = [['tr'],['de'],['es']]

# markup = ReplyKeyboardMarkup(level, one_time_keyboard=True)

def create_audio_number(dest='de',src='en'):

  number = np.random.randint(1,100)
  translator = Translator()
  p = inflect.engine()
  number_w = p.number_to_words(number)
  result = translator.translate(number_w, src=src, dest=dest)



#   result  = 
#   Instantiates a client
  client = texttospeech.TextToSpeechClient()
 
  # Set the text input to be synthesized
  synthesis_input = texttospeech.SynthesisInput(text=result.text)
  
  # Build the voice request, select the language code ("en-US") and the ssml
  # voice gender ("neutral")
  voice = texttospeech.VoiceSelectionParams(
    language_code= dest,
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,)

  # Select the type of audio file you want returned
  audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(
        request={"input": synthesis_input, "voice": voice, "audio_config": audio_config}
    )

  # The response's audio_content is binary.
  with open(f'audio/{result.text}.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    
    
    
  return open(f'audio/{result.text}.mp3', 'rb'), result.text

#   level = input('what is the level of your number exercise:1/2/3 ')
# if level == '1':
#     k = np.random.randint(1,100)
# if level == '2':
#     k = np.random.randint(100,1000)
# if level == '3':
#     k = np.random.randint(1000,1000000)
    
# numberpractice,number_button= create_audio_number(f"{k}",'en','de')
with open('token.txt', 'r') as f:
    token = f.read()

updater = Updater(token)

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
        return result.text

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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

IN, out, tolang, voc, quizans= range(5)

m_help = "You can use the following commands:\n"\
"/practiceword : First select the destination language then select the right answer\n"\
"/practicenumber : First select the destination language then select the hardness level of the practice then guess the right answer\n"\
"/dictionary : English dictioanary give the word you want to see definition.\n"\
"/translate : Translates the text you enter. select destination and source languages \n"\
"/cannel : Cancels the current operation.\n"\
"/quiz : Answer the quiz.\n"\
#one_time_keyboard Requests clients to hide the keyboard as soon as it’s been used. 


# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
def start(update: Update, context: CallbackContext):

    """Start the conversation and ask user for input."""
    update.message.reply_text(
    """Hi! My name is Doctor LAng. You can go translation or dictionary
moreover you can practice easy words and numbers""",)#reply_markup=markup
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






def translatetele(update: Update, context : CallbackContext):
    # keyboard = [
    #     [
    #         InlineKeyboardButton("de", callback_data=str(IN)),
    #         InlineKeyboardButton("es", callback_data=str(IN)),
    #     ]
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # update.message.reply_text("give the dest lang and text", reply_markup=reply_markup)
    replytext = '''send the text you want to translate and specify the destination language by writing tolang then destination language code like 'en' 'de' 'es' 'tr' 'ar' 'it' \n
    Ex: Life is just a chance to grow a soul tolang en'''
    m_id = update.message.message_id
    update.message.reply_text(replytext, reply_to_message_id=m_id,)#reply_markup=markup
    # bot.register_next_step_handler(update.message, send_to_trans, message_id = m_id)
    return IN
# def destination_language()

# def start_handler(update: Update, context):
#     keyboard = [
#         [
#             InlineKeyboardButton("de", callback_data=str(IN)),
#             InlineKeyboardButton("es", callback_data=str(IN)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text("give the dest lang and text", reply_markup=reply_markup)
#     return IN




def send_to_trans(update: Update, context: CallbackContext):
    textt = update.message.text
    # dest = context.user_data[IN].data
    # replytextt = translatetext(textt,dest)

    # update.message.reply_text("this is not proper usage but maybe this is the translation you desire to english" + replytextt)


    # add if statement to prevent possible errors if the user dont use tolang in message
    
    distint = textt.split('tolang ')
    try:
        destlang = distint[1]
        maintext = distint[0]   
    except:
        spilit = textt.split()
        dest = spilit[-1]
        textlack = " ".join(spilit[:-1])
    
    if len(distint) == 2:

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
        try:
            replytextt = "this is not proper usage but maybe this is the translation you desire\n" + translatetext(textlack,dest)
        except:
            replytextt = '''You are doing wrong\n
            Please try again but anyway\n '''
        update.message.reply_text(replytextt)
    # await query.edit_message_text(replytextt)
    


def voicetele(update: Update, context: CallbackContext):
    replytext = '''send the text you want to translate and specify the destination language code like en de it tr es  b \n'''
    m_id = update.message.message_id
    update.message.reply_text(replytext, reply_to_message_id=m_id,)#reply_markup=markup
    return voc

def answer_with_voice(update: Update, context: CallbackContext):
    if len (update.message.text) == 2:
        dest = update.message.text
        answ = create_audio_number(dest)
    else:
        answ = create_audio_number()
    context.bot.send_message(chat_id=update.message.chat.id, text=answ[1])
    # context.bot.send_audio(chat_id=update.message.chat.id, audio=answ[0])
    # context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('audio/'+k+'.mp3', 'rb'))
    return quizans

# def quiztele(update: Update, context: CallbackContext):
#     selections = ['ana', 'baba', 'kardas']
#     question = 'what is your name?'
#     msg = update.effective_message.reply_poll(question,selections,type= Poll.QUIZ,correct_option_id=1)
#     payload = {
#     msg.poll.id: {"chat_id": update.effective_chat.id, "message_id": msg.message_id}
# }
#     context.bot_data.update(payload)

def quizanssfunc(update: Update, context: CallbackContext):
    # random.shuffle()

    answ = answer_with_voice.answ
    selections = ['ana', 'baba', 'kardas', f'{answ[1]}']
    question = 'what is your name?'
    msg = update.effective_message.reply_poll(question,selections,type= Poll.QUIZ,correct_option_id=4)
    payload = {
    msg.poll.id: {"chat_id": update.effective_chat.id, "message_id": msg.message_id}
}
    context.bot_data.update(payload)

async def receive_quiz_answer(update: Update, context: CallbackContext) -> None:
    """Close quiz after three participants took it"""
    # the bot can receive closed poll updates we don't care about
    if update.poll.is_closed:
        return
    if update.poll.total_voter_count == 1:
        try:
            quiz_data = context.bot_data[update.poll.id]
        # this means this poll answer update is from an old poll, we can't stop it then
        except KeyError:
            return
        await context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])
# def quizanss(update: Update, context: CallbackContext):
#     reply = 'Listen audio file what is the right number?'
#     answer = update.poll_answer
#     answered_poll = context.user_data['poll']
#     if answer.data == '1':
#         reply = 'You are right'
#     else:
#         reply = 'You are wrong'

def cancel(update, context):
    ''' to cancel the conversation'''
    update.message.reply_text('Thank you! I hope we can talk again some day.\n')
    return ConversationHandler.END






def main():
    """Main."""

    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    # dispatcher.add_handler(
    dispatcher.add_handler(CommandHandler('quiz',quizanssfunc))



    dispatcher.add_handler(PollHandler(receive_quiz_answer))


    # dispatcher.add_handler(CommandHandler("practiceword", create_audio_word))
    # dispatcher.add_handler(CommandHandler("practicenumber", create_audio_number))
    # dispatcher.add_handler(CommandHandler('translate', translatetele) )




    conv_handler = ConversationHandler (
        entry_points=[CommandHandler('translate', translatetele),CommandHandler('voice', voicetele)],
        # CommandHandler('quizvoice',answer_with_voice)
        states={
            IN: [MessageHandler(Filters.text , send_to_trans)],
            voc: [MessageHandler(Filters.text,answer_with_voice )],
            quizans : [CommandHandler('quizz',quizanssfunc)],
        #    tolang: [MessageHandler(Filters.text,start_handler)]
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