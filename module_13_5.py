from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()

button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
kb.add(button, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup={"resize_keyboard": True, 'is_persistent': True,
                                                                                    'one_time_keyboard': True, "keyboard": [[button], [button2]]})

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age_ = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_ = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight_ = message.text)
    data = await state.get_data()
    calories = (9.99 * int(data.get('weight_'))) + (6.25 * int(data.get('growth_'))) - (4.92 * int(data.get('age_'))) - 161
    await message.answer(f'Ваш результат {calories} — это ваш основной обмен веществ (BMR) в калориях.')
    await state.finish()

@dp.message_handler(text = 'Информация')
async def information(message):
    await message.answer('Информация о боте:\n\n1. Язык: Python\n2. Область применения: Здоровье\n3. Состояния: Стейт-менеджер')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
