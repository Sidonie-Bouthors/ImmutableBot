# ImmutableBot
# Sidonie Bouthors

import logging
import requests
import random
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


PORT = int(os.environ.get('PORT', 5000))
TOKEN = "5663089404:AAGO-_fsJfZkMTKLF5XijNvDLPgc_F8Iil4"


# Enable logging
logging.basicConfig(format = "%(asctime)s - %(name)s - %(levelname)s  - %(message)s", 
                    level = logging.INFO)

logger = logging.getLogger(__name__)

helpfulMood = false

def start(update, context): 
  """reply when called upon for the first time"""
  update.message.reply_text("Who dares call upon me")

def help(update, context):
  """offer help when help is requested? maybe"""
  if (helfulMood) :
    update.message.reply_text(
      """Fine, I shall help you
      """, parse_mode="HTML")
  else :
    update.message.reply_text(
      """You are not deserving of my help
      """, parse_mode="HTML")

def sus(update, context):
  """suspicious"""
  update.message.reply_text("Suspicious activity detected. Beware!")

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

  dp.add_handler(MessageHandler(Filters.regex("caffeine")
				| Filters.regex("coffee")
				| Filters.regex("café")
				| Filters.regex("caféine")
				| Filters.regex("maté")
				| Filters.regex("secte")
				| Filters.regex("culte"), sus))
  
  dp.add_error_handler(error)

  # updater.start_polling()

  updater.start_webhook(listen = '0.0.0.0', 
                        port = int(PORT), 
                        url_path = TOKEN)
  updater.bot.setWebhook('https://young-shore-01510.herokuapp.com/' + TOKEN)

  updater.idle()

if __name__ == '__main__': 
  main()
