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
  "sylvain" : "CAACAgQAAxkBAAEFv7xjE5DxQaTd7Auri5FsHMSf_H9wygAC0woAAra-qFDvV1-zx6_HLykE"}

supremacyStickers = {
    "douchs" : "CAACAgQAAxkBAAEFwDBjE85Vqvuv1doSz3hbUfhqeJHHMgACGg0AAv3U8FD0INfU4047MSkE",
    "police" : "CAACAgQAAxkBAAEFwD5jE9ToUWPWRBM8SN93XKBxw2esiQACeQ4AAqCP4VDJc_52ogKXlSkE",
    "cap" : "CAACAgQAAxkBAAEFwEBjE9UH9EqpCSw4oHqXB8No32-0pwACAg8AAu2xeFEgTcBWepCKCCkE"
}

maiStickers = {
  "gay" : "CAACAgQAAxkBAAEFwB1jE8ll62np5bw1GSb7Is0pW66Q5QACzgsAAnHZ4FBw8LWarlpc-ykE",
  "sadge" : "CAACAgQAAxkBAAEFwB9jE8lxRTLAeOR47XfrAts-AlljLgACJwoAAgudsFAVhZgqZ46DhikE",
  "tirwed" : "CAACAgQAAxkBAAEFwDRjE8_5ffUrP-3xbH1paVMSFfCaYwACEQoAAi5AaFDM6Wnglkif7ykE",
  "happy" : "CAACAgQAAxkBAAEFwDZjE8_8M_Zu_50B267iu1wJ0kBMSgACsRMAAnOssVD63eo-raRwrykE",
  "fast" : "CAACAgQAAxkBAAEFwDhjE8_-opVHtKYYPvScg50s0LFAGQACXg0AAkVG4FB78iLdMI2cGykE"
}

