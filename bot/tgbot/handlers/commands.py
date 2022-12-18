from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.misc import messages
import tgbot.keyboards.inline_keyboards as inline_keyboards


async def command_start(message: Message):
    await message.reply(messages.hello.format(username=message.from_user.username))


async def command_main_menu(message: Message):
    await message.answer(text='Главное меню', reply_markup=inline_keyboards.main_menu)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state='*')
    dp.register_message_handler(command_main_menu, commands=['menu'], state="*")
