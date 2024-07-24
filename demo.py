from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from config import bot_token
# Example projects
projects = {
    "project1": {"name": "Project 1", "description": "Description of Project 1"},
    "project2": {"name": "Project 2", "description": "Description of Project 2"},
}

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton(project_id, callback_data=project_id)] for project_id in projects.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select a project:', reply_markup=reply_markup)
# swx@2WS
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    # Store the selected project ID in user_data
    print('User selected : ',query.data)
    context.user_data["selected_project"] = query.data
    # Display detailed information options
    keyboard = [
        [InlineKeyboardButton("📝 Project Description", callback_data='project_description'),
        InlineKeyboardButton("💻 Technologies Used", callback_data='technologies_used')],
        [InlineKeyboardButton("📈 Outcome", callback_data='outcome'),
        InlineKeyboardButton("💡 Code Snippets/Demos", callback_data='code_snippets_demos')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('Select an option to learn more about the project:', reply_markup=reply_markup)
    selected_project = context.user_data.get("selected_project")
    if selected_project == query.data:
        # Display the selected project's details based on the callback data
        if query.data == 'project_description':
            project_info = projects[selected_project]["description"]
            query.edit_message_text(f"{projects[selected_project]['name']}: {project_info}")
        # Add similar conditions for other callback data types 
# def handle_callback(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     query.answer()
    
#     # Retrieve the stored project ID
#     selected_project = context.user_data.get("selected_project")
#     if selected_project == query.data:
#         # Display the selected project's details based on the callback data
#         if query.data == 'project_description':
#             project_info = projects[selected_project]["description"]
#             query.edit_message_text(f"{projects[selected_project]['name']}: {project_info}")
#         # Add similar conditions for other callback data types
        
#     else:
#         query.edit_message_text("No active project found.")

def main():
    # Setup the dispatcher and register handlers
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    # dp.add_handler(CallbackQueryHandler(handle_callback))

    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    print('Bot started ...')
    main()