cyrielleStickers = {
  "not hehe" : "CAACAgQAAxkBAAEFwBtjE8eJPmfCPSULZas6K7CK7uuxbwACgwwAAjcQ8FD8WTJixoO_9CkE",
  "aie" : "CAACAgQAAxkBAAEFwBljE8eHYOjUIhljmH2WGZecAif62wACSw0AApvA8VAAAScgDvSNStYpBA",
  "no spray" : "CAACAgQAAxkBAAEFwCZjE8puZUyvPonz-ly4KXMX8XagVAACOQ4AAn99sFDTRqqD6tXZfSkE"
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

##### The Class Stickers #####
def rocketscience(update, context):
  update.message.reply_sticker(theClassStickers["rocket"], quote=False)
def cute(update, context):
  update.message.reply_sticker(theClassStickers["turtle"], quote=False)
def hullo(update, context):
  update.message.reply_sticker(theClassStickers["bird"], quote=False)
def weird(update, context):
  update.message.reply_sticker(theClassStickers["man"], quote=False)
def sad(update, context):
  update.message.reply_sticker(theClassStickers["cry"], quote=False)
def jacopo(update, context):
  update.message.reply_sticker(theClassStickers["jacopo"], quote=False)
def crise(update, context):
  update.message.reply_sticker(theClassStickers["barbacrise"], quote=False)
def german(update, context):
  update.message.reply_sticker(theClassStickers["german"], quote=False)
def justdoit(update, context):
  update.message.reply_sticker(theClassStickers["sylvain"], quote=False)

#### Cyrielle's Stickers #####
def hehe(update, context):
  if not update.message.from_user.username == "sidonie_b" :
    update.message.reply_sticker(cyrielleStickers["not hehe"], quote=False)
def aie(update, context):
  update.message.reply_sticker(cyrielleStickers["aie"], quote=False)
def nospray(update, context):
  update.message.reply_sticker(cyrielleStickers["no spray"], quote=False)

##### Supremacy Stickers #####
def douchs(update, context):
  update.message.reply_sticker(supremacyStickers["douchs"], quote=False)
def police(update, context):
  update.message.reply_sticker(supremacyStickers["police"], quote=False)
def cap(update, context):
  update.message.reply_sticker(supremacyStickers["cap"], quote=False)

##### Maï's Stickers #####
def sadge(update, context):
  update.message.reply_sticker(maiStickers["sadge"], quote=False)
def gay(update, context):
  update.message.reply_sticker(maiStickers["gay"], quote=False)
def fast(update, context):
  update.message.reply_sticker(maiStickers["fast"], quote=False)
def happy(update, context):
  update.message.reply_sticker(maiStickers["happy"], quote=False)
def tirwed(update, context):
  update.message.reply_sticker(maiStickers["tirwed"], quote=False)

def disapproval(update, context):
  if not update.message.from_user.username == "sidonie_b" :
    update.message.reply_text("*Disapproval*")

def trial(update, context):
  update.message.reply_text("Trial is in session!")

def error(update, context):
  logger.error(f"You broke something, fix it : {context.error}")

def main(): 
  # start the bot
  updater = Updater(TOKEN, use_context = True)

  dp = updater.dispatcher

  # dp.add_handler(CommandHandler("start", start))
  # dp.add_handler(CommandHandler("help", help))
  dp.add_handler(CommandHandler("trial", trial))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"caffeine", re.IGNORECASE))
				| Filters.regex(re.compile(r"coffee", re.IGNORECASE))
				| Filters.regex(re.compile(r"café", re.IGNORECASE))
				| Filters.regex(re.compile(r"caféine", re.IGNORECASE))
				| Filters.regex(re.compile(r"maté", re.IGNORECASE))
				| Filters.regex(re.compile(r"secte", re.IGNORECASE))
				| Filters.regex(re.compile(r"culte", re.IGNORECASE)), disapproval))

  # hehe
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"hehe", re.IGNORECASE)), hehe))
  # aie aie aie
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"aie aie aie", re.IGNORECASE))
                                | Filters.regex(re.compile(r"aïe aïe aïe", re.IGNORECASE)), aie))
  # no shrug
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"shrug", re.IGNORECASE)), nospray))
  # no shower
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"douchs", re.IGNORECASE)), douchs))
  # cap
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"cap", re.IGNORECASE))
                                | Filters.regex(re.compile(r"casquette", re.IGNORECASE)), cap))
  # police
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"police", re.IGNORECASE))
                                | Filters.regex(re.compile(r"st sulpice", re.IGNORECASE)), police))
  
  # maï sticker reactions
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"sadge", re.IGNORECASE)), sadge))
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"gay", re.IGNORECASE)), gay))
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"tired", re.IGNORECASE))
                                | Filters.regex(re.compile(r"tirwed", re.IGNORECASE)), tirwed))
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"happy", re.IGNORECASE))
                                | Filters.regex(re.compile(r"h^^py", re.IGNORECASE)), happy))
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"fast", re.IGNORECASE)), fast))
  
  # immutable sticker reactions
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"rocket science", re.IGNORECASE))
                                | Filters.regex(re.compile(r"space", re.IGNORECASE))
                                | Filters.regex(re.compile(r"nerd", re.IGNORECASE)), rocketscience))
  
  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"cute", re.IGNORECASE))
                                | Filters.regex(re.compile(r"aww", re.IGNORECASE))
                                | Filters.regex(re.compile(r"turtle", re.IGNORECASE)), cute))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"immutable", re.IGNORECASE))
                                | Filters.regex(re.compile(r"immubot", re.IGNORECASE))
                                | Filters.regex(re.compile(r"birb", re.IGNORECASE)), hullo))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"weird", re.IGNORECASE))
                                | Filters.regex(re.compile(r"clotilde", re.IGNORECASE))
                                | Filters.regex(re.compile(r"kluter", re.IGNORECASE)), weird))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"triste", re.IGNORECASE))
                                | Filters.regex(re.compile(r"ça dégoute", re.IGNORECASE))
                                | Filters.regex(re.compile(r"dégoute", re.IGNORECASE))
                                | Filters.regex(re.compile(r"degoute", re.IGNORECASE))
                                | Filters.regex(re.compile(r"tristitude", re.IGNORECASE)), sad))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"wtf", re.IGNORECASE))
                                | Filters.regex(re.compile(r"i never lie", re.IGNORECASE))
                                | Filters.regex(re.compile(r"never lied", re.IGNORECASE))
                                | Filters.regex(re.compile(r"andiamo", re.IGNORECASE))
                                | Filters.regex(re.compile(r"aggiudi cato", re.IGNORECASE))
                                | Filters.regex(re.compile(r"big fan of harm", re.IGNORECASE))
                                | Filters.regex(re.compile(r"bitch i lie all the time too", re.IGNORECASE)), jacopo))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"barbacrise", re.IGNORECASE))
                                | Filters.regex(re.compile(r"barbapapa", re.IGNORECASE))
                                | Filters.regex(re.compile(r"terrible", re.IGNORECASE)), crise))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"glutentag", re.IGNORECASE))
                                | Filters.regex(re.compile(r"allemand", re.IGNORECASE)), german))

  dp.add_handler(MessageHandler(Filters.regex(re.compile(r"just do it", re.IGNORECASE))
                                | Filters.regex(re.compile(r"zylvanos", re.IGNORECASE)), justdoit))
  
  dp.add_error_handler(error)

  updater.start_webhook(listen = '0.0.0.0', 
                        port = int(PORT), 
                        url_path = TOKEN,
                        webhook_url=('https://young-shore-01510.herokuapp.com/' + TOKEN))

  updater.idle()

if __name__ == '__main__': 
  main()
