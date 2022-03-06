import requests
from telebot import types
import telebot
from time import sleep
import random
token = "5218688832:AAFEDBG9Udpd_XSiZ470dSBQlp50L00FCjg"
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="صورة قرآن",callback_data = 'check')
com = types.InlineKeyboardButton(text ="أية قرآن",callback_data = 'i')
#----#


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co,com)
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
		
    
pass

bot.polling(True)
