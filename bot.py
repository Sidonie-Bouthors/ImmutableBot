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
XKCD_CURRENT_URL = "https://xkcd.com/info.0.json"
XKCD_URL1 = "https://xkcd.com/"
XKCD_URL2 = "/info.0.json"


# Enable logging
logging.basicConfig(format = "%(asctime)s - %(name)s - %(levelname)s  - %(message)s", 
                    level = logging.INFO)

logger = logging.getLogger(__name__)

reactive = True
helpfulMood = False

classPack = {
  "rocket"      : "CAACAgQAAxkBAAEFv6xjE5C5lhvQHF9vTLzKSYpb0LPtHwACyAsAAsH_oVABPRbhJX7PtikE",
  "turtle"      : "CAACAgQAAxkBAAEFv65jE5DSt-GVLH4lXgoFZqXamOhstQACxwwAAl6eqFBd0IREErULECkE",
  "bird"        : "CAACAgQAAxkBAAEFv7BjE5Dm5svcfZDifjqvimBsqVNxiQACugoAAnAFqFDkbcaNnqE3NSkE",
  "man"         : "CAACAgQAAxkBAAEFv7JjE5DoAY7UF6ajcFjTxSv9SXcSsQAC_w0AAuqfoVDUaXef2lbKZikE",
  "cry"         : "CAACAgQAAxkBAAEFv7RjE5DqnBTCxjZifRSl4UmRi0d8WAACZQwAAoGZoVCsHPqFg2iyECkE",
  "jacopo"      : "CAACAgQAAxkBAAEFv7ZjE5DseHrs2hOqnvK6-iPII8oBKQACzAwAAtm9qFDeaa5Y86pQbSkE",
  "barbacrise"  : "CAACAgQAAxkBAAEFv7hjE5DtW7QN5rIx8Vh1AXoZ6nM7XwAC5QsAAqDmqVCnEArJAR84gykE",
  "german"      : "CAACAgQAAxkBAAEFv7pjE5DvyRrOfoMY8CASSvpYD8ubOgACRw8AAsHioFAx5z9yMbh5ISkE",
  "sylvain"     : "CAACAgQAAxkBAAEFv7xjE5DxQaTd7Auri5FsHMSf_H9wygAC0woAAra-qFDvV1-zx6_HLykE"
  }

maiPack = {
  "tirwed"  : "CAACAgQAAxkBAAEFwDRjE8_5ffUrP-3xbH1paVMSFfCaYwACEQoAAi5AaFDM6Wnglkif7ykE",
  "happy"   : "CAACAgQAAxkBAAEFwDZjE8_8M_Zu_50B267iu1wJ0kBMSgACsRMAAnOssVD63eo-raRwrykE",
  "sadge"   : "CAACAgQAAxkBAAEFwB9jE8lxRTLAeOR47XfrAts-AlljLgACJwoAAgudsFAVhZgqZ46DhikE",
  "fast"    : "CAACAgQAAxkBAAEFwDhjE8_-opVHtKYYPvScg50s0LFAGQACXg0AAkVG4FB78iLdMI2cGykE",
  "gay"     : "CAACAgQAAxkBAAEFwB1jE8ll62np5bw1GSb7Is0pW66Q5QACzgsAAnHZ4FBw8LWarlpc-ykE"
  }

