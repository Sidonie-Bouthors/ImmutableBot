# ImmutableBot
# Sidonie Bouthors

import logging
import requests
import random
import os
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', 5000))
# PORT = int(os.environ.get('PORT', 8443))
TOKEN = "5663089404:AAGO-_fsJfZkMTKLF5XijNvDLPgc_F8Iil4"


# Enable logging
logging.basicConfig(format = "%(asctime)s - %(name)s - %(levelname)s  - %(message)s", 
                    level = logging.INFO)

logger = logging.getLogger(__name__)

helpfulMood = False
theClassStickers = {
  "rocket" : "CAACAgQAAxkBAAEFv6xjE5C5lhvQHF9vTLzKSYpb0LPtHwACyAsAAsH_oVABPRbhJX7PtikE",
  "turtle" : "CAACAgQAAxkBAAEFv65jE5DSt-GVLH4lXgoFZqXamOhstQACxwwAAl6eqFBd0IREErULECkE",
  "bird" : "CAACAgQAAxkBAAEFv7BjE5Dm5svcfZDifjqvimBsqVNxiQACugoAAnAFqFDkbcaNnqE3NSkE",
  "man" : "CAACAgQAAxkBAAEFv7JjE5DoAY7UF6ajcFjTxSv9SXcSsQAC_w0AAuqfoVDUaXef2lbKZikE",
  "cry" : "CAACAgQAAxkBAAEFv7RjE5DqnBTCxjZifRSl4UmRi0d8WAACZQwAAoGZoVCsHPqFg2iyECkE",
  "jacopo" : "CAACAgQAAxkBAAEFv7ZjE5DseHrs2hOqnvK6-iPII8oBKQACzAwAAtm9qFDeaa5Y86pQbSkE",
  "barbacrise" : "CAACAgQAAxkBAAEFv7hjE5DtW7QN5rIx8Vh1AXoZ6nM7XwAC5QsAAqDmqVCnEArJAR84gykE",
  "german" : "CAACAgQAAxkBAAEFv7pjE5DvyRrOfoMY8CASSvpYD8ubOgACRw8AAsHioFAx5z9yMbh5ISkE",
  "sylvain" : "CAACAgQAAxkBAAEFv7xjE5DxQaTd7Auri5FsHMSf_H9wygAC0woAAra-qFDvV1-zx6_HLykE"
}

def start(update, context): 
  """reply when called upon for the first time"""
  update.message.reply_text("Who dares call upon me")

def help(update, context):
  """offer help when help is requested? maybe"""
  if (helpfulMood) :
    update.message.reply_text(
      """Fine, I shall help you
      """, parse_mode="HTML")
  else :
    update.message.reply_text(
      """You don't deserve my help
      """, parse_mode="HTML")

def rocketscience(update, context):
  update.message.reply_sticker(theClassStickers["rocket"], quote=False)
def cute(update, context):
  update.message.reply_sticker(theClassStickers["turtle"], quote=False)
def hullo(update, context):
  update.message.reply_sticker(theClassStickers["bird"], quote=False)
def weird(update, context):
  update.message.reply_sticker(theClassStickers["man"], quote=False)
def sadge(update, context):
  update.message.reply_sticker(theClassStickers["cry"], quote=False)
def wtf(update, context):
  update.message.reply_sticker(theClassStickers["jacopo"], quote=False)
def crise(update, context):
  update.message.reply_sticker(theClassStickers["barbacrise"], quote=False)
def german(update, context):
  update.message.reply_sticker(theClassStickers["german"], quote=False)
def justdoit(update, context):
  update.message.reply_sticker(theClassStickers["sylvain"], quote=False)

def sus(update, context):
  """suspicious"""
  update.message.reply_text("*Disapproval*")

def trial(update, context): 
  """trial time"""
  update.message.reply_text("Trial is in session!")

def error(update, context): 
  """error"""
  logger.error(f"You broke something, fix it : {context.error}")

def main(): 
  # start the bot
  updater = Updater(TOKEN, use_context = True)

  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help))
  dp.add_handler(CommandHandler("trial", trial))

  dp.add_handler(MessageHandler(Filters.regex(r"caffeine")
				| Filters.regex(r"coffee")
				| Filters.regex(r"café")
				| Filters.regex(r"caféine")
				| Filters.regex(r"maté")
				| Filters.regex(r"secte")
				| Filters.regex(r"culte"), sus))

  # sticker reactions
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"rocket science", re.IGNORECASE))
                                | Filters.regex(re.compile(r"space", re.IGNORECASE)), rocketscience))
  
  '''
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"rocket science", re.IGNORECASE)), rocketscience))
  
  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"cute", re.IGNORECASE)), cute))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"immutable", re.IGNORECASE))
                                | filters.Regex(re.compile(r"birb", re.IGNORECASE)), hullo))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"weird", re.IGNORECASE)), weird))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"sadge", re.IGNORECASE))
                                | filters.Regex(re.compile(r"ça dégoute", re.IGNORECASE)), sadge))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"wtf", re.IGNORECASE)), wtf))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"barbacrise", re.IGNORECASE)), crise))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"glutentag", re.IGNORECASE)), german))

  dp.add_handler(MessageHandler(filters.Regex(re.compile(r"just do it", re.IGNORECASE)), justdoit))
  '''
  dp.add_error_handler(error)

  updater.start_webhook(listen = '0.0.0.0', 
                        port = int(PORT), 
                        url_path = TOKEN,
                        webhook_url=('https://young-shore-01510.herokuapp.com/' + TOKEN))

  updater.idle()

if __name__ == '__main__': 
  main()
