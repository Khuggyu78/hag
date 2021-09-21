import samino
import random
from threading import Thread
import os
import pyjokes
from PIL import Image
import requests
import wikipedia



sid = "AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICIxNWNiNTlkOS1jNDZjLTQyZWEtYTY2MS05NTg1ZjYzNzk3OWYiLCAiNSI6IDE2MzIyMDc4NDMsICI0IjogIjc5LjIzNS4xNjYuMjgiLCAiNiI6IDEwMH333pYin4Zoy4y5U4y4LF3l-Xjwlw"

vip = [
    "b9166ca0-d549-4fe1-9c2c-584673bdf889",
    "efd2a89d-5ac0-4d66-a7d3-ecb456f3c079",
    "d0fbb7a7-4ad2-41d5-80be-43083360d332",
    "cf924322-d67e-4aab-9ca4-8260fc5e4cc1",
    "6bc53c9d-b3ee-44ec-a4e3-50fc9ed51ac6",
    "fab3a54d-6fe0-40dd-ba9d-49e62d014f74",
    "cc7a4d4c-4d3b-4da4-b3c9-3d7aed819552",
    "e05d7ca8-b438-44ce-b031-a4a1028b1761",
    "172ea1d9-564c-4678-88e1-b02a0d587eb3"
]

client = samino.Client(
    "22210FBEEEA9D9C77872C1D9E57892F6CE987064D3B9EA712461480F639FFD4AFC4B33191E466EDB9D"
)

comId = "160428216"


client.sid_login(sid)

client.launch()

local = samino.Local(comId)


@client.event("on_community_join", comId)
def on_com_join(data: samino.UserInfo):
    nickname = data.nickname

    userId = data.userId

    local.comment(f" مرحبا بك في منتدنا المتواضع {nickname}", userId=userId, asWeb=True)


@client.event("on_member_join")
def on_join(data: samino.Event):
    comId = data.ndcId

    chatId = data.message.chatId

    nickname = data.message.author.nickname

    local.send_message(chatId, f"[C]• ﹝ 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 ﹞ • \n \n [C]{nickname}", asWeb=True, comId=comId)



@client.event("on_sticker")
def on_sticker(data: samino.Event):
    comId = data.ndcId

    chatId = data.message.chatId

    local.send_message(chatId, f"ملصق جميل !", asWeb=True, comId=comId)


@client.event("on_live_mode_started")
def on_live_mode_started(data: samino.Event):
    comId = data.ndcId

    chatId = data.message.chatId

    local.send_message(chatId,
                       f"A member has start the live mode!",
                       asWeb=True,
                       comId=comId)


@client.event("on_live_mode_ended")
def on_live_mode_ended(data: samino.Event):
    comId = data.ndcId

    chatId = data.message.chatId

    local.send_message(chatId,
                       f"A member has end the live mode !",
                       asWeb=True,
                       comId=comId)


@client.event("on_view_mode_disabled")
def on_view_mode_disabled(data: samino.Event):
    comId = data.ndcId

    chatId = data.message.chatId

    local.send_message(chatId,
                       f"A member has disabled the view mode !",
                       asWeb=True,
                       comId=comId)


@client.event("on_message")
def on_message(data: samino.lib.Event):
    msg = data.message.content

    msgId = data.message.messageId

    comId = data.ndcId

    chatId = data.message.chatId

    userId = data.message.userId

    nickname = data.message.author.nickname

    try:
        mentionIds = data.message.json["extensions"]["mentionedArray"]

    except:
        pass

    local = samino.Local(comId)


    if msg.startswith("!tap"):
    

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        
        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)

        client.watch_ad(userId)




        local.send_message(chatId,
                           f"{nickname}@لقد حصلت على جائزتك اليومية ",                        asWeb=True)

    if msg.startswith("!coin"):
      for user in mentionIds:
          sd=msg.replace('!coin','')
          client.watch_ad(userid["userId"])

          local.send_message(chatId,
                           f"{sd}لقد حصلت على جائزتك اليومية ",                        asWeb=True)
                           




