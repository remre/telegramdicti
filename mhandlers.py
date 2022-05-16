from email import message
from gc import callbacks
from generations.trans_dict_func import TransGoogle,Translatet, dictionary,wrong_answers_number
import numpy as np
import glob

import telebot 
import logging
from telegram.ext import (
    DispatcherHandlerStop,
    ContextTypes,
    ConversationHandler,
    Updater,
    ExtBot,
    CallbackContext,
)
from telegram import (
    ReplyKeyboardRemove,
    KeyboardButtonPollType,
    KeyboardButton,
    Bot,
    Poll,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)
# from typing import Tuple, Dict, Any
# import schedule
import time
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/emreb/Documents/projects/secret/projecttelebotapi-cafc88105725.json'


logger = logging.getLogger(__name__)

dictt_answers = wrong_answers_number()
np.random.shuffle(dictt_answers)

# with open('C:/Users/emreb/Documents/projects/secret/token.txt', 'r') as f:
#     TOKEN = f.read()
# TOKEN = '5390988406:AAGZpy9maBTXPphCxwNdqRjTib3uLCrme4U'
IN, out, voc, boc, quizans,Quizroutes,quizagain = range(7)
end_dict,end_trans,end_quiz= range(3)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

m_help = "You can use the following commands:\n"\
"/practiceword : First select the destination language then select the right answer\n"\
"/practicenumber : First select the destination language then select the hardness level of the practice then guess the right answer\n"\
"/dictionary : English dictioanary give the word you want to see definition.\n"\
"/translate : Translates the text you enter. select destination and source languages \n"\
"/cancel : Cancels the current operation.\n"\
#one_time_keyboard Requests clients to hide the keyboard as soon as it’s been used. 


# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
def start(update: Update, context: CallbackContext):

    """Start the conversation and ask user for input."""
    update.message.reply_text(
    """Hi! My name is Translation Bot. You can go translation or dictionary
moreover you can practice easy words and numbers""",)#reply_markup=markup
    # return tolang


# @bot.message_handler(commands=['help'])
def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    # update.message.reply_text(m_help)
    # update.message.sender_chat_id = update.message.chat_id
    
    context.bot.send_message(chat_id=update.message.chat_id, text=m_help)
    


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
    return end_dict

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

        trial = Translatet(maintext,destlang)
        replytextt = trial.translatetext()
    else:
        try:
  
            trial = Translatet(textlack,dest)
            replytextt = "this is not proper usage but maybe this is the translation you desire\n" + trial.translatetext()
        except Exception as e:
            replytextt = '''You are doing wrong\n
            Please try again but anyway\n '''

    update.message.reply_text(replytextt)
    return end_trans

def voicetele(update: Update, context: CallbackContext):
    replytext = '''So Here is the voice quiz give me the language code that you want to exercise then the level you want to train (1-3) \n
I will send you the voice then you
will  guess the right answer. Let's go! Ex: es 3'''
    # m_id = update.message.message_id  reply_text  reply_to_message_id=m_id,
    try:
        m_id = update.message.message_id

        update.message.reply_text(replytext,reply_to_message_id = m_id)#reply_markup=markup
    except:
        update
    return voc
def voicetelee(update: Update, context: CallbackContext):
    replytext = '''So Here is the voice quiz give me the language code that you want to test in word skills \n
I will send you the voice then you
will  guess the right answer. Let's go! Ex: es'''

    # m_id = update.message.message_id

    # update.message.reply_text(str(m_id),message_id = m_id)
    try:
        m_id = update.message.message_id

        update.message.reply_text(replytext,reply_to_message_id = m_id)
    except:
        dat = update.callback_query.data
        if dat == 'quizagain':
            update.callback_query.answer()
            update.callback_query.edit_message_text(text=replytext)
    #reply_markup=markup
    return boc

answers = {'number':'', }#'words':'' 

