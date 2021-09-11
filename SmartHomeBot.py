pip install adafruit-io
pip install python-telegram-bot==13.0
from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
aio = Client('heroofcentury', 'aio_SoFd54YBlUIIcmgGEK0I377LuKH8')
light = aio.feeds('light')
fan = aio.feeds('fan')
def start(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Please type in /help for the help reg. the commands of bot')
  print('STARTED')
def hel(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Commands\n\tTurn on light - LIGHT ON\n\tTurn off light - LIGHT OFF\n\tTurn on Fan - FAN ON\n\tTurn off fan - FAN OFF')
  print('HELPED')
def lon(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(light.key, 1)
  bot.message.reply_text('Okay, turning on the light...')
  print('LIGHT ON')
def lof(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(light.key, 0)
  bot.message.reply_text('Okay, turning off the light...')
  print('LIGHT OFF')
def fon(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(fan.key, 1)
  bot.message.reply_text('Okay, turning on the fan...')
  print('FAN ON')
def fof(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(fan.key, 0)
  bot.message.reply_text('Okay, turning off the fan...')
  print('FAN OFF')
def main(bot,update):
  mes = bot.message.text
  if (mes == "/start" ):
    start(bot,update)
  elif (mes == "/help" ):
    hel(bot,update)
  elif (mes == "Turn on light" ):
    lon(bot,update)
  elif (mes == "Turn off light"):
    lof(bot,update)
  elif (mes == "Turn on fan" ):
    fon(bot,update)
  elif (mes == "Turn off fan" ):
    fof(bot,update)
bot_token = '1964189139:AAHAieTfoTdxnvLokgKrRmPDYBSWk_W2nXs'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()