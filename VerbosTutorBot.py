from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes
import random
import unicodedata
import time
import sys
import os
import json
from Lesson import Lesson

#TODO:пересоздать репозиторий, чтобы в нем не было токенов телеграмма, сделать этот репозиторий опенсорсным
#TODO:зайти в свой домашний линукс. Видимо комп подвис, нужно просить папу перезагрузить
#TODO:понять как запускать бота на сервере в фоновом режиме


def get_lesson(context: ContextTypes.DEFAULT_TYPE) -> Lesson:
	try:
		return context.user_data['lesson']
	except KeyError:
		lesson = Lesson()
		context.user_data['lesson'] = lesson
		return lesson

# Обработчик команды старта
async def new_conjugation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	lesson = get_lesson(context)

	lesson.NewConjugation()
	
	await update.message.reply_text(f"========================:")
	await update.message.reply_text(f"Vamos a conjugar el verbo '{lesson.selected_verb}' en '{lesson.selected_tense}'")
	await update.message.reply_text(f"{lesson.CurrentPronoun()}:")

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	lesson = get_lesson(context)
	
	if not lesson.lesson_started:
		lesson.lesson_started = True
		await update.message.reply_text('Hola! Soy un bot para practicar conjugaciones de verbos en español.\nEmpezemos!')
		await new_conjugation(update, context)
		return

	user_input = update.message.text
	response = lesson.CheckAnswer(user_input)
	await update.message.reply_text(response)

	if lesson.ConjugationFinished():
		await new_conjugation(update, context)
	else:
		pronoun = lesson.CurrentPronoun()
		await update.message.reply_text(f"{pronoun}:")


# Обработчик команды stop
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
	lesson = get_lesson(context)
	total_answers = lesson.total_answers
	correct_answers = lesson.total_answers - lesson.mistakes
	total_time = time.time() - lesson.start_time
	
	if total_answers > 0:
		accuracy = correct_answers / total_answers * 100
		average_time = total_time / total_answers
		await update.message.reply_text(
			f"Statistica:\nRespuestos total: {total_answers}\n"
			f"Respuestos correctos: {correct_answers}\n"
			f"Errores: {total_answers - correct_answers}\n"
			f"Precisión: {accuracy:.2f}%\n"
			f"Tiempo total:  {total_time:.1f} segundos\n"
			f"Tiempo de respuesta: {average_time:.1f} segundos"
		)
	else:
		await update.message.reply_text("No exercises were completed.")

	
# Основная функция
def main() -> None:
	if not os.path.isfile('secret.json'):
		raise Exception('secret.json file not found')
		
	with open('secret.json') as f:
		config = json.load(f)
		BotToken = config['BotToken']
	
	app = ApplicationBuilder().token(BotToken).build()

	# Различные обработчики команд    
	app.add_handler(CommandHandler("stop", stop))
	app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

	app.run_polling()
	
if __name__ == '__main__':
	main()
