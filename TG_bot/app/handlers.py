from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keybords as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()
    time = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Здраствуйте это бот сообщества Digital Lab', reply_markup=kb.main)
    await message.reply('Что вам подсказать?')

@router.message(F.text == 'Digital Lab')
async def cmd_start(message: Message):
    await message.answer('Клуб или сообщество Digital Lab главной целью которого было собрать энтузиастов среди студентов готовых учиться новому и находить новые знакомства!')

@router.message(F.text == '1121a')
async def cmd_start(message: Message):
    await message.answer('Аудитория 1121а это пространство для развития и получения нового опыта участниками сообщества')

@router.message(F.text == 'О боте')
async def cmd_start(message: Message):
    await message.answer('Этот бот был написан одним из участников клуба :^) ')

@router.message(F.text == 'Контакты')
async def cmd_start(message: Message):
    await message.answer('Выберите участника', reply_markup=kb.contacs)

@router.callback_query(F.data == 'vlad')
async def contacs(callback: CallbackQuery):
    await callback.message.answer('Владислав Суховей - @zavdigitallab')

@router.callback_query(F.data == 'tex')
async def contacs(callback: CallbackQuery):
    await callback.message.answer('Тех.поддержка бота - @harbinger_of_winter', )

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.time)
    await message.answer('Введите время в которое придете')

@router.message(Register.time)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возвраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Введите ваш номер телефона через меню', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Вы придете к: {data["time"]}\nВаше имя: {data["name"]}\nВаш возвраст: {data["age"]}\nВаш номер телефона: {data["number"]}', reply_markup=kb.back)
    await state.clear()

@router.message(F.text == 'Вернуться назад')
async def back(message: Message):
    await message.answer('Нажмите на: /start')
