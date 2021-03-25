import telebot
import time
bot = telebot.TeleBot(" ") #Add telegram bot token here

#Welcome message to /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome!")

#reply to /city1
@bot.message_handler(commands=['city1'])
def wcity1(message):
		FileCity1=open('FileCity1.txt','r')
		bot.reply_to(message, FileCity1.read())
		FileCity1.close()

#reply to /city2
@bot.message_handler(commands=['city2'])
def wcity2(message):
		FileCity2=open('FileCity2.txt','r')
		bot.reply_to(message, FileCity2.read())
		FileCity2.close()

print("Telegram bot working") 

from requests import ConnectionError
while True: #Fixes 'ConnectionError' from telegram bot
	try:
		bot.polling()
		break
	except ConnectionError:
		print("Connection error. Trying again...")
		time.sleep(1) 


