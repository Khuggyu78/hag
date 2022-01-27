
import aminofix
cl = aminofix.Client()
cl.login(email='cce64023ca@firemailbox.club',password='o123o123')
sub_cli = aminofix.SubClient(comId="89430311", profile=cl.profile)
print("done login")
import websocket
import requests
import amino
import json
import requests
from bs4 import BeautifulSoup
import urllib.parse 
import prsaw
from prsaw import RandomStuff
from random import randint
import giphy_client as gc


class Helper:
    def __init__(self, headers, client=None, sub=None, amino=None):
        self.headers = headers
        self.url = "wss://ws1.narvii.com"
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'
        self.client = client
        self.amino = amino

    def start_vc(self, comId: str, chatId: str, joinType: int = 1):
        websocket.enableTrace(True)
        ws = websocket.WebSocket()
        ws.connect(self.url, header=self.headers)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"
            },
            "t": 112
        }
        data = json.dumps(data)
        ws.send(data)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "channelType": 1,
                "id": "2154531"
            },
            "t": 108
        }
        data = json.dumps(data)
        ws.send(data)

    def end_vc(self, comId = None, chatId = None):
        websocket.enableTrace(True)
        websockets = websocket.WebSocket()
        websockets.connect(self.url, header=self.headers)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": 2,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = json.dumps(data)
        websockets.send(data)
        websockets.close()

    def send_message(self, comId: str, chatId: str, message: str, type: int = 0):
        data = {
            'content': message,
            'type': type,
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api + comId + self.chat + chatId}/message', data=data, headers=self.headers).text
        request = json.loads(r)
        return request

    def setCom(self, comId: str):
        self.sub = amino.SubClient(comId=comId, profile=self.client.profile)

import amino
import base64
import random
import wikipedia
from gtts import gTTS
import urllib.request

from collections import Counter

# login
Email = "cce64023ca@firemailbox.club"
Password = "o123o123"
# comId
comId = "89430311"
# orginal White list urls
vip = "http://aminoapps.com/p/4mawlv0"
# DeviceIds
dv = '22005E3894DC234AC731212A947611401ACBBAECBAE7D3D4CC2FE9913751F1AFB10F393FB1A2C313A7'

msg = f"""

[C]╭── ─ ────╌ ⃝🎭᭠〭ꨩ࿔〬 ──── ─ ──╮
[C].        °.    .      °    .         +         .           *        
[C]  .°   .        .          .°    .      °    .          
[C]• ﹝  𝗪𝗘𝗟𝗖𝗢𝗠𝗘   ﹞ •
[C]⬮ ⬯:: : : ::  ⬮ ⬯
[C]𝙴𝚗𝚕𝚒𝚐𝚑𝚝𝚎𝚗 𝚘𝚞𝚛 𝚏𝚘𝚛𝚞𝚖 
[C]𝚊𝚗𝚍 𝚑𝚘𝚙𝚎 𝚢𝚘𝚞 
[C]𝚎𝚗𝚓𝚘𝚢 𝚠𝚒𝚝𝚑 𝚞𝚜 
[C]𓇬:▒ ╌ ⃝💭࿔〬 ▒:𓇬
[C]. .  حـلـلتـم . . اهـلا . .
[C]. . ووطـئـتـم سـهـلا  . .
[C] ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜
[C]. . انرت دردشة البوت
[C]هـذا الـمكانان  هو الافضل لتعطي اوامرك لشخص لا يستطيع رفضها 
[C] ويمكنك كسب القروش المجانية كل 24 ساعة
[C]الرجاء قم بالألتزام بالقوانين
[c]يمكنك  الابلاغ عن اي خطأ عند المطور
[C] ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜
[C]𓇡𓇡𓍕𓇡𓇡𓍕𓇡𓇡𓇡𓇡𓍕𓇡𓇡𓍕𓇡𓇡
[C]༻༺
[C] 𓇡𓇡𓍕𓇡𓇡𓍕𓇡𓇡 𓍕𓇡𓇡𓍕𓇡𓇡
[C]• ﹝   𝗦𝗲𝗲 𝘆𝗼𝘂   ﹞ •
[C]⬮ ⬯:: : : ::  ⬮ ⬯
[C].        °.    .      °    .         +         .           *        
[C]  .°   .        .          .°    .      °    .           
[C]╰─── ─ ───  ╌ ⃝🎭᭠〭ꨩ࿔〬  ──── ─ ──╯

"""

