from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from aiogram.types.input_file import InputFile
from crud_functions import initiate_db, get_all_products, add_user, is_included

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()

kb = ReplyKeyboardMarkup()
lkb = InlineKeyboardMarkup()
baykb = InlineKeyboardMarkup()


button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
button3 = KeyboardButton(text="Купить")
button_register = KeyboardButton(text="Регистрация")
kb.add(button, button2, button3, button_register)

lkb_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
lkb_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
lkb.add(lkb_button, lkb_button2)

baykb_button = InlineKeyboardButton(text='Product1', callback_data='product_buying')
baykb_button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
baykb_button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
baykb_button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
baykb.add(baykb_button, baykb_button2, baykb_button3, baykb_button4)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

product_descriptions = {
    1: {"name": "Product1", "description": "описание 1", "price": 100, "photo": "product1.jpg"},
    2: {"name": "Product2", "description": "описание 2", "price": 200, "photo": "product2.jpg"},
    3: {"name": "Product3", "description": "описание 3", "price": 300, "photo": "product3.jpg"},
    4: {"name": "Product4", "description": "описание 4", "price": 400, "photo": "product4.jpg"},
}

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup={"resize_keyboard": True,
                                                                                     "keyboard": [[button], [button2], [button3], [button_register]]})

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = lkb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Для мужчин: BMR = (9,99 x вес в кг) + (6,25 x рост в см) - (4,92 x возраст в годах) + 5\n"
                              "Для женщин: BMR = (9,99 x вес в кг) + (6,25 x рост в см) - (4,92 x возраст в годах) - 161")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    # await call.amswar()

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


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    if not products:
        await message.answer("Нет доступных продуктов.")
        return
    for product in products:
        product_id, title, description, price = product
        await message.answer(f"Название: {title} | Описание: {description} | Цена: {price}")
        photo = product_descriptions[product_id]
        if photo:
            try:
                await bot.send_photo(chat_id=message.chat.id, photo=types.InputFile(photo['photo']))
            except FileNotFoundError:
                await message.answer(f"Фото {product_id} не найдено.")
        else:
            await message.answer("Фото для данного продукта отсутствует.")
    await message.answer("Выберите продукт для покупки:", reply_markup=baykb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text = 'Информация')
async def information(message):
    await message.answer('Информация о боте:\n\n1. Язык: Python\n2. Область применения: Здоровье\n3. Состояния: Стейт-менеджер')


@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError
    except ValueError:
        await message.answer("Возраст должен быть положительным числом. Попробуйте снова:")
        return

    await state.update_data(age=age)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация завершена! Добро пожаловать!")
    await state.finish()


if __name__ == '__main__':
    initiate_db()
    executor.start_polling(dp, skip_updates=True)
