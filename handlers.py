from aiogram.filters import CommandStart
from aiogram import types
from aiogram.utils.markdown import hbold
from loader import dp

@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    kb=[
        [types.KeyboardButton(text='Я робот')],
        [types.KeyboardButton(text='Я не робот')]
        [types.KeyboardButton(text='Робот, но мне сказали что я не робот')]
    ]
    keyBoard=types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard==True,
        input_field_placeholder='Введите любой текст')

    await message.answer(f'Привет, путник,{message.from_user.full_name}!', reply_markup=keyBoard)

@dp.message(Command('Inline'))
async def cmd_inline(message:types.Message, bot: Bot):
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='Google', url='https://google.com'


@dp.message()
async def echo_handler(message:types.Message):
    try:
        await message.send_copy(chat_id=message.chat_id)
    except TypeError:
        await message.answer('Оши_бочка')