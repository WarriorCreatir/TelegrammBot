import openai
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6189637119:AAFQ-aByjvgEKM7uass1oo629-dMIPS6WRA'

openai_api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" you:", " AI:"]
    )
    await message.answer(response['choices'][0]['text'])
