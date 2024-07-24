from telegram.ext import *
# bot_token = "7344857569:AAFmNxOob75KiczRHZ8CslIL0X9SERwbRko"
bot_token = "6192945152:AAGaM_RX7F9fY2wBhcCE00zdY1bGPtgHSRw"
from telegram import InlineKeyboardButton , InlineKeyboardMarkup, Update , callbackquery
#swx@2WS

def start(update,context):
    # update.message.reply_text('Hello Welcome to my portfolio bot.')
    buttons = [[InlineKeyboardButton("Yes",callback_data='yes')],[InlineKeyboardButton('No',callback_data='no')]]
    my_reply = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Welcome to my portfolio bot \n Do you want get started? .',reply_markup = my_reply)
def help(update,context):
    update.message.reply_text('This bot provides you with a list of my most recent projects.')
def user_message(update,context):
    user_msg = update.message.text.lower()
def my_handler(update: Update,context:CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'yes':
        query.edit_message_text('you\'re at right place to get to know my skills thank you.')
    else:
        query.edit_message_text('OK please check out when you feel like to, anytime i\'m available thanks.')
if __name__ == "__main__":
    print('Bot started ...')
    updater = Updater(token=bot_token,use_context=True)
    dp = updater.dispatcher   
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(MessageHandler(Filters.text,user_message))
    dp.add_handler(CallbackQueryHandler(my_handler))
    updater.start_polling()
    updater.idle()