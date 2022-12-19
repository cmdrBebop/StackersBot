from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

import tgbot.keyboards.inline_keyboards as inline_keyboards
from tgbot.misc import messages
from tgbot.services.db.database import Database


async def command_start(message: Message, state: FSMContext):
    database: Database = message.bot.get('database')

    await message.delete()
    await state.finish()

    if not await database.users_worker.is_reg(message.from_user.id):
        await database.users_worker.add_new_user(message.from_user.id, message.from_user.mention)
        await database.subscribe_worker.add_subscribes(message.from_user.id)

    await message.answer(messages.hello, reply_markup=inline_keyboards.form_about_me_start)


async def command_main_menu(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    await message.answer(text='Главное меню', reply_markup=inline_keyboards.main_menu)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state='*')
    dp.register_message_handler(command_main_menu, commands=['menu'], state="*")