supremacyPack = {
  "piazza bean"     :"CAACAgQAAxkBAAEFwKxjFHM7Pddle1wo7polaIZEnkxXZwAClw4AAkFOaFD4uNZmbs25fykE",
  "killer urs"      : "CAACAgQAAxkBAAEFwK5jFHNGzXsLvjZJwhM91m9nLyH1tAACTQoAAsmlaVCGv5FT1HtorikE",
  "jeanne"          : "CAACAgQAAxkBAAEFwLBjFHNQykP0vkhJ9qDc9OnZJC0RbQACnwwAAg7OaVBIJPZRQb64dSkE",
  "schinz"          : "CAACAgQAAxkBAAEFwLRjFHNZWC6UTIaYtApKW66wiH6tJwACBQwAAhjTaFDfzJYWy0T0xCkE",
  "futur blanc"     : "CAACAgQAAxkBAAEFwLZjFHNhc965s8bmtmzWA8v6HLm0-gACdQ8AAr7iaFASElc2isAUESkE",
  "dé pet dé"       : "CAACAgQAAxkBAAEFwLhjFHOzgPTsypRV-HmFpAQYw16C2gADDQACk_toUBSOJXdEqJFVKQQ",
  "space"           : "CAACAgQAAxkBAAEFwLpjFHPBKVu3bumDHs2A9BszsfWjmAAC_Q0AAgdSaVAmzr58BYQp5ikE",
  "sylvain omar"    : "CAACAgQAAxkBAAEFwLxjFHPKXjtw04ysL4BXUoXsclGJ2AACiA4AAkm5aVAyu-4KmjvUVikE",
  "hallucination"   : "CAACAgQAAxkBAAEFwL5jFHPUuCw0sfrQUkLwkP7GDopNggACCAsAAnOzaVDS6QR_sxKygSkE",
  "kluter"          : "CAACAgQAAxkBAAEFwMBjFHPdifvt6IgkV298ZTXqdRCDaAACowwAAmEuaVA1KNkZuNIkvikE",
  "rocket science"  : "CAACAgQAAxkBAAEFwMJjFHPtwUp7XH_g1Zk3VUMoQRP8BAACUgwAAm-DaVC5wN1R0_r4UikE",
  "stack tortoises" : "CAACAgQAAxkBAAEFwMRjFHP4-D_IZ-UZ7M8hDR4GnH2FFAACegwAAkSMaFBuN0RQ2MqM2SkE",
  "tortoise"        : "CAACAgQAAxkBAAEFwMZjFHQBPdWqun9QKODGGNHMNQ_xLAACkQsAAgGDaVCXDOHI8fYTQCkE",
  "ça dégoute"      : "CAACAgQAAxkBAAEFwMhjFHQKF-VYZ1k6tbGnx-rLR0_QPwACTQ0AAqBRcFAOt9QY45k1TCkE",
  "schedule laugh"  : "CAACAgQAAxkBAAEFwMpjFHQZOSgEX07_jLxdb7NJAAHp9P4AAnoMAAJO2IBQYelkahSLjtIpBA",
  "jeanne man 1"    : "CAACAgQAAxkBAAEFwMxjFHQjSwsg3dTFYxh4mONZNksSBwAC7AsAAoO4iVCA_FT00x_YnykE",
  "jeanne man 2"    : "CAACAgQAAxkBAAEFwM5jFHQs2nUZB9Lfa2JxncpDLN3MUgACOAwAArNygFCRt_0d9XCliSkE",
  "jeanne man 3"    : "CAACAgQAAxkBAAEFwNBjFHQ1z7llTgHQyuZxLeKBsnjfLgACkw8AAiILgVBDampUv3r1rCkE",
  "just do it"      : "CAACAgQAAxkBAAEFwNJjFHQ_X4p4DwLGoKHpGVs-HgXVXQACoQ4AAonBkVBfHM0gxJWP1ikE",
  "birb"            : "CAACAgQAAxkBAAEFwNZjFHRL8JT3hTgarNtfCsVCGMPlXgAC8gwAAu2QoFDNgtmXSgX87CkE",
  "barbacrise"      : "CAACAgQAAxkBAAEFwNhjFHSVuTN_UFoozpx2dY1tLavGFwACcQ8AAlgUmVCYq7aLu-hkPSkE",
  "weird man"       : "CAACAgQAAxkBAAEFwNpjFHSnxUhnuEYMJFdEPpt21Gi0hAACKg0AArkmmFDciRCLJt_qKikE",
  "glutentag"       : "CAACAgQAAxkBAAEFwNxjFHSu5iLSfbv3TDqdGr0qoF9NDQAChA0AAvrhoVCQPGuDcCULeykE",
  "allemand"        : "CAACAgQAAxkBAAEFwN5jFHS5xCYTB6VYV2Xn9upruJgxZwAClAsAAnN7sFCwsYXiSiNsYykE",
  "ptdsd"           : "CAACAgQAAxkBAAEFwOBjFHTDdC5baFlYvBToBYSspHtupAAC1woAAilRsVByzPkoxjJmAykE",
  "regenbogen"      : "CAACAgQAAxkBAAEFwOJjFHTk-zpWbFNZbLzlJwbp5zzEhwACeAwAAr64sFAG7DGrL5vfvCkE",
  "schrecklich"     : "CAACAgQAAxkBAAEFwORjFHTsBKS9Y0amgXmGBfjYTlPhYQACmwoAAqJssFAm3IqgATp12ykE",
  "jacoppoo"        : "CAACAgQAAxkBAAEFwOZjFHT0tQsvkIlQspHdzCC1l0bRlAACVgwAAqbawFDyomRZlZGgDikE",
  "behold jacopo"   : "CAACAgQAAxkBAAEFwOhjFHT80wn38_G1Uo3G8ssQ6BqXUQACuwwAAkRq4VDbq4y-5DJLuykE",
  "bad person"      : "CAACAgQAAxkBAAEFwOpjFHUE_ERVY9o7H7sGv88Zgqq01gACkwsAAijs2FBQ1uc4dbBHiykE",
  "bazooka"         : "CAACAgQAAxkBAAEFwOxjFHUNi1x54V7O_za1q6wGxGcZWgAC9g4AAiKs4VClW-W-Iiei5SkE",
  "police"          : "CAACAgQAAxkBAAEFwD5jE9ToUWPWRBM8SN93XKBxw2esiQACeQ4AAqCP4VDJc_52ogKXlSkE",
  "ci-git"          : "CAACAgQAAxkBAAEFwO5jFHUWtRGv4K99k0349id0K3hT2QAC-w0AArzm8FAZSHzSrbtJxCkE",
  "ci-git mdr"      : "CAACAgQAAxkBAAEFwPBjFHUgUWip8nlDSuNB-UY1BtlaggACvAwAAsDk6FBygI05T_IYgykE",
  "douchs"          : "CAACAgQAAxkBAAEFwDBjE85Vqvuv1doSz3hbUfhqeJHHMgACGg0AAv3U8FD0INfU4047MSkE",
  "cap"             : "CAACAgQAAxkBAAEFwEBjE9UH9EqpCSw4oHqXB8No32-0pwACAg8AAu2xeFEgTcBWepCKCCkE",
  "inginir"         : "CAACAgQAAxkBAAEFwPJjFHUtJlUM4yvHpgsuhCEFzGwq2gACBw0AAiyPeVE9JkGl8KeHTykE",
  "dont see it"     : "CAACAgQAAxkBAAEFwPRjFHU9cPlVpZf30yCVS3PfRRfPlgACYQ8AAgummFFJ_gkhhGI40ikE",
  "jeanne beans"    : "CAACAgQAAxkBAAEFwPZjFHXE_sXsD36CoNXKqpFzSL0jZwACOgsAArawmVFQtWYm9zhk5ykE",
  "blasphème pink"  : "CAACAgQAAxkBAAEFwPhjFHXPyvDbmsT9gY16bp9DQ1eRMQAClQsAAkj0mVGOaC7k8uLhHCkE",
  "blasphème jaune" : "CAACAgQAAxkBAAEFwPpjFHXcMDSayyM7dhk0_99f8lpEFgACtAwAAuCQmVFi8bVOG0K_9CkE",
  "sacrejaune"      : "CAACAgQAAxkBAAEFwPxjFHXePSZbZpu3pE3k1IqmjzY-UAACmwwAAnz-mVEFaLFC657yCikE",
  "sacrebleu"       : "CAACAgQAAxkBAAEFwP5jFHXfJDtmeeWIlmcD6nia9jw64AACAg4AAhi5mVE6d_x3US0zfSkE"
}

