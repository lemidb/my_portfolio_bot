from telegram.ext import Updater, CommandHandler,MessageHandler, dispatcher , Filters, CallbackQueryHandler, callbackcontext

from telegram import InlineKeyboardButton,InlineKeyboardMarkup, Update

from config import bot_token


def start_method(update,context):
    print(update)
    menu = [[InlineKeyboardButton(text='menu 1',url='https://www.google.com'),InlineKeyboardButton('menu 2',callback_data='menu2')]]
    update.message.reply_text('HERE ARE THE MENUS: ',reply_markup=InlineKeyboardMarkup(menu))
def helper(update,context):
    pass
def reply_method(update:Update,context)->None:
    user_message = update.message.text.lower()
    if user_message in ('hello','hi'):
        update.message.reply_text('Hello there')
def call_handler(update:Update,context:callbackcontext)->None:
    print(f'This is an Update from callbackquery {update}')
    my_query  = update.callback_query
    my_query.answer()
    if my_query.data == 'menu2':
        my_query.edit_message_text("OOh you selected Menu 2",reply_markup=InlineKeyboardMarkup([]))
 
if __name__=='__main__':
    updater = Updater(token=bot_token,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('getstarted',start_method))
    dp.add_handler(CommandHandler('help',helper))
    dp.add_handler(MessageHandler(Filters.text,reply_method))
    # this is callback handler
    dp.add_handler(CallbackQueryHandler(call_handler))
    updater.start_polling()
    updater.idle()