client = amino.Client()
client.login(Email, Password)
aaa = Helper(headers=client.headers, client=client, amino=amino)
aaa.setCom(comId)
wikipedia.set_lang('ar')
vipId = client.get_from_code(vip).objectId
whiteList = [vipId]
blackList = ["aa4036ba-2571-4cbf-96c8-a16b672e44ce"]
sub = aaa.sub
print('Done')


@client.event('on_group_member_leave')
def on_group_member_leave(data: amino.objects.Event):
    author = data.message.author
    chatId = data.message.chatId
    msgG = f"""

[C] وداعاً 

[C] نتمنى عودتك باقرب وقت

"""
    sub.send_message(chatId=chatId, message=msgG)
@client.event('on_group_member_join')
def on_group_member_join(data: amino.objects.Event):
    author = data.message.author
    chatId = data.message.chatId
    url = author.userId
    url = client.get_from_id(url, 0, comId).shortUrl
    icon = urllib.request.urlopen(author.icon)
    sub.send_message(chatId=chatId, message=msg, embedTitle=author.nickname,embedLink="ndc://user-profile/"+author.userId)


@client.event('on_chat_tip')
def on_chat_tip(data: amino.objects.Event):
    msg = data.message
    coins = msg.extensions['tippingCoins']
    chatId = data.message.chatId
    author = data.message.author
    sub.send_message(chatId=chatId, message='[C]شكرا لك على ' + str(coins) + ' قرش' + '\n\n[C]' + author.nickname)