cyriellePack = {
  "not hehe"  : "CAACAgQAAxkBAAEFwBtjE8eJPmfCPSULZas6K7CK7uuxbwACgwwAAjcQ8FD8WTJixoO_9CkE",
  "aie"       : "CAACAgQAAxkBAAEFwBljE8eHYOjUIhljmH2WGZecAif62wACSw0AApvA8VAAAScgDvSNStYpBA",
  "no spray"  : "CAACAgQAAxkBAAEFwCZjE8puZUyvPonz-ly4KXMX8XagVAACOQ4AAn99sFDTRqqD6tXZfSkE"
}

def start(update, context):
  update.message.reply_text("Who dares call upon me")

def help(update, context):
  if helpfulMood :
    update.message.reply_text(
      """Fine, I shall help you
      """, parse_mode="HTML")
  else :
    update.message.reply_text(
      """You don't deserve my help
      """, parse_mode="HTML")

def regexFilter(main, *keywords) : 
  filters = Filters.regex(re.compile(main, re.IGNORECASE))
  for k in keywords :
    filters |= Filters.regex(re.compile(k, re.IGNORECASE))
  return filters
  
def autoMessage(message, *keywords, exceptUsers=[]) :
  dp.add_handler(MessageHandler(regexFilter(*keywords), reactText(message, exceptUsers)))

def reactText(message, exceptUsers):
  global reactive
  return lambda update, context : update.message.reply_text(message) \
                                    if (not update.message.from_user.username in exceptUsers) \
                                      and reactive \
                                    else None

