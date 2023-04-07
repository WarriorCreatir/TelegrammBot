from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import openai

import os
from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv("6123845287:AAFTyX5O1K6OGqYkThQPyOTCm8Pc36t6YPo")
openai.api_key = os.getenv(
    "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")

updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Я бот, готовый отвечать на ваши вопросы.")


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "Я могу ответить на ваши вопросы. Просто напишите свой вопрос и я постараюсь дать на него ответ."
    )


def echo(update, context):
    response = openai.Completion.create(
        engine="davinci",
        prompt=update.message.text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=response.choices[0].text)


start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()