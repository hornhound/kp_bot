import telegram
from telegram.ext import Updater, CommandHandler
import psycopg2
import urlparse
import random

bot = telegram.Bot(token = "459235062:AAHdk58qLQc0MiTkgPgh5c6wPKCXUpn7nNg")
updater = Updater(token = "459235062:AAHdk58qLQc0MiTkgPgh5c6wPKCXUpn7nNg")
dispatcher = updater.dispatcher

def start(bot,update):
	bot.sendMessage(chat_id = update.message.chat_id,
					text = "Hello %s! My one and only job is to kp Willson whenever he talks."%update.message.from_user.first_name)


def kp(bot,update):
	list_of_insults = ["stfu", "FUck you"]
	if update.message.from_user.username == "Willsoncy":
		idx = random.randint(0,1)
		bot.sendMessage(chat_id = update.message.chat_id, text = list_of_insults[idx],reply_to_message_id=update.message.message_id)

