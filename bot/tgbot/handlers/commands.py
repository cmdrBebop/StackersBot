from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

import tgbot.keyboards.inline_keyboards as inline_keyboards
from tgbot.misc import messages
from tgbot.misc import states
import tgbot.misc.callbacks as callbacks


async def command_start(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    await message.answer(messages.hello, reply_markup=inline_keyboards.form_about_me_start)
    await states.Survey.starting_completing.set()


async def command_main_menu(message: Message, state: FSMContext):
    await message.delete()
    await state.finish()

    await message.answer(text='Главное меню', reply_markup=inline_keyboards.main_menu)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state='*')
    dp.register_message_handler(command_main_menu, commands=['menu'], state="*")