def autoSticker(reaction, *keywords, exceptUsers=[]) :
  dp.add_handler(MessageHandler(regexFilter(*keywords), reactSticker(reaction, exceptUsers)))

def reactSticker(sticker, exceptUsers=[]):
  global reactive
  return lambda update, context : update.message.reply_sticker(sticker, quote=False) \
                                    if (not update.message.from_user.username in exceptUsers) \
                                      and reactive \
                                    else None

def trial(update, context):
  global reactive
  if reactive :
    update.message.reply_text("Trial is in session!")

def xkcd(update, context):
  curr = requests.get(XKCD_CURRENT_URL)
  curr_comic = curr.json()
  curr_num = curr_comic['num']
  rand = requests.get(XKCD_URL1 + random.randint(1, curr_num) + XKCD_URL2)
  rand_comic = rand.json()
  update.message.bot.send_photo(update.message.chat.id, rand_comic['img'])


def shutup(update, context):
  global reactive
  if reactive :
    reactive = False
    update.message.reply_text("Alright :') goodbye")
  else :
    update.message.reply_text("I'm already quiet :(")

def comeback(update, context):
  global reactive
  if not reactive :
    reactive = True
    update.message.reply_text("Hullo! I'm back :)")
  else :
    update.message.reply_text("I'm already right here :)")

def error(update, context):
  logger.error(f"You broke something, fix it : {context.error}")

##### MAIN #####
def main(): 
  updater = Updater(TOKEN, use_context = True)

  global dp
  dp = updater.dispatcher

  # dp.add_handler(CommandHandler("start", start))
  # dp.add_handler(CommandHandler("help", help))
  dp.add_handler(CommandHandler("trial", trial))
  dp.add_handler(CommandHandler("shutup", shutup))
  dp.add_handler(CommandHandler("comeback", comeback))
  dp.add_handler(CommandHandler("comic", xkcd))
  dp.add_handler(MessageHandler(regexFilter("shut up immubot"), shutup))
  dp.add_handler(MessageHandler(regexFilter("come back immubot"), comeback))

  autoMessage("*Disapproval*", "coffee", "caffeine", "café", "caféine", "maté", "secte", "culte", exceptUsers=["sidonie_b"])

  autoSticker(cyriellePack["not hehe"], "hehe", exceptUsers=["sidonie_b"])
  autoSticker(cyriellePack["aie"],      "aie aie aie", "aïe aïe aïe")
  autoSticker(cyriellePack["no spray"], "shrug")
  
  autoSticker(supremacyPack["bazooka"], "bazooka", "squirell", "boom")
  autoSticker(supremacyPack["douchs"],  "douchs")
  autoSticker(supremacyPack["cap"],     "cap", "casquette")
  autoSticker(supremacyPack["police"],  "police", "st sulpice")
  
  # maï sticker reactions
  autoSticker(maiPack["sadge"],   "sadge")
  autoSticker(maiPack["gay"],     "gay")
  autoSticker(maiPack["tirwed"],  "tired", "tirwed")
  autoSticker(maiPack["happy"],   "happy", "h\^\^py")
  autoSticker(maiPack["fast"],    "fast")
  
  # immutable sticker reactions
  autoSticker(classPack["rocket"],      "rocket science",
                                        "space", 
                                        "nerd")
  autoSticker(classPack["turtle"],      "cute", 
                                        "aww", 
                                        "turtle")
  autoSticker(classPack["bird"],        "immutable", 
                                        "immubot", 
                                        "birb")
  autoSticker(classPack["man"],         "weird", 
                                        "clotilde", 
                                        "kluter")
  autoSticker(classPack["cry"],         "triste", 
                                        "ça dégoute", 
                                        "dégoute", 
                                        "degoute", 
                                        "tristitude")
  autoSticker(classPack["jacopo"],      "wtf", 
                                        "i never lie", 
                                        "never lied", 
                                        "andiamo", 
                                        "aggiudi cato",
                                        "big fan of harm", 
                                        "bitch i lie all the time too")
  autoSticker(classPack["barbacrise"],  "barbacrise", 
                                        "barbapapa", 
                                        "terrible")
  autoSticker(classPack["german"],      "glutentag", 
                                        "allemagne")
  autoSticker(classPack["sylvain"],     "just do it", 
                                        "zylvanos")
  
  dp.add_error_handler(error)

  updater.start_webhook(listen = '0.0.0.0', 
                        port = int(PORT), 
                        url_path = TOKEN,
                        webhook_url=('https://young-shore-01510.herokuapp.com/' + TOKEN))

  updater.idle()

if __name__ == '__main__': 
  main()
