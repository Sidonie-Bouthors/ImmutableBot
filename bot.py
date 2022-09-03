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

def start(update, context): 
  """reply when called upon for the first time"""
  update.message.reply_text("Who dare calls upon me")

def help(update, context):
  """do not offer help when help is requested"""
  update.message.reply_text(
    """You are not deserving of my help
    """, parse_mode="HTML")

def trial(update, context): 
  """trial time"""
  update.message.reply_text("Trial is in session!")

def error(update, context): 
  """error"""
  logger.error(f"Something is broken : {context.error}")

def main(): 
  # start the bot
  updater = Updater(TOKEN, use_context = True)

  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help))
  
  dp.add_error_handler(error)

  # updater.start_polling()

  updater.start_webhook(listen = '0.0.0.0', 
                        port = int(PORT), 
                        url_path = TOKEN)
  updater.bot.setWebhook('https://young-shore-01510.herokuapp.com/' + TOKEN)

  updater.idle()

if __name__ == '__main__': 
  main()
