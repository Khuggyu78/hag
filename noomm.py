import requests
import re
import telebot
import os
bot = telebot.TeleBot("5218688832:AAFEDBG9Udpd_XSiZ470dSBQlp50L00FCjg")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message,"مرحباً في البوت")

@bot.message_handler(func=lambda m: True)
def get(message):
	res=requests.post(f"https://api.simsimi.net/v2/?text={message.text}&lc=en&cf=false").json()["success"]
	bot.reply_to(message,res)
	print(":)")

bot.polling(True)
