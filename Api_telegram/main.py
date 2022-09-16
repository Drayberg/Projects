from aiogram import Bot, Dispatcher, executor, types
from time import sleep
import random
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
API_TOKEN = os.getenv('TOKEN')
PATH_1 = os.getenv('PATH_1')
PATH_2 = os.getenv('PATH_2')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def select_pack(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row('First pack', 'Second pack')
    await message.reply('Выбирай.', reply_markup=markup)


@dp.message_handler(text=['First pack', 'Second pack'])
async def send_image(photo):
    if photo.text == 'First pack':
        path = PATH_1
        directory = os.listdir(path)
        while directory:
            file = random.choice(directory)
            random_photo = open(f'{path}{file}', 'rb')
            await bot.send_photo(photo.chat.id, photo=random_photo)
            directory.remove(file)
            sleep(5)
    elif photo.text == 'Second pack':
        path = PATH_2
        directory = os.listdir(path)
        while directory:
            file = random.choice(directory)
            random_photo = open(f'{path}{file}', 'rb')
            await bot.send_photo(photo.chat.id, photo=random_photo)
            directory.remove(file)
            sleep(5)


@dp.message_handler()
async def wrong_message_check(message):
    await bot.send_message(message.chat.id,
                           'Некорректный запрос, введите команду <b>/start</b> и выберите интересующий вас пак.',
                           parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp)
