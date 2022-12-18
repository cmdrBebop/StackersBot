from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

import tgbot.misc.messages as messages
import tgbot.keyboards.inline_keyboards as inline_keyboards
import tgbot.misc.callbacks as callbacks


async def show_subscribe_menu(call: CallbackQuery, callback_data: dict):
    # todo: get toggles status from db
    await call.message.edit_text(messages.user_subscribes_status.format(
        hackathon_sub_status=messages.positive_toggle,
        lecture_sub_status=messages.positive_toggle,
        meet_up_sub_status=messages.positive_toggle,
    ), reply_markup=inline_keyboards.subscribe_menu)


async def change_hackathon_subscribe(call: CallbackQuery):
    # todo: change status in db
    await call.answer("Успешно")


async def sub_all(call: CallbackQuery):
    # todo: change status in db
    await call.answer("Успешно")


async def unsub_all(call: CallbackQuery):
    # todo: change status in db
    await call.answer("Успешно")


async def subscribe_back(call: CallbackQuery):
    await call.message.edit_text('Главное меню', reply_markup=inline_keyboards.main_menu)
    await call.answer()


def register_subscribes(dp: Dispatcher):
    dp.register_callback_query_handler(show_subscribe_menu, callbacks.navigation.filter(to='subscribes'))
    dp.register_callback_query_handler(change_hackathon_subscribe, callbacks.change_subscribe.filter(object='hackathon'))
    dp.register_callback_query_handler(sub_all, callbacks.change_subscribe.filter(object='sub_all'))
    dp.register_callback_query_handler(unsub_all, callbacks.change_subscribe.filter(object='unsub_all'))
    dp.register_callback_query_handler(subscribe_back, callbacks.change_subscribe.filter(object='back'))
