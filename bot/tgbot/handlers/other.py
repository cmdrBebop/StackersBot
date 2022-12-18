from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

import tgbot.misc.messages as messages
import tgbot.keyboards.inline_keyboards as inline_keyboards
import tgbot.misc.callbacks as callbacks


async def show_statistics_menu(call: CallbackQuery, callback_data: dict):
    # todo: get statistics from db
    await call.message.edit_text(messages.user_statistics.format(
        rate=0,
        number_of_visits=0
    ), reply_markup=inline_keyboards.get_back_button('main_menu'))
    await call.answer()


async def show_main_menu(call: CallbackQuery):
    await call.message.edit_text('Главное меню', reply_markup=inline_keyboards.main_menu)
    await call.answer()


async def close_button(call: CallbackQuery):
    await call.message.delete()
    await call.answer()


def register_other(dp: Dispatcher):
    dp.register_callback_query_handler(show_statistics_menu, callbacks.navigation.filter(to='statistics'))
    dp.register_callback_query_handler(show_main_menu, callbacks.navigation.filter(to='main_menu'))
    dp.register_callback_query_handler(close_button, callbacks.navigation.filter(to='close'))
