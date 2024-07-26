# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
# from config import bot_token
# import requests

# def start(update,context):
#     update.message.reply_text("Welcome on board")
#     menu = [[InlineKeyboardButton("Google Search", url="https://www.google.com")]]
#     update.message.reply_text("Please choose a button", reply_markup=InlineKeyboardMarkup(menu))
# def button(update:Update,context:CallbackContext):
#     query=update.callback_query
#     query=query.answer()
#     if query.data == "google":
#         # requests.get(query.url)
#         query.edit_message_text(text="You have selected Google Search")
# def main():
#     print("Bot started")
#     updater = Updater(token=bot_token, use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('start',start))
#     dp.add_handler(CallbackQueryHandler(button))
#     updater.start_polling()
#     updater.idle()
# if __name__=="__main__":
#     main()

import emoji

# Example string with emojis
example_string = "Hello World 🌍"

# Using replace_emoji to remove emojis
cleaned_string = emoji.replace_emoji(example_string, "")

print(cleaned_string)