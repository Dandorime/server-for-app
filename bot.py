import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command

API_TOKEN = '7673698115:AAFSWRVd_U4_mZkoiKHXxUhtX00zOBjL4LM'  # Замените на свой токен

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Передаем bot как первый аргумент и storage как второй

# URL вашего мини-приложения
MINI_APP_URL = 'https://bring-back-my.vercel.app/'

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Запустить мини-приложение", web_app=WebAppInfo(url=MINI_APP_URL))]
    ])
    await message.answer("Привет! Нажмите на кнопку, чтобы запустить мини-приложение:", reply_markup=keyboard)
    
# Функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())