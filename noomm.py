import aminofix
c = aminofix.Client()
c.login("danial7987@gmail.com","o123o123")
cList=["http://aminoapps.com/c/svaaalfredo123","http://aminoapps.com/c/TmthylLydlz446","http://aminoapps.com/c/TmthylYdwlShwdh","http://aminoapps.com/c/XXIdol","http://aminoapps.com/c/LifeIdolsDi","http://aminoapps.com/c/OuDistrIc9","http://aminoapps.com/c/IdolsPalace378","http://aminoapps.com/c/DNW","http://aminoapps.com/c/NaIymun","http://aminoapps.com/c/IraqiMafia","http://aminoapps.com/c/2BEFREE","http://aminoapps.com/c/1_989","http://aminoapps.com/c/ResiDe","http://aminoapps.com/c/QrSn180","http://aminoapps.com/c/Africans","http://aminoapps.com/c/Hellpalace69","http://aminoapps.com/c/fahdggg","http://aminoapps.com/c/ZCO","http://aminoapps.com/c/MOagic","http://aminoapps.com/c/IdolsCurs","http://aminoapps.com/c/Anime-City","http://aminoapps.com/c/ANedRae","http://aminoapps.com/c/HECATE769","http://aminoapps.com/c/AvAnOs","http://aminoapps.com/c/ZhuaXinQian","http://aminoapps.com/c/AnBabys","http://aminoapps.com/c/JrLt","http://aminoapps.com/c/SI0BS"]
comId="89430311"
sub = aminofix.SubClient(comId=comId,profile=c.profile)
@c.event("on_text_message")
def on_text_message(data):
	try:
		msg = data.message.content
		msgId = data.message.messageId
		user = data.message.author.userId
		chatId = data.message.chatId
	except Exception as t:
		print(t)
	for l in cList:
		if l in msg and user!=c.userId:
			try:
				n = c.get_from_code(l)
				linkOfUser = f"ndc://x89430311/user-profile/{user}"
				title = sub.get_chat_thread(chatId).title
				linkOfChat = f"ndc://x{comId}/chat-thread/{chatId}"
				m = f"""
[bCU]رابط العضو:"
[CU]{linkOfUser}
[C]*＊✿❀○❀✿＊*
[cbu]رابط المنتدى المخالف:
[c]{l}
[C]*＊✿❀○❀✿＊*
[cbu]أسم الدردشة:
[c]{title}
[C]*＊✿❀○❀✿＊*
[cbu]رابط الدردشة:
[c]{linkOfChat}"""
				sub.send_message(chatId="078af5ff-1956-46f9-88a7-bacb4ff6b37f",message=m)
			except Exception as err:
				print(err)
print("???")
