import logging
from telegram.ext import *
import re,emoji,time
from config import bot_token,my_chat_id,ProjectInfo,about_section,demos, tech_urls
from telegram import InlineKeyboardButton , InlineKeyboardMarkup, Update , callbackquery

#swx@2WS
stack = []
callback_stack = []
logging.basicConfig(filename="lemi.txt",level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

project=''

def start(update,context) -> None:
    # swx@2WS
    # update.message.reply_text('Hello Welcome to my portfolio bot.')
    buttons = [[InlineKeyboardButton("✅ Yes",callback_data='yes'),InlineKeyboardButton('❌ No',callback_data='no')]]
    my_reply = InlineKeyboardMarkup(buttons)
    initial_message = 'Welcome to lemi\'s Portfolio Bot! 👋 Hello there! My name is Lemi Melkamu, and I\'m excited to show you around my portfolio through this bot. Whether you\'re looking for insights into my latest projects, wanting to learn more about my skills, or simply curious about what I do, I\'m here to guide you!'
    update.message.reply_text(text=f'{initial_message} \n Do you want to learn more about my projects?', reply_markup=my_reply)

def help(update,context):
    update.message.reply_text('This bot provides you with a list of my most recent projects.')
def user_message(update,context):
     pass
def project_details(update:Update, context:CallbackContext) -> None:
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
        ],
        [InlineKeyboardButton("⬅️ Back", callback_data="back")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('Select an option to learn more about the project:', reply_markup=reply_markup)
   
def my_handler(update: Update,context:CallbackContext) -> None: # type: ignore
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
        ],
        [InlineKeyboardButton("⬅️ Back", callback_data="back")]
    ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('choose the options please',reply_markup=reply_markup)
    if data == 'projects':
        menus = [[InlineKeyboardButton('JIT Library monitoring',callback_data='jit_library')],[InlineKeyboardButton('Chatbot system for organizations website',callback_data='chat_bot')],[InlineKeyboardButton('Proactive monitoring',callback_data='proactive')],
                 [InlineKeyboardButton("⬅️ Back", callback_data="back")]]
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
       data = stack.pop()      
    # if data == "project":
    #     my_handler(update,context)            
    if data == "about_me":
        text = about_section
        button = [[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
        query.edit_message_text(text=text)
        query.message.reply_markup(reply_markup=InlineKeyboardMarkup(button))
        
    if data == "contact_me":
                
        my_github = "https://github.com/lemidb"
        my_linkedin = "https://www.linkedin.com/in/lemidbgelnemerd2"
        my_twitter = "http://x.com/lemi_melkamu"
        my_gmail = "mailto:lemimelkamu@gmail.com"
        my_telegram = "https://t.me/@lemidb"

    # [InlineKeyboardButton("🐙 GitHub", url=my_github),
        contact_keyboard = [[InlineKeyboardButton("💼 LinkedIn", url = my_linkedin),InlineKeyboardButton("🐙 GitHub", url = my_github)],[InlineKeyboardButton("🐦 Twitter",url=my_twitter),InlineKeyboardButton("🛸 Telegram",url=my_telegram)],[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(contact_keyboard)
#         # chat_id=query.message.chat_id,message_id=query.message.message_id,
        query.edit_message_text(text='Here are my contact details:',reply_markup=reply_markup)
        # query.edit_message_text('Here is my email: {}'.format(my_gmail))
    if query.data == 'no':
        query.edit_message_text('OK please check out when you feel like to, anytime i\'m available thanks.')   


def print_and_return(value):
    print(f'## This tech values after filtered. {value}')
    return value

def clean_emoji(text):
    # return ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
        cleaned_text = emoji.replace_emoji(text, replace="")
        # Replace emojis with an empty string
        # cleaned_text = emoji_pattern.sub(r'', text)
        return cleaned_text
    
def handle_project_details(update: Update,context=CallbackContext) -> None:
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
                buttons = [[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
                reply_markup = InlineKeyboardMarkup(buttons)
                query.edit_message_text(text="DESCRIPTION for the project: {} :".format(project),reply_markup=reply_markup)
        if data =="technologies_used":
            technologies=ProjectInfo[project]['technologies']
            emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
            for tech in technologies:
                # cleaned_tech = emoji.replace_emoji(tech,'')
                cleaned_tech = clean_emoji(tech)
                # emoji_pattern.sub('',tech).strip()
            buttons = [[InlineKeyboardButton(tech, url=print_and_return(tech_urls[cleaned_tech]))] for tech in technologies]
            buttons.append([InlineKeyboardButton("⬅️ Back", callback_data="back")])
            reply_markup = InlineKeyboardMarkup(buttons)
            query.edit_message_text(text="Here are the technologies used for {}:".format(project),reply_markup=reply_markup)
        
        if data == "outcome":
            outcome=ProjectInfo[project]['outcome']
            buttons = [[InlineKeyboardButton(outcome,callback_data='outcome')],[InlineKeyboardButton("⬅️ Back", callback_data="back")]]
            reply_markup = InlineKeyboardMarkup(buttons)
            query.edit_message_text(text="Outcome of the project {}: ".format(project),reply_markup=reply_markup)
        if data == "demo":
            demo=ProjectInfo[project]['demo']
            demo_path = demos[demo]
            print(f"Here is the demo file: {demo_path}")
            if project == "chat_bot":
               context.bot.send_message(chat_id=query.message.chat_id, text="please wait while the video loads")   
            with open(f"{demo_path}",'rb') as video:
                context.bot.send_video(chat_id=query.message.chat_id, video=video, caption="Here's my demo for the {} project. Enjoy!".format(project))
        
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
    
    