@client.event("on_message")
def on_message(data: samino.Event):
    message = data.message.content

    nickname = data.message.author.nickname

    msgId = data.message.messageId

    chatId = data.message.chatId

    userId = data.message.userId

    comId = data.ndcId

    print("\n\033[0;30;42m Nickname ❯ \033[0;0m" + "\033[0;37;40m " +
          nickname + " \033[0;0m" + "\n\033[0;30;42m comId ❯ \033[0;0m" +
          "\033[0;37;40m " + f"{comId}" + " \033[0;0m" +
          "\n\033[0;30;42m chatId ❯ \033[0;0m" + "\033[0;37;40m " + chatId +
          " \033[0;0m" + "\n\033[0;30;42m userId ❯ \033[0;0m" +
          "\033[0;37;40m " + userId + " \033[0;0m" +
          "\n\033[0;30;42m Message ❯ \033[0;0m" + "\033[0;37;40m " + message +
          " \033[0;0m\n")


@client.event("on_message")
def on_message(data: samino.Event):
    msg = data.message.content

    msgId = data.message.messageId

    comId = data.ndcId

    chatId = data.message.chatId

    userId = data.message.userId

    nickname = data.message.author.nickname

    try:
        mentionIds = data.message.json["extensions"]["mentionedArray"]

    except:
        pass

    local = samino.Local(comId)


    if msg.startswith("!prv"):
      local.start_chat(userId , message, asWeb)
      local.send_message(chatId, "تم بدء دردشة مع العضو", comId=comId, asWeb=True)

    
    if msg.startswith("!msg"):
        local.send_message(chatId, msg[5:], comId=comId, asWeb=True)
             

    if msg.startswith("شكرا"):
        local.send_message(chatId, "عفوا", comId=comId, asWeb=True)


    if msg.startswith("اكرهك"):
        local.send_message(chatId, "حسنا وانا احبك رغم كرهك لي", comId=comId, asWeb=True)

    if msg.startswith("طلق"):
       local.send_message(chatId, "انت طالق طالق طالق \n _ \n تم التطليق ", comId=comId, asWeb=True)
       

    if msg.startswith("سار"):
       local.send_message(chatId,"نعم", comId=comId, asWeb=True)



    

    if msg.startswith("!start"):
        local.send_message(chatId, "Hi \n !I'm here ", comId=comId, asWeb=True)
        
    if msg.startswith("مباريات") :
        local.send_message(chatId,"https://plus.kooora4live.net/m1/", comId=comId, asWeb=True)


    if msg.startswith("احلف"):
        local.send_message(chatId, "والله يرجال", comId=comId, asWeb=True)


    if msg.startswith("مين زوجك"):
        local.send_message(chatId, "مروان والباقي مش رجال طبعا معدا عمر  ", comId=comId, asWeb=True)

    if msg.startswith("ليش"):
        local.send_message(chatId, "[B]لأنك حريمه", comId=comId, asWeb=True)

    if msg.startswith("كيفك"):
        local.send_message(chatId,
                           "أنا بخير أذا كنت انت بخير",
                           comId=comId,
                           asWeb=True)

    if msg.startswith("بوت"):
        local.send_message(chatId, "اهلا", comId=comId, asWeb=True)

    if msg.startswith("!ser"):
      sdd=msg.replace('!ser','')
      u=(wikipedia.summary(sdd, sentences = 2))
      local.send_message(chatId, u, comId=comId, asWeb=True)

    if msg.startswith("ريكو"):
      local.send_message(chatId,
                           "عمة الكل وتاج راسك ",
                           comId=comId,replyTo=msgId)


    if msg.startswith("اليكس"):
      local.send_message(chatId,
                           "عمكم وتاج راسكم والشوقر دادي ",
                           comId=comId,replyTo=msgId)


    if msg.startswith("امنيه"):
      local.send_message(chatId,
                           "عمتك",
                           comId=comId,replyTo=msgId)


    if msg.startswith("اياد"):
      local.send_message(chatId,
                           "عمك",
                           comId=comId,replyTo=msgId)





    if msg.startswith("!color"):
            rp = ('اسود', 'بني', 'رمادي','أبيض','وردي','بنفسجي','برتقالي','أزرق','أصفر','اخضر','أحمر')
            rpr = random.choice(rp)
            local.send_message(chatId, rpr, comId=comId, asWeb=True)  
  
     
    if msg.startswith("السلام عليكم"):
        local.send_message(chatId, " وعليكم السلام", comId=comId, asWeb=True) 
    
    if msg.startswith("ssd"):
      local.kick(chatId, user["uid"], allowRejoin=True)
      

  
    if msg.startswith("حبيبي"):
        local.send_message(chatId, "يعمري", comId=comId, asWeb=True)

    if msg.startswith("انت جميل"):
        local.send_message(chatId, "احبك . ", comId=comId, asWeb=True)

    if msg.startswith("شخبارك"):
        local.send_message(chatId, "بخير دامك بخير", comId=comId, asWeb=True)

    if msg.startswith("احبك"):
        local.send_message(chatId,
                           "وانا اكثر قدام نتزوج  ",
                           comId=comId,
                           asWeb=True)

    if msg.startswith("رقص"):
        local.send_message(chatId, "ارقص بس لمروان", comId=comId, asWeb=True)

    if msg.startswith("! tap"):
        local.send_message(chatId, "وي اشبو دا", comId=comId, asWeb=True)
    

    if msg.startswith("انطم"):
        local.send_message(chatId, "حاضر اسف للازعاج", comId=comId, asWeb=True)
    
                           
      

    
                           

    if msg.startswith("!حجر"):
        pc = ('حجرة', 'ورقة', 'مقص')
        rpc = random.choice(pc)
        local.send_message(chatId, rpc, comId=comId, asWeb=True)

    if msg.startswith("!مقص"):
        rc = ('حجرة', 'ورقة', 'مقص')
        pcr = random.choice(rc)
        local.send_message(chatId, pcr, comId=comId, asWeb=True)

    if msg.startswith("!ورق"):
        rp = ('حجرة', 'ورقة', 'مقص')
        rpr = random.choice(rp)
        local.send_message(chatId, rpr, comId=comId, asWeb=True)

    if msg.startswith("!joke"):
      d=(pyjokes.get_joke())
      local.send_message(chatId,d, comId=comId, asWeb=True)
         
        
        
        
    if msg.startswith("!prv"):
        local.start_chat(userId , message, asWeb)
        local.send_message(chatId,"تم بدء دردشة مع العضو", comId=comId, asWeb=True)


    if msg.startswith("نيني"):
      ravii=msg.replace('نيني','')
      chatId=("7dc06177-8ebe-033f-26df-d68dc55744ad")
      local.send_message(chatId,
                            ravii,
                               comId=comId,
                               asWeb=True)

    if msg.startswith("منيوك"):
      userId = data.message.userId
      local.kick(chatId, user["uid"], False)

    if msg.startswith("انعل"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("طيز"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("كحبه"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("قحبة"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("عاهر"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("نيك"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("طيز"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("اهكرك"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("انا هكر"):
       userId = data.message.userId
       local.kick(chatId, userId, False)

    if msg.startswith("ابوك"):
       userId = data.message.userId
       local.kick(chatId, user["uid"], False)


                               
    if msg.startswith("!XO"):
      local.send_message(chatId," 1|2|3\n4|5|6\n7|8|9", comId=comId, asWeb=True)

      
    if msg.startswith("!x-1"):
      local.send_message(chatId,"X|2|3\n4|5|6\n7|8|9", comId=comId, asWeb=True)

    if msg.startswith("!x-2"):
      local.send_messag(chatId,"1|X|3\n4|5|6\n7|8|9", comId=comId, asWeb=True)


    if msg.startswith("!x-3"):
      local.send_message(chatId,"1|2|X\n4|5|6\n7|8|9", comId=comId, asWeb=True)


    if msg.startswith("!x-4"):
       local.send_message(chatId,"1|2|3\nX|5|6\n7|8|9", comId=comId, asWeb=True)


    if msg.startswith("!x-5"):
      local.send_message(chatId,"1|2|3\n4|X|6\n7|8|9", comId=comId, asWeb=True)

    if msg.startswith("!x-6"):
      local.send_message(chatId,"1|2|3\n4|5|X\n7|8|9", comId=comId, asWeb=True)


    if msg.startswith("!x-7"):
      local.send_message(chatId,"1|2|3\n4|5|6\nX|8|9", comId=comId, asWeb=True)


    if msg.startswith("!x-8"):
       local.send_message(chatId,"1|2|3\n4|5|6\n7|X|9", comId=comId, asWeb=True)


    if msg.startswith("!x-9"):
        local.send_message(chatId,"1|2|3\n4|5|6\n7|8|X", comId=comId, asWeb=True)
        
    if msg.startswith("!x1-o-2"):
        local.send_message(chatId,"X|O|3\n4|5|6\n7|8|9", comId=comId, asWeb=True)

    if msg.startswith("!x1-o-3"):
        local.send_message(chatId,"X|2|O\n4|5|6\n7|8|9", comId=comId, asWeb=True)
        
    if msg.startswith("!x1-o-4"):
        local.send_message(chatId,"X|2|3\nO|5|6\n7|8|9", comId=comId, asWeb=True)
        
    if msg.startswith("!x1-o-5"):
      local.send_message(chatId,"X|2|3\n4|O|6\n7|8|9", comId=comId, asWeb=True)

    if msg.startswith("!x1-o-6"):
      local.send_message(chatId,"X|2|3\n4|5|O\n7|8|9", comId=comId, asWeb=True)
      
    if msg.startswith("!x1-o-7"):
      local.send_message(chatId,"X|2|3\n4|5|6\nO|8|9", comId=comId, asWeb=True)
      
    if msg.startswith("!x1-o-8"):
        local.send_message(chatId,"X|2|3\n4|5|6\n7|O|9", comId=comId, asWeb=True)

    if msg.startswith("!x1-o-9"):
      local.send_message(chatId,"X|2|3\n4|5|6\n7|8|O", comId=comId, asWeb=True)

          

    if userId in vip:

        if msg.startswith("!liv"):
            local.start_vc("f588db7a-b14a-4bc0-9909-74fc791710ea")
            local.send_message(chatId,
                            "start live mode",
                               comId=comId,
                               asWeb=True)

        if msg.startswith("!end liv"):
            local.end_vc("f588db7a-b14a-4bc0-9909-74fc791710ea")
            local.send_message(chatId,
                               "the live mode has ended",
                               comId=comId,
                               asWeb=True)

        if msg.startswith("!1liv"):
            local.start_vc("061ed718-a4c0-42eb-97d9-d738f29629c1")
            local.send_message(chatId,
                            "start live mode",
                               comId=comId,
                               asWeb=True)

        if msg.startswith("!1end liv"):
            local.end_vc("061ed718-a4c0-42eb-97d9-d738f29629c1")
            local.send_message(chatId,
                               "the live mode has ended",
                               comId=comId,
                               asWeb=True)


        if msg.startswith("!follow"):
            for user in mentionIds:
                local.follow(user["uid"], asWeb=True)
                local.send_message(chatId,
                                   "The member has been followed",
                                   asWeb=True)

        if msg.startswith("!kick"):
            for user in mentionIds:
                local.kick(chatId, user["uid"])

        if msg.startswith("!ban"):
            for user in mentionIds:
                local.kick(chatId, user["uid"], False)

        if msg.startswith("!unfollow"):
            for user in mentionIds:
                local.unfollow(user["uid"], asWeb=True)
                local.send_message(chatId,
                                   "The member has been followed",
                                   asWeb=True)

        if msg.startswith("!اطرد"):
            for user in mentionIds:
                local.kick(chatId, user["uid"], allowRejoin=True)

        if msg.startswith("ارقصيلي"):
          local.send_message(chatId,"💃💃💃💃💃💃💃",comId=comId,asWeb=True)
             
            


        
        
 
 

 

