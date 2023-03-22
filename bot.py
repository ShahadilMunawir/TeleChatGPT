import os
import uuid
import openai
import telebot
import requests
from PIL import Image
from io import BytesIO
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

@bot.message_handler(commands=["image"])
def generate_image(message: telebot.types.Message):
    prompt = ' '.join(message.text.split()[1:])
    if len(prompt.split()) == 0:
        return bot.reply_to(message, "Usage: /image {prompt}")

    chatId = message.chat.id

    bot.send_message(chatId, f"Generating image: {prompt}")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    if not os.path.exists("Images"):
        os.mkdir("Images")

    image_url = response["data"][0]["url"]
    image_bytes = requests.get(image_url).content
    image = Image.open(BytesIO(image_bytes))
    filePath = "Images/" + uuid.uuid4().hex  + ".jpg"
    image.save(filePath)

    with open(filePath, "rb") as f:
        return bot.send_photo(chatId, f)

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