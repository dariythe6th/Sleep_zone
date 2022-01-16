from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Бот запущен.")

def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я твой помощник для сна")


def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		answer = text
		if answer[0]=='#':
			if answer[1:5]=='утро':
				time1= answer[7:13]
				time2 = answer[16:22]
				rate = answer[29:31]
				newansw= time1+ " - " +time2+ " Ты оценил сон на: "+rate
		context.bot.send_message(chat_id=chat.id, text=newansw)
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите сколько вы спали")

token ="5003896889:AAFlIPPPr7_-YFsN9_QO9nnO8W2e_L4ZSew"
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()