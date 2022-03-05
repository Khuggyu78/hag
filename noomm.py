import requests
from telebot import types
import telebot
from time import sleep
import random
token = "5013418953:AAHj8R05EJ7msi6JX4pzAQ3n3g4JOuf0Jhc"
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- Get",callback_data = 'check')
#----#


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Welcome To Quran Bot  
Now Click Get. 
- - - - - - - - - - 
By  : @o4mrrr
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	combo(call.message)   	
def combo(message):
		bot.send_message(message.chat.id,"<strong>يتم العثور الرجاء الانتظار... </strong>",parse_mode="html")
		rl = random.randint(1,600)
		url = f"https://iuytiuyt.000webhostapp.com/newquran/{rl}.gif"
		bot.send_photo(message.chat.id,url,caption=f"<strong>Found Successfly. \nSorah Number : {rl}</strong>",parse_mode="html")
		bot.send_message(message.chat.id,"<strong>ادعي لـO4mr</strong>",parse_mode="html") 
		
    
pass

bot.polling(True)
