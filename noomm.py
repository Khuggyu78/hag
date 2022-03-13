import requests
from telebot import types
import telebot
from time import sleep
import random
import time
token = "5013418953:AAHj8R05EJ7msi6JX4pzAQ3n3g4JOuf0Jhc"
bot = telebot.TeleBot(token)
r=requests.session() 
kj1 = types.InlineKeyboardButton(text ="سورة قرآن",callback_data = 'check')
yt1 = types.InlineKeyboardButton(text ="آية قرآن",callback_data = 'i')
cr1 = types.InlineKeyboardButton(text ="قريباً..",callback_data = 'n')
me1 = types.InlineKeyboardButton(text ="عشوائي",callback_data = 'e')
asd=1

		
	
@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2#trakos
    maac.add(kj1,yt1, cr1, me1)
    bjj = message.chat.id
    messagee = bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Welcome To Quran Bot  
Now Click Get. 
- - - - - - - - - - 
By  : @O4mrrr
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'n':
    	co(call.message)
    if call.data == 'e':
    	com(call.message)
    if call.data == 'check':
    	combo(call.message)   	
    if call.data == 'i':
    	check(call.message)   	
def combo(message):
		bot.send_message(message.chat.id,"<strong>يتم العثور الرجاء الانتظار... </strong>",parse_mode="html")
		rl = random.randint(1,600)
		urlu = f"https://iuytiuyt.000webhostapp.com/newquran/{rl}.gif"
		bot.send_photo(message.chat.id,urlu,caption=f"<strong>Found Successfly. \nSorah Number : {rl}</strong>",parse_mode="html")
		bot.send_message(message.chat.id,"<strong>ادعي لـO4mr</strong>",parse_mode="html") 
def check(message):
		bot.send_message(message.chat.id,"<strong>يتم العثور الرجاء الانتظار... </strong>",parse_mode="html")
		urle = requests.get(f"https://soud.me/api/Quran").json()
		ab = urle["info"]['Ayah']
		bot.send_message(message.chat.id,"❀° ┄────────────────────────╮\n\n"+ab+"\n\n╰───────────────────────┄ °❀")
def co(message):
	   	bot.send_message(message.chat.id,"New Bot!!@Aqxvbot")	   	
	   	
def com(message):
    							zekr = requests.get('https://azkar-api.nawafhq.repl.co/zekr?json=true').json()['content']
    							bot.send_message(message.chat.id,zekr)
    						
    						
pass

bot.polling(True)
#By O4mr
