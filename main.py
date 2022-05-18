import os

import logging

from telegram.ext import (
    CommandHandler,
    Updater,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    PollHandler,
    ConversationHandler,
)
from telegram import (
    KeyboardButtonPollType,
    KeyboardButton,
    Bot,
    Poll,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)
from mhandlers import *


# TOKEN = '5390988406:AAGZpy9maBTXPphCxwNdqRjTib3uLCrme4U'
TOKEN = os.environ.get('TOKEN')
def main():
    """Main."""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # dispatcher.add_handler(CommandHandler("cancel", cancel))
    
    dispatcher.add_handler(PollHandler(receive_quiz_answer,pass_chat_data=True, pass_user_data=True)) 
    

    translator_conv = ConversationHandler(
        entry_points=[CommandHandler('translate', translatetele)],

        states={
            IN: [
                MessageHandler(Filters.text , send_to_trans),#& ~Filters.command  
                # CommandHandler("cancel", cancel)
                ],
            end_trans:
            [
                MessageHandler(Filters.text, send_to_trans),
                MessageHandler(Filters.regex('cancel'),cancel),
            ], 
        },
       fallbacks=[CommandHandler('help', help)],
        )

    dictionary_conv = ConversationHandler(
        entry_points=[CommandHandler("dictionary", dictitele)],
        states={
            out: [
                MessageHandler(Filters.text & ~Filters.command, sendd_message_dict),# & ~Filters.command
            # CommandHandler("cancel", cancel),
            ],
            end_dict: 
            [
                MessageHandler(Filters.text & ~Filters.command, sendd_message_dict),
                CommandHandler("cancel", cancel),
            ]
            #, pattern='^([a-z])$'
        },
        
        fallbacks=[
            CommandHandler('help', help)],
    )

    number_quiz = ConversationHandler (
        entry_points=[CommandHandler('practicenumber', voicetele)],

        states={
            voc: [MessageHandler(Filters.text, answer_with_voice)],
            # quizans : [MessageHandler(Filters.text, quiztele)],
            Quizroutes:
            [
            CallbackQueryHandler(answer_with_voice, pattern="^" + str(voc) + "$"),
            CallbackQueryHandler(quiztele, pattern="^" + str(quizans) + "$"),
            # CommandHandler("cancel", cancel),
            ],  # CallbackQueryHandler(cancel, pattern="^" + str(exit) + "$")
            # end_quiz:[
            # CallbackQueryHandler(voicetele, pattern="^" + str(quizagain) + "$"), 
            # CallbackQueryHandler(cancel, pattern="^" + str(exit) + "$"),
            # CommandHandler("cancel", cancel),  
            # ],          
        },

        fallbacks=[CommandHandler('cancel', cancel)],
        )

    word_quiz = ConversationHandler (allow_reentry=True,
        entry_points=[CommandHandler('practiceword', voicetelee)],
        # CommandHandler('quizvoice',answer_with_voice)
        states={
            boc:
            [MessageHandler(Filters.text, answer_with_voice)],
            # quizans : [MessageHandler(Filters.text, quiztele)],
            Quizroutes: 
            [CallbackQueryHandler(help, pattern="^" + str(boc) + "$"), 
            # CallbackQueryHandler(voicetele, pattern="^" + str(quizagain) + "$"),
            CallbackQueryHandler(quiztele, pattern="^" + str(quizans) + "$"),
            
            # MessageHandler(Filters.regex('quizagain'), help),
            CommandHandler("cancel", cancel),
            ],
            end_quiz:
            [
            # CallbackQueryHandler(cancel),
            CallbackQueryHandler(cancel, pattern="^" + str(exit) + "$"),
            CallbackQueryHandler(voicetelee, pattern="^" + str('quizagain') + "$"),
            # MessageHandler(Filters.regex('exit'), cancel),
            # CommandHandler("cancel", cancel), 
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)], 
        )

    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command , handle_midlle_message))
    dispatcher.add_error_handler(error) 
    dispatcher.add_handler(translator_conv)
    dispatcher.add_handler(number_quiz)
    dispatcher.add_handler(word_quiz)
    dispatcher.add_handler(dictionary_conv)

    PORT = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url='https://telegramtrans-app.herokuapp.com/'+TOKEN)

    # logging.info(f"Start webhook mode on port PORT:{PORT}")
                        #   webhook_url='https://transanddict.herokuapp.com/'+TOKEN)
                        # to post https://api.telegram.org/bot5390988406:AAGZpy9maBTXPphCxwNdqRjTib3uLCrme4U/setWebhook

    # updater.start_polling()

    updater.idle()
    # while True:
    #     schedule.run_pending()
        # The sleep prevents the CPU to work unnecessarily.
        # time.sleep(1)
    # updater.idle()

    # Declaration of the schedule
    # schedule.every().day.at(deliver_time).do(job)


# DispatcherHandlerStop
if __name__ == "__main__":
    # bot.polling()
    # print(token), print(PORT)
    main()