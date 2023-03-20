import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем ссылки на страницы, которые нужно проверять
url = "https://kino-mall.ru/schedule/?date=23.03.2023"

# options
options = webdriver.ChromeOptions()

# headless mode
options.add_argument("--headless")

# Инициализируем драйвер браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Инициализируем бота
bot = Bot(token="6120394891:AAH6XO2WW2LSTeBEt-TmpCTQtapZ9ysuDSE")
dp = Dispatcher(bot)

users = []

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот, который будет проверять страницу kino-mall.ru и отправлять вам уведомление, когда ссылка на страницу изменится.")

# Функция для проверки страницы
async def check_page():
    while True:
        # Обновляем страницу
        print("Checking page...")
        driver.refresh()
        print("Processing...")
        # Ждем, пока пользователь не отправит сообщение
        await asyncio.sleep(0.1)
        print("Checking the page...Please wait...")
        # Проверяем, изменилась ли ссылка на страницу
        if driver.current_url == url:
            print("Ссылка изменилась!")
            # Отправляем сообщение всем пользователям, которые отправили команду "check"
            for user_id in users:
                await bot.send_message(chat_id=user_id, text="Ссылка на страницу kino-mall.ru изменилась!")
            break

# Обработчик сообщений
@dp.message_handler()
async def message_handler(message: types.Message):
    if message.text == "/check":
        await message.reply("Начинаю проверку страницы...")
        # Добавляем chat_id пользователя в список пользователей
        users.append(message.chat.id)
        await check_page()

# Запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)