@client.event('on_text_message')
def on_text_message(data: amino.objects.Event):
    mention = data.message.mentionUserIds
    content = data.message.content
    msgId = data.message.messageId
    chatId = data.message.chatId
    author = data.message.author
    msg = data.message.content
    if author.userId in blackList: pass
    else:
        if 'ههه' in content:
            sub.send_message(chatId=chatId, message='دوم الضحكة', replyTo=msgId)
            
        if 'شادي' in content:
        	sub.send_message(chatId=chatId, message="""
[c]مرحباً انا 𝚂𝙷𝙰𝙳𝚈,كيف يمكنني مساعدتك!
[c]بداية الأمر (!)
[c]قائمة الأومر-
[c]-help 
[c]	
        	
        	
        	"""
        	, replyTo=msgId)
        if 'سار' in content:
        	sub.send_message(chatId=chatId, message="""
[c]أنا أسف أختي  قيد الأصلاح حالياً
        	
        	"""
        	, replyTo=msgId)
        if content.startswith('!follow'):
            if 'me' in content[8:11]: sub.follow(author.userId)
            else:
                ID = content[8:]
                ID = client.get_from_code(ID).objectId
                sub.follow(userId=ID)
            sub.send_message(chatId=chatId, message='تم متابعة العضو', replyTo=msgId)

        if content.startswith('!unfollow'):
            if 'me' in content[10:13]: sub.unfollow(author.userId)
            else:
                ID = content[10:]
                ID = client.get_from_code(ID).objectId
                sub.unfollow(userId=ID)
            sub.send_message(chatId=chatId, message='تم الغاء متابعة العضو', replyTo=msgId)
            
        if msg.startswith('!coins'):
        	sub.send_coins(coins=msg[7:],chatId=chatId,transactionId=client.userId)
        	
        if msg.startswith('!title'):
        	sub.edit_titles(userId=userId,titles=[msg[7:]],colors=['#000000'])        
 	   

        if content.startswith('!say'):
            if len(content) > 70: pass
            else:
                sayed = gTTS(content[5:], slow=False, lang='ja')
                sayed.save('sayed.mp3')
                with open('sayed.mp3', 'rb') as fp:
                    sub.send_message(chatId=chatId, file=fp, fileType='audio')
                os.remove('sayed.mp3')
              

        if content.startswith('!msg'):
        	mqa=content.replace('!msg','')
        	sub.send_message(chatId=chatId, message=mqa, replyTo=msgId)
        	
        if content.startswith('/'):
        	try:
        		rs = prsaw.RandomStuff("JnXcTIUCxvwj")
        		response =rs.get_ai_response(msg[1:])
        		msg = response[0]["message"]
        		sub.send_message(chatId,message=f"{msg}")
        	except Exception as c:
        		print(c)
        
        if msg.startswith("!covid"):
        	try:
        		country = msg[7:]
        		url = f"https://coronavirus-19-api.herokuapp.com/countries/{country}"
        		stats = requests.get(url)
        		json_stats = stats.json()
        		country = json_stats["country"]
        		totalCases = json_stats["cases"]
        		todayCases = json_stats["todayCases"]
        		totalDeaths = json_stats["deaths"]
        		todayDeaths = json_stats["todayDeaths"]
        		recovered = json_stats["recovered"]
        		active = json_stats["active"]
        		critical = json_stats["critical"]
        		casesPerOneMillion = json_stats["casesPerOneMillion"]
        		deathsPerOneMillion = json_stats["deathsPerOneMillion"]
        		totalTests = json_stats["totalTests"]
        		testsPerOneMillion =json_stats["testsPerOneMillion"]
        		msg = f"""
[BC]Covid-19 Status Of {country}!
[C]Total Cases : {totalCases}
[C]Today Cases : {todayCases}
[C]Total Deaths : {totalDeaths}
[C]Today Deaths : {todayDeaths}
[C]Recovered : {recovered}
[C]Active : {active}
[C]Critical : {critical}
[C]Cases Per One Million : {casesPerOneMillion}
[C]Deaths Per One Million : {deathsPerOneMillion}
[C]Total Tests : {totalTests}
[C]Tests Per One Million : {testsPerOneMillion}
""" 
        		sub.send_message(chatId=chatId, message=msg)
        	except Exception as c:
        		print(c)
        if content.startswith('!like'):
        	likee=content.replace('!like ','')
        	lolo=cli.get_from_link(likee).ndc_Id
        	print(lolo)
        	lolo2=cli.get_from_link(likee).object_Id
        	cli.vote(lolo,lolo2)
        	sub.send_message(chatId=chatId, message="تم وضع أعجاب بالمدونة", replyTo=msgId)
        
      
        if content.startswith('!YN'):
        	phyyc = ("كاذب","صادق")
        	rbjhl = random.choice(phyyc)
        	sub.send_message(chatId=chatId, message=rbjhl,replyTo=msgId)
        	
        if content.startswith('!img'):
        	mmkk=content.replace('!img','')
        	print("ok")
        	content=urllib.parse.quote(mmkk)
        	url = 'https://www.google.com/search?q='+content+'&tbm=isch&tbs=isz:l&hl=ar&sa=X&ved=2ahUKEwjGi4yLi5nzAhUZFBoKHU7XBK4Q258EegQIARBW&biw=412&bih=756'
        	print("ok")
        	r = requests.get(url)
        	soup = BeautifulSoup(r.text, 'html.parser')
        	images= soup.find_all('img')
        	print("ok")
        	images=images[5:12]
        	ptint("ok")
        	for image in images:
        		k=image['src']+".jpg"
        		with open("/sdcard/omar.jpg", 'rb') as f:
        			im = requests.get(k)
        			print("ok")
        			sub.send_message(chatId, fileType='image', file=f)
        			os.remove("omar.jpg")
        			
        	
        if content.startswith('!حجر'):
        	pc = ('حجرة', 'ورقة', 'مقص')
        	rpc = random.choice(pc)
        	sub.send_message(chatId=chatId, message=rpc, replyTo=msgId)
        	
        if content.startswith('!ورقة'):
        	ptc = ('حجرة', 'ورقة', 'مقص')
        	rhpc = random.choice(ptc)
        	sub.send_message(chatId=chatId, message=rhpc, replyTo=msgId)
        
        
        if content.startswith('!مقص'):
        	phc = ('حجرة', 'ورقة', 'مقص')
        	rbhl = random.choice(phc)
        	sub.send_message(chatId=chatId, message=rbhl,replyTo=msgId)
        	
        if content.startswith('!gif'):
        	to_search = content[5:]
        	try:
        	  api_instance = gc.DefaultApi()
        	  api_key ='w0JGbOjCtZqH0s1GMT8X5S6pLKtVyv4C'
        	  fmt = 'gif'
        	  response = api_instance.gifs_search_get(api_key,to_search,limit=1,offset=randint(1,10),fmt=fmt)
        	  gif = response.data[0]
        	  url= gif.images.downsized.url
        	  urllib.request.urlretrieve(url,f"{to_search}.gif")
        	  with open(f"{to_search}.gif","rb") as file:
        	      sub.send_message(chatId=data.message.chatId,file=file,fileType="gif")
        	      os.remove(f"{to_search}.gif")
        	except Exception as a: print(a)
	    	
        	
        
        if content.startswith('!prof'):
        	for user in mention:
        		info = sub.get_user_info(mention[0])
        		print(info)
        		sub_cli.edit_profile(nickname=info.nickname,icon=urllib.request.urlopen(info.icon))    		
        		sub.send_message(chatId=chatId, message="تم",replyTo=msgId)		
        
        if content.startswith('!num'):
        	randomnumb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'] 
        	koil = random.choice(randomnumb)
        	sub.send_message(chatId=chatId, message=koil, replyTo=msgId)
        	
        if content.startswith('!ghost'):
            gett=content.replace('!ghost ','')
            sub.send_message(chatId=chatId, message=gett, messageType="109")
        
        	
        	
        
        if content.startswith('!get'):
            get=content.replace('!get ','')
            id=client.get_from_code(get).objectId
            sub.send_message(chatId=chatId, message=id, replyTo=msgId)

        if content.startswith('!base64'):
            try:
                en = base64.b64decode(content[8:])
            except:
                en = base64.b64encode(content[8:].encode())
            sub.send_message(chatId=chatId, message=f'[CI]{en.decode()}', replyTo=msgId)

        if '!help' in content:
            sub.send_message(chatId=chatId, message="""[BIC]بدائية الأوامر (!)

[C]- help : إرسال جميع الأوامر
[C]- base64 [النص] : فك وتشفير
[C]- follow [رابط بروفايل] : متابعة
[C]- unfollow [رابط بروفايل] : إلغاء المتابعة
[C]- comment [me - رابط بروفايل - منشن] : ترك بصمة على الحائط

[C]- tr [يجب الرد على الرسالة التي تريد ترجمتها]

[C]- msg [الرسالة] : إرسالة رسالة
[C]- get [رابط] : id إستخراج ال
[C]- say [الرسالة] : إرسالة رسالة صوتية
[C]- google [النص] : البحث في قوقل
[C]-infobot:للحصول على معلومات البوت
[C]- res [None - رابط دردشة] : إستخراج صور الدردشة وإرسالها
[C]comt:[النص]لتعليق على حائط البروفايل


[BIC]القائمة البيضاء
[C]- black [منشن - رابط بروفايل] : إضافة عضو إلى القائمة السوداء
[C]- white [منشن - رابط بروفايل] : إضافة عضو إلى القائمة البيضاء
[C]- unblack [منشن - رابط بروفايل] : إزالة عضو من القائمة السوداء
[C]- unwhite [منشن - رابط بروفايل] : إزالة عضو من القائمة البيضاء
[C]- view [True - False] : وضع الأطلاع
[C]- join [رابط دردشة] : دخول دردشة
[C]- chat [منشن - me - رابط عضو] : بدأ دردشة
[C]- vc : دخول الدردشة المباشرة كمشاهدة
[C]- deviceId : إعطائك ديفايس اي دي
[C]- kick [منشن] : طرد عضو
[C]- ban [منشن] : طرد عضو نهائي
[C]- post [t=عنوان & c=محتوى] : إنشاء مدونة
[C]- start : بدأ غرفة صوتية
[C]- end : أنهاء الغرفة الصوتية
[C]- set com [comId] : تعيين منتدى جديد
[C]- set welcome [رسالة الترحيب] : تعيين رسالة ترحيب جديدة

""", replyTo=msgId)

        if content.startswith('!google'):
            st = wikipedia.search(content[8:])
            s = wikipedia.summary(st[0])
            sub.send_message(chatId=chatId, message=f"""
[CBI]{st[0]}  
  
[CI]{s[0:1990]}""", replyTo=msgId)

        if content.startswith('!res'):
            if 'http' in content:
                obj = client.get_from_code(content[5:])
                COM = obj.path
                COM = COM[1:COM.index('/')]
                subO = amino.SubClient(COM, profile=client.profile)
                info = subO.get_chat_thread(obj.objectId)
                icons = [info.icon, info.backgroundImage]
            else:
                info = sub.get_chat_thread(chatId)
                icons = [info.icon, info.backgroundImage]
            for icon in icons:
                ic = urllib.request.urlopen(icon)
                sub.send_message(chatId, fileType='image', file=ic)

        if content.startswith('!longEx'):
            Video = YouTube(content[8:])
            Video.streams.first().download(filename='video')
            vc = VideoFileClip('video.mp4')
            trim = vc.subclip(0, 180)
            ac = trim.audio
            ac.write_audiofile('audio.mp3')
            with open('audio.mp3', 'rb') as fp:
                sub.send_message(chatId=chatId, fileType='audio', file=fp)
            vc.close()
            ac.close()
            os.remove('video.mp4')
            os.remove('audio.mp3')

        if content.startswith('!ex'):
            Video = YouTube(content[4:])
            Video.streams.first().download(filename='video')
            vc = VideoFileClip('video.mp4')
            ac = vc.audio
            ac.write_audiofile('audio.mp3')
            with open('audio.mp3', 'rb') as fp:
                sub.send_message(chatId=chatId, fileType='audio', file=fp)
            vc.close()
            ac.close()
            os.remove('video.mp4')
            os.remove('audio.mp3')

        if content.startswith('!comment'):
            if mention is None:
                if 'me' in content[9:12]:
                    sub.comment('[CB]I love you 🤍 !.', userId=author.userId)
                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=author.userId)
                else:
                    obj = client.get_from_code(content[9:]).objectId
                    sub.comment('[CB]I love you 🤍 !.', userId=obj)
                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=obj)
            else:
                for user in mention:
                    sub.comment('[CB]I love you 🤍 !.', userId=user)
                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=user)
                    
        if content.startswith('!comt'):
                    mqm=content.replace('!comt','')
                    sub.comment(mqm, userId=author.userId)
                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=author.userId)
  
        if content.startswith('!Bot join the chat'):
            sub.join_chat(chatId)

        if content.startswith('!Bot sit on my lap'):
            sub.send_message(chatId=chatId, message="I will sit ", replyTo=msgId)

        if content.startswith('!dv'):
            ads=requests.get("https://aminohub.sirlez.repl.co/deviceId").text
            sub.send_message(chatId=chatId, message=ads, replyTo=msgId)

        if content.startswith('!Bot kiss me'):
            sub.send_message(chatId=chatId, message="Take a kiss 💋", replyTo=msgId)

        if content.startswith('!Bot give me'):
            sub.send_message(chatId=chatId, message="This is a " + content[14:] + f" for {author.nickname} ",replyTo=msgId)
        if "!infobot" in content:
        	sub.send_message(chatId=chatId, message="""
[C] ╭── ─ ────╌ ⃝🎭᭠〭ꨩ࿔〬 ──── ─ ──╮
[C]    ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜	
[c] مرحبا بك في معلومات البوت
[c]
[c]انا روبوت دردشة واسمي هو شـادي
[c] أنا اقوم بالكثير من المهام يمكنك منادتي بأسمي
[c]  وسأعرض عليك كيف تستدعي قائمة الأوامر
[c] <$المطور$>", 
[C]  -Omar.
[c]  مصمم البروفايل
[c]   -Omnia.
[C]   ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜ ͡──͜
[C] ╰─── ─ ───  ╌ ⃝🎭᭠〭ꨩ࿔〬  ──── ─ ──╯

"""
,embedLink="ndc://user-profile/efd2a89d-5ac0-4d66-a7d3-ecb456f3c079"
,embedTitle="المطور:-Omar            ")

        if author.userId in whiteList:
            if content.startswith('!ban'):
                for user in mention:
                    if user == client.userId:
                        blackList.append(author.userId)
                        sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لطرد البوت!!!', replyTo=msgId)
                    else:
                        sub.kick(user, chatId, False)
                        sub.send_message(chatId, message=f'[C] تم حظر هذا <$العضو$> لمخالفته القواعد! ',mentionUserIds=[user])

            if content.startswith('!kick'):
                for user in mention:
                    if user == client.userId:
                        blackList.append(author.userId)
                        sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لطرد البوت!!!', replyTo=msgId)
                    else:
                        sub.kick(user, chatId, True)
                        sub.send_message(chatId, message=f'[C] تم طرد هذا <$العضو$> لمخالفته القواعد! ', mentionUserIds=[user])

            if content.startswith('!deviceId'):
                r = random.choice([dv, dv1, dv2, dv3, dv4, dv5, dv6, dv7, dv8])
                sub.start_chat(userId=author.userId, message=r)
                sub.send_message(chatId, message=f'[C]<$@{author.nickname}$> أنظر إلى رسائلك الخاصة ', mentionUserIds=[author.userId])

            if content.startswith('!chat'):
                if mention is None:
                    if 'me' in content[6:9]:
                        sub.start_chat(userId=author.userId, message='[C] تم بدأ دردشة معك بسبب أمر من أعضاء القائمة البيضاء')
                    else:
                        obj = client.get_from_code(content[6:]).objectId
                        sub.start_chat(userId=obj, message='[C] تم بدأ دردشة معك بسبب أمر من أعضاء القائمة البيضاء')
                    sub.send_message(chatId, message='[C] تم بدأ دردشة مع العضو!', replyTo=msgId)
                else:
                    for user in mention:
                        sub.start_chat(userId=user, message='[C] تم بدأ دردشة معك بسبب أمر من أعضاء القائمة البيضاء')
                        sub.send_message(chatId, message='[C] <$تم بدأ دردشة مع هذا <$العضو!', mentionUserIds=user, replyTo=msgId)

            if content.startswith('!join'):
                obj = client.get_from_code(content[6:]).objectId
                info = sub.get_chat_thread(obj)
                sub.join_chat(obj)
                sub.send_message(chatId, message=f'تم دخول {info.title}', replyTo=msgId)

            if content.startswith('!view'):
                if 'False' in content:
                    sub.edit_chat(chatId, viewOnly=False)
                    sub.send_message(chatId=chatId, message="تم ألغاء تفعيل وضع الأطلاع", replyTo=msgId)
                else:
                    sub.edit_chat(chatId, viewOnly=True)
                    sub.send_message(chatId=chatId, message="تم تفعيل وضع الأطلاع", replyTo=msgId)

            if content.startswith('!unwhite'):
                if mention is None:
                    obj = client.get_from_code(content[9:]).objectId
                    if obj == vipId: blackList.append(author.userId); sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لأزالة قائد القائمة البيضاء!!!', replyTo=msgId)
                    else: whiteList.remove(obj); sub.send_message(chatId=chatId, message='[C] تم إزالة العضو من القائمة البيضاء!', replyTo=msgId)
                else:
                    for user in mention:
                        if user == vipId: blackList.append(author.userId); sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لأزالة قائد القائمة البيضاء!!!', replyTo=msgId)
                        else: whiteList.remove(user); sub.send_message(chatId=chatId, message='[C] تم إزالة العضو من القائمة البيضاء!', replyTo=msgId)

            if content.startswith('!unblack'):
                if mention is None: blackList.remove(client.get_from_code(content[9:]).objectId)
                else:
                    for user in mention:
                        blackList.remove(user)
                sub.send_message(chatId=chatId, message='[C] تم إزالة العضو من القائمة السوداء!', replyTo=msgId)

            if content.startswith('!vc'):
                client.join_video_chat_as_viewer(comId=comId, chatId=chatId)
                sub.send_message(chatId=chatId, message='[C] تم الدخول كمشاهدة!', replyTo=msgId)

            if content.startswith('!white'):
                if mention is None: whiteList.append(client.get_from_code(content[7:]).objectId)
                else:
                    for user in mention:
                        whiteList.append(user)
                sub.send_message(chatId=chatId, message='[C] تم إضافة العضو إلى القائمة البيضاء!', replyTo=msgId)

            if content.startswith('!black'):
                if mention is None:
                    obj = client.get_from_code(content[8:]).objectId
                    if obj == vipId:
                        pass
                    else:
                        blackList.append(obj)
                else:
                    for user in mention:
                        if user == vipId: blackList.append(author.userId); sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لأزالة قائد القائمة البيضاء!!!', replyTo=msgId)

                sub.send_message(chatId=chatId, message='[C] تم إضافة العضو إلى القائمة السوداء!', replyTo=msgId)

            if '!start' in content:
                aaa.start_vc(comId, chatId, 1)
                sub.send_message(chatId, message='[C] تم بدأ غرفة المشاهدة')

            if '!end' in content:
                aaa.end_vc(comId, chatId)
                sub.send_message(chatId, message='[C] تم إيقاف غرفة المشاهدة')

            if content.startswith('!offline'):            
                sub.activity_status('offline')
                sub.send_message(chatId, message="حسناً أنا الان اوفلاين")
                
            if content.startswith('!online'):
                sub.activity_status("online")
                sub.send_message(chatId, message="حسناً أنا الان اونلاين")
                
                

            if content.startswith('!post'):
                content = str(content)
                print(content)
                tit = content[content.index('t='):content.index('&')]
                tit = tit.replace('t=', '')
                con = content[content.index('c='):]
                con = con.replace('t=', '')
                con = con.replace('c=', '')
                sub.post_blog(title=tit, content=con)
                sub.send_message(chatId=chatId, message=f"""[C] تم إنشاء المدونة
[C] العنوان : {tit}
[C] المحتوى : {con}""", replyTo=msgId)

            if content.startswith('!set welcome'):
                con = content[13:]
                global msg1
                msg1 = con
                sub.send_message(chatId, f"""[C] تم إعادة تعيين رسالة الترحيب
{con}""")
            if content[0][0] == "!":
            	if content[0][1:].lower() == "save":
            		nazvan = sub.get_chat_thread(chatId=data.message.chatId).title
            		opisan = sub.get_chat_thread(chatId=data.message.chatId).content
            		fonsss = sub.get_chat_thread(chatId=data.message.chatId).backgroundImage
            		sub.send_message(message="Saved!", chatId=data.message.chatId, replyTo=id)
	
