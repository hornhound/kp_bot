import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import psycopg2
import urlparse
import random
import os
#Initialization for webhook
TOKEN = '459235062:AAHdk58qLQc0MiTkgPgh5c6wPKCXUpn7nNg'
PORT = int(os.environ.get('PORT', '5000'))


bot = telegram.Bot(token = TOKEN)
updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher
bot.setWebhook(webhook_url = "https://willson-kp-bot.herokuapp.com/" + TOKEN)

def start(bot,update):
	bot.sendMessage(chat_id = update.message.chat_id,
					text = "Hello %s! My one and only job is to kp Willson whenever he talks."%update.message.from_user.first_name)


def kp(bot,update):
	list_of_insults = ["stfu", "FUck you"]
	bot.sendMessage(chat_id = update_message.chat_id, text = update.message.from_user.username)
	if update.message.from_user.username == "Willsoncy":
		idx = random.randint(0,1)
		bot.sendMessage(chat_id = update.message.chat_id, text = list_of_insults[idx]+' '+update.message.from_user.first_name,reply_to_message_id=update.message.message_id)


dispatcher.add_handler(CommandHandler('start', start))
kp_handler = MessageHandler(Filters.text,kp)
dispatcher.add_handler(kp_handler)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://vays-meetupbot.herokuapp.com/" + TOKEN)
updater.idle()

