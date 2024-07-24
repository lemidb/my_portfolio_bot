from telegram.ext import *
from config import bot_token
from telegram import InlineKeyboardButton , InlineKeyboardMarkup, Update , callbackquery
#swx@2WS

def start(update,context):
    # update.message.reply_text('Hello Welcome to my portfolio bot.')
    buttons = [[InlineKeyboardButton("✅ Yes",callback_data='yes'),InlineKeyboardButton('❌ No',callback_data='no')]]
    my_reply = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Welcome to lemi\'s Portfolio Bot! 👋 Hello there! My name is Lemi Melkamu, and I\'m excited to show you around my portfolio through this bot. Whether you\'re looking for insights into my latest projects, wanting to learn more about my skills, or simply curious about what I do, I\'m here to guide you!')
    update.message.reply_text('Do you want to learn more about my projects?', reply_markup=my_reply)
def help(update,context):
    update.message.reply_text('This bot provides you with a list of my most recent projects.')
def user_message(update,context):
    user_msg = update.message.text.lower()
def my_handler(update: Update,context:CallbackContext):
    # swx@2WS
    query = update.callback_query
    query.answer()
    if query.data == 'yes':
        keyboard = [
        [
            InlineKeyboardButton("👤 About Me", callback_data='about_me'),
            InlineKeyboardButton("📁 Projects", callback_data='projects'),
        ],
        [
            InlineKeyboardButton("💼 Skills", callback_data='skills'),
            InlineKeyboardButton("✉️ Contact Me", callback_data='contact_me'),
        ]
    ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('Please choose:',reply_markup=reply_markup)
    if query.data == 'projects':
        #  swx@2WS
        menus = [[InlineKeyboardButton('JIT LIBRARY MONITORING',callback_data='jit_library')],[InlineKeyboardButton('CHATBOT SYSTEM FOR ORGANIZATIONS WEBSITE',callback_data='chat_bot')],[InlineKeyboardButton('PROACTIVE MONITORING',callback_data='proactive')]]
        reply_markup = InlineKeyboardMarkup(menus)
        query.edit_message_text('Here are some of my projects',reply_markup=reply_markup)
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