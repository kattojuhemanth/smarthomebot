import os
from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
user = os.getenv('user')
api = os.getenv('api')
aio = Client(user, api)
light = aio.feeds('light')
fan = aio.feeds('fan')
def start(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Please type in /help for the help reg. the commands of bot')
  print('STARTED')
def hel(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text("Commands\n\tfor turning on the light - '/Turnonlight'\n\tfor turning off the light - '/Turnofflight'\n\tfor turning on the fan - '/Turnonfan'\n\tfor turning off the fan - '/Turnofffan'")
  print('HELPED')
def lon(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(light.key, 1)
  bot.message.reply_text("Okay, turning on the light...\nCommands\n\tfor turning on the light - '/Turnonlight'\n\tfor turning off the light - '/Turnofflight'\n\tfor turning on the fan - '/Turnonfan'\n\tfor turning off the fan - '/Turnofffan'")
  print('LIGHT ON')
def lof(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(light.key, 0)
  bot.message.reply_text("Okay, turning off the light...\nCommands\n\tfor turning on the light - '/Turnonlight'\n\tfor turning off the light - '/Turnofflight'\n\tfor turning on the fan - '/Turnonfan'\n\tfor turning off the fan - '/Turnofffan'")
  print('LIGHT OFF')
def fon(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(fan.key, 1)
  bot.message.reply_text("Okay, turning on the fan...\nCommands\n\tfor turning on the light - '/Turnonlight'\n\tfor turning off the light - '/Turnofflight'\n\tfor turning on the fan - '/Turnonfan'\n\tfor turning off the fan - '/Turnofffan'")
  print('FAN ON')
def fof(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(fan.key, 0)
  bot.message.reply_text("Okay, turning off the fan...\nCommands\n\tfor turning on the light - '/Turnonlight'\n\tfor turning off the light - '/Turnofflight'\n\tfor turning on the fan - '/Turnonfan'\n\tfor turning off the fan - '/Turnofffan'")
  print('FAN OFF')
def wrong(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text("Can't understand the input. Please type in /help for the help reg. the commands of bot")
  print('WRONG INPUT')
def main(bot,update):
  mes = bot.message.text
  if (mes == "/start" ):
    start(bot,update)
  elif (mes == "/help" ):
    hel(bot,update)
  elif (mes == "/Turnonlight" ):
    lon(bot,update)
  elif (mes == "/Turnofflight"):
    lof(bot,update)
  elif (mes == "/Turnonfan" ):
    fon(bot,update)
  elif (mes == "/Turnofffan" ):
    fof(bot,update)
  else :
    wrong(bot,update)
bot_token = '1964189139:AAHAieTfoTdxnvLokgKrRmPDYBSWk_W2nXs'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
