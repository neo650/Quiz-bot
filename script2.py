# from telethon import TelegramClient, events
# from telethon.tl.custom import Button
import configparser
# from random import randint

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


#### Access credentials
config = configparser.ConfigParser() # Define the method to read the configuration file
config.read('config.ini') # read config.ini file

api_id = config.get('default','api_id')
api_hash = config.get('default','api_hash')
BOT_TOKEN = config.get('default','BOT_TOKEN') 
weather_key = config.get('default','weather_key')

updater = Updater(BOT_TOKEN)

# client = TelegramClient('sessions/session_master', api_id, api_hash).start(bot_token=BOT_TOKEN)
# client = TelegramClient('Bot', api_id, api_hash).start(bot_token=BOT_TOKEN)
# client = TelegramClient('session_name', api_id, api_hash)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there! I'm a quiz bot. Type /quiz to start the quiz.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type /quiz to start the quiz. Answer the questions and earn points!")
    
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

def quiz_answer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello from quiz_answer!")

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, quiz_answer))

updater.start_polling()
updater.idle()



# Define the /start command
# @BotClient.on(events.NewMessage(pattern="^/string(?: |$)(.*)"))
# @client.on(events.NewMessage(pattern='/(?i)start')) 
# @client.on(events.NewMessage(pattern='/start')) 
# async def start(event):
#     sender = await event.get_sender()
#     SENDER = sender.id
#     text = "Quiz Bot 🤖 ready\n" +\
#         "\"<b>/time</b>\" → Find out what day it is, i'll even tell you the time!\n"+\
#         "\"<b>/weather CITY</b>\" → I will provide the weather forecast for the city you entered\n" +\
#         "\"<b>/quiz</b>\" → Let's play together!\n" 
#     await client.send_message(SENDER, text, parse_mode="HTML")
    

## Function that waits user event [press button]
# def press_event(user_id):
#     return events.CallbackQuery(func=lambda e: e.sender_id == user_id)


### MAIN
# if __name__ == '__main__':
#     print("bot started")
#     client.run_until_disconnected()
