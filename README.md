# TeleChatGPT
TeleChatGPT is the Telegram bot implementation of ChatGPT.

## Installation
To install TeleChatGPT, you'll need to follow these steps:
1. Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/ShahadilMunawir/TeleChatGPT.git
```
2. Navigate to the project directory:
```bash
cd TeleChatGPT
```
3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Setting up Environment Variables
To use this bot you will need to set up two environment variables. These variables contain API keys, and are used to configure the application.

Here are the steps to set up the required environment variables

1. Open your terminal or command prompt
2. Navigate to the directory where the bot is installed
3. Copy the `.env.example` file to a new file named `.env` by running the following command:
```bash
mv .env.example .env
```
4. Open the `.env` file in a text editor, and replace the placeholders with the actual values for your environment variables. For example to setup the `TELEGRAM_BOT_TOKEN` variable, replace the placeholder with the actual value.
```bash
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```
5. Save the `.env` file


## Usage
To start the bot, run the following command:
```python3
python3 bot.py
```

## Contact
If you have any questions or feedback, please feel free to contact the maintainer at `shahadilmunawir110@gmail.com`

