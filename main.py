import os


from google.cloud import texttospeech
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


from transanddicttry import *


def main():
    """Main."""
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(PollHandler(receive_quiz_answer,pass_chat_data=True, pass_user_data=True)) 
    dispatcher.add_error_handler(error)

    translator_conv = ConversationHandler (
        entry_points=[CommandHandler('translate', translatetele)],

        states={
            IN: [MessageHandler(Filters.text , send_to_trans)]
           
        },
        fallbacks=[CommandHandler('help', help)] ,
        )
        
    number_quiz = ConversationHandler (
        entry_points=[CommandHandler('practicenumber', voicetele)],

        states={
            voc: [MessageHandler(Filters.text, answer_with_voice)],
            # quizans : [MessageHandler(Filters.text, quiztele)],
            Quizroutes:
            [CallbackQueryHandler(answer_with_voice, pattern="^" + str(voc) + "$"), 
           
            CallbackQueryHandler(quiztele, pattern="^" + str(quizans) + "$"),
            CallbackQueryHandler(cancel, pattern="^" + str(exit) + "$")],    
        },

        fallbacks=[CommandHandler('help', help)] ,
        )

    word_quiz = ConversationHandler (
        entry_points=[CommandHandler('practiceword', voicetelee)],
        # CommandHandler('quizvoice',answer_with_voice)
        states={
            voc:
            [MessageHandler(Filters.text, answer_with_voice)],
            # quizans : [MessageHandler(Filters.text, quiztele)],
            Quizroutes: 
            [CallbackQueryHandler(answer_with_voice, pattern="^" + str(voc) + "$"), 
            # CallbackQueryHandler(voicetele, pattern="^" + str(quizagain) + "$"),
            CallbackQueryHandler(quiztele, pattern="^" + str(quizans) + "$"),
            MessageHandler(Filters.regex('quizagain'), help),],

        },
        fallbacks=[CommandHandler('help', help)] ,)

    conv_handlerr = ConversationHandler(
        entry_points=[CommandHandler("dictionary", dictitele)],
        states={
            out: [MessageHandler(Filters.text, sendd_message_dict)],
            #, pattern='^([a-z])$'
        },
        
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(translator_conv)
    dispatcher.add_handler(number_quiz)
    dispatcher.add_handler(word_quiz)
    dispatcher.add_handler(conv_handlerr)

    PORT = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=token)
    updater.bot.setWebhook('https://telegramtrans-app.herokuapp.com/' + token)

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