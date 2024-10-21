import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Замените 'YOUR_TOKEN' на токен вашего бота
TELEGRAM_TOKEN = ''
GIGACHAT_API_URL = ''  # Пример URL, замените на актуальный
GIGACHAT_API_KEY = ''  # Ваш ключ API GigaChat


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот на основе GigaChat. Как я могу помочь?')


def chat_with_gigachat(message: str) -> str:
    headers = {
        'Authorization': f'Bearer {GIGACHAT_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': message,
        'max_tokens': 150  # Настройте количество токенов по необходимости
    }

    response = requests.post(GIGACHAT_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get('response', 'Извините, я не смог обработать ваш запрос.')
    else:
        return 'Ошибка обращения к GigaChat API.'


def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    bot_response = chat_with_gigachat(user_message)
    update.message.reply_text(bot_response)


def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
   main()
