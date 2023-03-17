import os
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHATGPT_TOKEN = os.environ.get("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
openai.api_key = CHATGPT_TOKEN

messages = [
    {
        "role": "system",
        "content": "Greeting"
    }
]

@bot.message_handler(commands=["start"])
def welcome_message(message: telebot.types.Message):
    return bot.send_message(message.chat.id, f"Hello {message.chat.first_name}")

@bot.message_handler(func=lambda m: True)
def ask(message: telebot.types.Message):
    question = message.text

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    replay = chat.choices[0].message.content

    messages.append(
        {
            "role": "system",
            "content": replay
        }
    )

    return bot.reply_to(message, replay)

bot.polling()
