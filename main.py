import asyncio
from pyrogram import Client, filters

# Здесь нужно указать токен вашего бота
API_TOKEN = ''
APP_ID = ''

class MyGigaChat(Client):
    def __init__(self, api_id, api_hash, bot_token):
        super().__init__(
            ":memory:",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
        )

    async def on_message(self, message):
        if message.text is not None:
            await self.send_message(
                chat_id=message.chat.id,
                text="Привет! Я твой виртуальный помощник ABRGPT. Чем могу помочь?"
            )

async def main():
    my_gigachat = MyGigaChat(APP_ID, '', API_TOKEN)
    await my_gigachat.start()
    await my_gigachat.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())