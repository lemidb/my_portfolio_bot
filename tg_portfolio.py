import logging
from telegram.ext import *
from config import bot_token,my_chat_id,ProjectInfo,about_section,demos
from telegram import InlineKeyboardButton , InlineKeyboardMarkup, Update , callbackquery
#swx@2WS
stack = []

logging.basicConfig(filename="lemi.txt",level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

project=''

def start(update,context):
    # swx@2WS
    # update.message.reply_text('Hello Welcome to my portfolio bot.')
    buttons = [[InlineKeyboardButton("✅ Yes",callback_data='yes'),InlineKeyboardButton('❌ No',callback_data='no')]]
    my_reply = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Welcome to lemi\'s Portfolio Bot! 👋 Hello there! My name is Lemi Melkamu, and I\'m excited to show you around my portfolio through this bot. Whether you\'re looking for insights into my latest projects, wanting to learn more about my skills, or simply curious about what I do, I\'m here to guide you!')
    update.message.reply_text('Do you want to learn more about my projects?', reply_markup=my_reply)
def help(update,context):
    update.message.reply_text('This bot provides you with a list of my most recent projects.')
def user_message(update,context):
    user_msg = update.message.text.lower()

def project_details(update:Update, context:CallbackContext):
    # swx@2WS
    query = update.callback_query
    print('We are in project details method now')
    keyboard = [
        [
            InlineKeyboardButton("📝 Project Description", callback_data='project_description'),
            InlineKeyboardButton("💻 Technologies Used", callback_data='technologies_used'),
        ],
        [
            InlineKeyboardButton("📈 Outcome", callback_data='outcome'),
            InlineKeyboardButton("💡 Code Snippets/Demos", callback_data='demo'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('Select an option to learn more about the project:', reply_markup=reply_markup)
    
def my_handler(update: Update,context:CallbackContext):
    # swx@2WS 
    query = update.callback_query
    query.answer()
    data = query.data
    print(f'Query data : {data}   is selected')
    if data == 'yes':
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
    if data == 'projects':
        menus = [[InlineKeyboardButton('JIT LIBRARY MONITORING',callback_data='jit_library')],[InlineKeyboardButton('CHATBOT SYSTEM FOR ORGANIZATIONS WEBSITE',callback_data='chat_bot')],[InlineKeyboardButton('PROACTIVE MONITORING',callback_data='proactive')]]
        reply_markup = InlineKeyboardMarkup(menus)
        query.edit_message_text('Here are some of my projects',reply_markup=reply_markup)
    if data == 'jit_library':
        stack.append(query.data)
        project_details(update,context)
    if data == 'chat_bot':
        stack.append(query.data)
        project_details(update,context)
    if data == 'proactive':
        stack.append(query.data)
        project_details(update,context)
           
    if data == 'project_description':
        handle_project_details(update,context)
    if data == 'technologies_used':
        handle_project_details(update,context)
    if data == 'outcome':
        handle_project_details(update,context)
    if data == 'demo':
        handle_project_details(update,context)
    if data == "back":
            project_details(update,context)         
    if data == "about_me":
        text = about_section
        query.edit_message_text(text=text)
    if data == "contact_me":
        my_github = "https://github.com/lemidb"
        my_linkedin = "https://www.linkedin.com/in/lemidbgelnemerd2"
        my_twitter = "http://x.com/lemi_melkamu"
        my_gmail = "mailto:lemimelkamu@gmail.com"
        contact_keyboard = [
    [InlineKeyboardButton("🐙 GitHub", url=my_github)],
     [InlineKeyboardButton("💼 LinkedIn", url=my_linkedin)],
    [InlineKeyboardButton("🐦 Twitter", url=my_twitter)],
    [InlineKeyboardButton("📧 Gmail", url=my_gmail)]
]
        reply_markup = InlineKeyboardMarkup(contact_keyboard)
        query.edit_message_text(text="Here are my contact details:",reply_markup=reply_markup)
    if query.data == 'no':
        query.edit_message_text('OK please check out when you feel like to, anytime i\'m available thanks.')

def handle_project_details(update: Update,context=CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data
    print('## Stack status: ',stack)
    global project
    if stack:
        project = stack.pop()
    print(f"Here is the last selected project: {project}")
    if project in ProjectInfo.keys():
        if data == 'project_description':
            if project in ProjectInfo.keys():
                description=ProjectInfo[project]['description']
                buttons = [[InlineKeyboardButton("Back", callback_data="back")]]
                reply_markup = InlineKeyboardMarkup(buttons)
                query.edit_message_text(text="DESCRIPTION for the project: {} :".format(project),reply_markup=reply_markup)
        if data =="technologies_used":
            technologies=ProjectInfo[project]['technologies']
            buttons =[ [InlineKeyboardButton(str(tech),callback_data=tech) for tech in technologies] ]
            buttons.append([InlineKeyboardButton("Back", callback_data="back")])
            reply_markup = InlineKeyboardMarkup(buttons)
            query.edit_message_text(text="Here are the technologies used for {}:".format(project),reply_markup=reply_markup)
        if data == "outcome":
            outcome=ProjectInfo[project]['outcome']
            buttons = [[InlineKeyboardButton(outcome,callback_data='outcome')],[InlineKeyboardButton("Back", callback_data="back")]]
            reply_markup = InlineKeyboardMarkup(buttons)
            query.edit_message_text(text="Outcome of the project {}: ".format(project),reply_markup=reply_markup)
        if data == "demo":
            demo=ProjectInfo[project]['demo']
            demo_path = demos[demo]
            print(f"Here is the demo file: {demo_path}")
            with open(f"{demo_path}",'rb') as video:
                #  query.message.reply_audio(audio,caption="Here's the one-minute video. Enjoy!")
                #  query.message.reply_audio(video,caption="Here is my demo for {} project. ".format(project))
                context.bot.send_video(chat_id=query.message.chat_id, video=video, caption="Here's my demo for the {} project. Enjoy!".format(project))
            # buttons = [[InlineKeyboardButton("Back", callback_data="back")]]
            # reply_markup = InlineKeyboardMarkup(buttons)
            # query.edit_message_text(text="Here is the demo for {} project".format(project),reply_markup=reply_markup)
        
def error_handler(update: Update, context: CallbackContext) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    # Optionally, send a notification to the developer
    dev_chat_id = my_chat_id  # Replace with your chat ID
    context.bot.send_message(chat_id=dev_chat_id, text=f'An error occurred: {str(context.error)}')

def main():
    updater = Updater(token=bot_token,use_context=True)
    dp = updater.dispatcher   
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(MessageHandler(Filters.text,user_message))
    dp.add_handler(CallbackQueryHandler(my_handler))
    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    print('Bot started ...')
    main()