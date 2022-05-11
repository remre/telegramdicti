# from imaplib import _AnyResponseData
# from email.mime import audio
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
import glob
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

def wrong_answers_word():
    pass


def wrong_answers_number():
    glob.glob("audio\*.mp3")
    return [file.split('\\')[1].split('.')[0] for file in glob.glob("audio\*.mp3")]

dictt_answers = wrong_answers_number()
np.random.shuffle(dictt_answers)

def create_audio_word(dest='de',src='en'):

  translator = Translator()
  r = RandomWords()
  word = r.get_random_word()
  result = translator.translate(word, src=src, dest=dest)
  # Instantiates a client
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
  with open('audio/question_word.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    
    
    
  return open('audio/question_word.mp3', 'rb'),result.text,word


def create_audio_number(number,dest='de',src='en'):
    numberr  = number_level(str(number))
    # number = np.random.randint(10,1000)
    translator = Translator()
    p = inflect.engine()
    number_w = p.number_to_words(numberr)
    result = translator.translate(number_w, src=src, dest=dest)
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
    with open('audio/NumberQuestion.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        
        
        
    return open('audio/NumberQuestion.mp3', 'rb'), result.text

# level = input('what is the level of your number exercise:1/2/3 ')


    
# numberpractice,number_button= create_audio_number(f"{k}",'en','de')
with open('C:/Users/emreb/Documents/projects/secret/token.txt', 'r') as f:
    token = f.read()



def translatetext(text,*args):
    translator = Translator()
    if args != ():
        if len(args) == 1:
            result = translator.translate(text, dest=args[0])
        if len(args) == 2:
            result = translator.translate(text, src=args[1], dest=args[0])
    else:
        result = translator.translate(text)

    return result.text

def dictionary(word):

    url_merriam = 'https://www.merriam-webster.com/dictionary/'
    page = requests.get(url_merriam+ word)
    soup = bs(page.content, 'html.parser')
    m = soup.find_all('span', class_='dtText')[:3]

    if m == []:
        words = soup.find('p',class_='spelling-suggestion-text')
        dictt =  [w.text for w in words]
    else:
        dictt= [c.text.split(':')[1].strip() for c in m]

    return (','.join(str(a)for a in dictt))
    
# structure will be constituded in the following way

# This program is dedicated to the public domain under the CC0 license.

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

IN, out, tolang, voc, quizans, goback,Quizroutes, newdict= range(8)

m_help = "You can use the following commands:\n"\
"/practiceword : First select the destination language then select the right answer\n"\
"/practicenumber : First select the destination language then select the hardness level of the practice then guess the right answer\n"\
"/dictionary : English dictioanary give the word you want to see definition.\n"\
"/translate : Translates the text you enter. select destination and source languages \n"\
"/cancel : Cancels the current operation.\n"\
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
    replytext = '''send the text you want to translate and specify the destination language by writing * then destination language code like 'en' 'de' 'es' 'tr' 'ar' 'it' \n
    Ex: Life is just a chance to grow a soul * de\n see more lang code here https://developers.google.com/admin-sdk/directory/v1/languages'''
    m_id = update.message.message_id
    update.message.reply_text(replytext, reply_to_message_id=m_id,)#reply_markup=markup
    # bot.register_next_step_handler(update.message, send_to_trans, message_id = m_id)
    return IN


def send_to_trans(update: Update, context: CallbackContext):
    textt = update.message.text
    distint = textt.split('* ')

    try:
        destlang = distint[1].lower()
        maintext = distint[0]   
    except IndexError:
        spilit = textt.split()
        dest = spilit[-1].lower()
        textlack = " ".join(spilit[:-1])

    if len(distint) == 2:

        replytextt = translatetext(maintext,destlang)

    else:
        try:
            replytextt = "this is not proper usage but maybe this is the translation you desire\n" + translatetext(textlack,dest)
        except Exception as e:
            replytextt = '''You are doing wrong\n
            Please try again but anyway\n '''

    update.message.reply_text(replytextt)
    # await query.edit_message_text(replytextt)
# def answer_with_voice_word(update: Update, context: CallbackContext):
#     global answers
#     m_id = update.message.message_id
#     textt = update.message.text.split(' ')
#     if len(textt)==2:

#         if len (textt[0]) == 2:
#             hardness = number_level(textt[1])
#             dest = (update.message.text).lower()
#             # if type(hardness) == int:
#             #     answers['number'] = create_audio_number(hardness,dest)
#             # else:
#             answers['number'] = create_audio_number(dest)
#         else:
#             answers['number'] = create_audio_number()
#     # move_ans = {'audio': answ}
#     # context.bot_data.update(move_ans)
#     # context.bot.send_message(chat_id=update.message.chat.id, text=answers['number'][1])
#     context.bot.send_audio(chat_id=update.message.chat.id, audio=answers['number'][0])

#     return quizans  


def voicetele(update: Update, context: CallbackContext):
    replytext = '''So Here is the voice quiz give me the language code that you want to exercise then the level you want to train (1-3) \n
I will send you the voice then you
will  guess the right answer. Let's go! Ex: es 3'''
    m_id = update.message.message_id

    update.message.reply_text(replytext, reply_to_message_id=m_id,)#reply_markup=markup
    return voc

answers = {'number':'', 'words':''}
def number_level(number):

    if number == '1':
        k = np.random.randint(1,100)
    if number == '2':
        k = np.random.randint(100,1000)
    if number == '3':
        k = np.random.randint(1000,10000)
    if re.match('[1-3]',str(number)) is None:
        k = 'You need to give 1,2,3 as level nothing else'
    return k

def answer_with_voice(update: Update, context: CallbackContext):
    global answers
    m_id = update.message.message_id
    textt = update.message.text.split(' ')
    if len(textt)==2:

        if len (textt[0]) == 2:
            hardness = textt[1].strip()
            dest = textt[0].lower().strip()

            answers['number'] = create_audio_number(hardness,dest)
        else:
            context.bot.send_message(chat_id=update.message.chat.id, text="You need to give the language code and the level check the example\n and try again!")
            return voc
    # move_ans = {'audio': answ}
    # context.bot_data.update(move_ans)
    # context.bot.send_message(chat_id=update.message.chat.id, text=answers['number'][1])

    context.bot.send_audio(chat_id=update.message.chat.id, audio=answers['number'][0])
    # query  = update.callback_query
    # await query.answer()
    # keyboard = [
    #     [
    #         InlineKeyboardButton("Yes, let's do it again!", callback_data=str(quizans)),
    #         InlineKeyboardButton("Nah, I've had enough ...", callback_data=str(goback)),
    #     ]
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # await query.edit_message_text(text="Third CallbackQueryHandler. Do want to start over?", reply_markup=reply_markup)
    return quizans



# solve the number level function problem and throw it to the right function and return the answer
# we need to run create_audio_number function just one time 
def quiztele(update: Update, context: CallbackContext):
    global answers, dictt_answers

    number_answer = answers["number"][1]
    # question  = answers["number"][0]
    level = update.message.text
    selections = [dictt_answers[1],dictt_answers[2],dictt_answers[3], f'{number_answer}']
    
    np.random.shuffle(selections)
    correct_id = selections.index(f'{number_answer}')
    selections 
    question = 'what is the number?'
    msg = update.effective_message.reply_poll(question,selections,type= Poll.QUIZ,correct_option_id=correct_id)
    payload = {
    msg.poll.id: {"chat_id": update.effective_chat.id, "message_id": msg.message_id}
}
    context.bot_data.update(payload)

# def quizanssfunc(update: Update, context: CallbackContext):
#     # random.shuffle()
#     #  gonna find a way to take answer from answer_with_voice function
#     move_ans = context.bot_data.get(update.m_id)
#     answer = answers('audio')
#     selections = ['ana', 'baba', 'kardas', f'{answer[1]}']
#     question = 'what is your name?'
#     msg = update.effective_message.reply_poll(question,selections,type= Poll.QUIZ,correct_option_id=4)
#     payload = {
#     msg.poll.id: {"chat_id": update.effective_chat.id, "message_id": msg.message_id}
# }
#     context.bot_data.update(payload)

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

async def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END




def main():
    """Main."""
    updater = Updater(token)
    dispatcher = updater.dispatcher
    # dispatcher.add_handler(MessageHandler(Filters.text, help))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # dispatcher.add_handler(CommandHandler('cancel', cancel))
    # dispatcher.add_handler(
    # dispatcher.add_handler(CommandHandler('quiz',quiztele))



    dispatcher.add_handler(PollHandler(receive_quiz_answer))


    # dispatcher.add_handler(CommandHandler("practiceword", create_audio_word))
    # dispatcher.add_handler(CommandHandler("practicenumber", create_audio_number))
    # dispatcher.add_handler(CommandHandler('translate', translatetele) )


    translator_conv = ConversationHandler (
        entry_points=[CommandHandler('translate', translatetele)],
        # CommandHandler('quizvoice',answer_with_voice)
        states={
            IN: [MessageHandler(Filters.text , send_to_trans)]
            #make it message handler with level 
           
        },

        fallbacks=[CommandHandler('help', help)] ,)

    conv_handler = ConversationHandler (
        entry_points=[CommandHandler('practicenumber', voicetele)],
        # CommandHandler('quizvoice',answer_with_voice)
        states={
            voc: [MessageHandler(Filters.text, answer_with_voice)],
            quizans : [MessageHandler(Filters.text, quiztele)],
            
            
            #make it message handler with level 
           
        },
        #    tolang: [MessageHandler(Filters.text,start_handler)]},

        fallbacks=[CommandHandler('help', help)] ,)


    conv_handlerr = ConversationHandler(
        entry_points=[CommandHandler("dictionary", dictitele)],

        states={
            out: [MessageHandler(Filters.text, sendd_message_dict)],
            #, pattern='^([a-z])$'
        },
        
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(translator_conv)
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(conv_handlerr)
    # dispatcher.add_handler(#Quizroutes: [
            # CallbackQueryHandler(quiztele,pattern="^"+str(quizans)+"$"),
            # CallbackQueryHandler(voicetele,pattern="^"+str(goback)+"$"), 
        #    ) #],
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


# DispatcherHandlerStop
if __name__ == "__main__":
    # bot.polling()
    main()