def answer_with_voice(update: Update, context: CallbackContext):
    global answers
    m_id = update.message.message_id
    textt = update.message.text.split(' ')
    if len(textt)==2:

        if len(textt[0]) == 2:
            hardness = textt[1].strip()
            dest = textt[0].lower().strip()
            new_number = TransGoogle(dest,hardness)
            new_voice = new_number.create_audio_file()
            answers['number'] = new_voice
        else:
            context.bot.send_message(chat_id=update.message.chat.id, text="You need to give the language code and the level check the example\n and try again!")
            return voc
    if len(textt) == 1 and len(textt[0]) == 2:
        dest = textt[0].lower().strip()
        new_word = TransGoogle(dest)
        new_word_voice = new_word.create_audio_file()
        answers['number'] = new_word_voice
    else:
        context.bot.send_message(chat_id=update.message.chat.id, text="You are giving wrong input\n please try again")
    # context.bot.send_message(chat_id=update.message.chat.id, text=answers['number'][1])
    keyboard = [
        [
            InlineKeyboardButton("don't like it new question", callback_data=str(voc)),
            InlineKeyboardButton("go to question", callback_data=str(quizans)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)    
    context.bot.send_audio(chat_id=update.message.chat.id, audio=answers['number'][0],reply_markup=reply_markup )
    # context.bot.send_message(update.message.chat.id, answers['number'][1])
    return Quizroutes

def quiztele(update: Update, context: CallbackContext):
    global answers, dictt_answers

    number_answer = answers["number"][1]
    # question  = answers["number"][0]
    # level = update.message.text
    # selections = [dictt_answers[1],dictt_answers[2],dictt_answers[3], f'{number_answer}']
    selections_deployed= ['saman','duman','yaman', f'{number_answer}']
    np.random.shuffle(selections_deployed)
    correct_id = selections_deployed.index(f'{number_answer}')
    selections_deployed 
    question = 'what is the answer?'
    keyboard = [
        [
            InlineKeyboardButton("Again!!", callback_data=str(quizagain)),
            InlineKeyboardButton("Enough!",callback_data=str(exit)),#, callback_data=str(exit)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = update.effective_message.reply_poll(question,selections_deployed,type= Poll.QUIZ,correct_option_id=correct_id,reply_markup=reply_markup)
    payload = {
    msg.poll.id: {"chat_id": update.effective_chat.id, "message_id": msg.message_id}
}
    context.bot_data.update(payload)
    return end_quiz



async def receive_quiz_answer(update: Update, context: CallbackContext) -> None:
    """Close quiz after three participants took it"""
    message = update.effective_message
    # the bot can receive closed poll updates we don't care about
    if update.poll.is_closed:
        return
    if update.poll.total_voter_count == 1:
        try:

            quiz_data = context.bot_data[update.poll.id]
            chat_id = quiz_data["chat_id"]
            
        # this means this poll answer update is from an old poll, we can't stop it then
        except KeyError:
            return
    await context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])

def handle_midlle_message(update,context):

    update.message.reply_text("You are not supposed text give me some commands")
    # return 

def cancel(update, context):
    ''' to cancel the conversation'''
    reply_text='Thank you! I hope we can talk again some day.\n'
    try:
        cqd = update.callback_query.data
        if cqd == str(exit):
            update.callback_query.answer()
            update.callback_query.send_message(text=reply_text)
            return ConversationHandler.END
    except:
        update.message.reply_text(reply_text)
        return ConversationHandler.END
    # try:
    # # m_id = update.message.message_id
    #     update.message.reply_text(reply_text)
    # except:
        
    #     if cqd == 'exit':
    # #     pass
    #     # mes_id = update.inline_message_id
    #     # pass
    #     # context.bot.send_message(text=reply_text)
    #     # Bot.answer_inline_query(update.inline_query.id, [], cache_time=1)
    
    # return ConversationHandler.END
    # DispatcherHandlerStop(state=help)
# def done(update: Update, context: ContextTypes):
    
#     """Display the gathered info and end the conversation."""
#     user_data = context.user_data
#     reply_markup=ReplyKeyboardRemove(),
#     user_data.clear()
#     return ConversationHandler.END



def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" ', update)
    logging.exception(context.error)

# def main():
#     """Main."""
#     updater = Updater(token)
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("help", help))
#     dispatcher.add_handler(CommandHandler('cancel', cancel))
#     dispatcher.add_handler(PollHandler(receive_quiz_answer,pass_chat_data=True, pass_user_data=True)) 
#     dispatcher.add_error_handler(error)

#     translator_conv = ConversationHandler (
#         entry_points=[CommandHandler('translate', translatetele)],

#         states={
#             IN: [MessageHandler(Filters.text , send_to_trans)]
           
#         },
#         fallbacks=[CommandHandler('help', help)] ,
#         )
        
#     number_quiz = ConversationHandler (
#         entry_points=[CommandHandler('practicenumber', voicetele)],

#         states={
#             voc: [MessageHandler(Filters.text, answer_with_voice)],
#             # quizans : [MessageHandler(Filters.text, quiztele)],
#             Quizroutes:
#             [CallbackQueryHandler(answer_with_voice, pattern="^" + str(voc) + "$"), 
           
#             CallbackQueryHandler(quiztele, pattern="^" + str(quizans) + "$"),
#             CallbackQueryHandler(cancel, pattern="^" + str(exit) + "$")],    
#         },

#         fallbacks=[CommandHandler('help', help)] ,
#         )

#     word_quiz = ConversationHandler (
#         entry_points=[CommandHandler('practiceword', voicetelee)],
#         # CommandHandler('quizvoice',answer_with_voice)
#         states={
#             voc:
#             [MessageHandler(Filters.text, answer_with_voice)],
#             # quizans : [MessageHandler(Filters.text, quiztele)],
#             Quizroutes: 
#             [CallbackQueryHandler(answer_with_voice, pattern="^" + str(voc) + "$"), 
#             # CallbackQueryHandler(voicetele, pattern="^" + str(quizagain) + "$"),
#             CallbackQueryHandler(quiztele, pattern="^" + str(quizans) + "$"),
#             MessageHandler(Filters.regex('quizagain'), help),],

#         },
#         fallbacks=[CommandHandler('help', help)] ,)

#     conv_handlerr = ConversationHandler(
#         entry_points=[CommandHandler("dictionary", dictitele)],
#         states={
#             out: [MessageHandler(Filters.text, sendd_message_dict)],
#             #, pattern='^([a-z])$'
#         },
        
#         fallbacks=[CommandHandler('start', start)],
#     )

#     dispatcher.add_handler(translator_conv)
#     dispatcher.add_handler(number_quiz)
#     dispatcher.add_handler(word_quiz)
#     dispatcher.add_handler(conv_handlerr)

#     updater.start_webhook(listen="0.0.0.0",
#                           port=int(8080),
#                           url_path=token)
#     updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + token)

#     updater.start_polling()
#     updater.idle()
#     while True:
#         schedule.run_pending()
#         # The sleep prevents the CPU to work unnecessarily.
#         time.sleep(1)
#     # updater.idle()

#     # Declaration of the schedule
#     # schedule.every().day.at(deliver_time).do(job)


# # DispatcherHandlerStop
# if __name__ == "__main__":
#     # bot.polling()
#     main()
