import samino
c = samino.Client("22210FBEEEA9D9C77872C1D9E57892F6CE987064D3B9EA712461480F639FFD4AFC4B33191E466EDB9D")
import websocket
import requests
import amino
import json


class Helper:
    def __init__(self, headers, client=None, sub=None, amino=None):
        self.headers = headers
        self.url = "wss://ws1.narvii.com"
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'
        self.client = client
        self.amino = amino

    

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

import wikipedia



# login
Email = "cce64023ca@firemailbox.club"
Password = "o123o123"
# comId
comId = '148528461'
# orginal White list urls
vip = "http://aminoapps.com/p/4mawlv0"
# DeviceIds
dv = '22E710842706B1A0EB0E65754D61CA24224E0892DCD5AB75BAD728CEE08D16081C01E939361B26B92C'

msg = f"""

[C]اهلاً بك !

[C]انرت الدردشة ⚡.

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


@client.event('on_text_message')
def on_text_message(data: amino.objects.Event):
    mention = data.message.mentionUserIds
    content = data.message.content
    msgId = data.message.messageId
    chatId = data.message.chatId
    author = data.message.author
    if author.userId in blackList: pass
    else:
        if "!coin" in content:
            sub.send_message(chatId=chatId, message='جاري ارسال القروش', replyTo=msgId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
            c.watch_ad(author.userId)
