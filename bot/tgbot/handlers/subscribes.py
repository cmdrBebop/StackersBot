from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

import tgbot.misc.messages as messages
import tgbot.keyboards.inline_keyboards as inline_keyboards
import tgbot.misc.callbacks as callbacks
from tgbot.services.db.database import Database


async def show_subscribe_menu(call: CallbackQuery):
    database: Database = call.bot.get('database')
    subs_status = await database.subscribe_worker.get_subscribes(call.from_user.id)

    msg = messages.user_subscribes_status.format(
        hackathon_sub_status=messages.positive_toggle if subs_status[
            'hackathon_subscribe'] else messages.negative_toggle,
        lecture_sub_status=messages.positive_toggle if subs_status['lecture_subscribe'] else messages.negative_toggle,
        meet_up_sub_status=messages.positive_toggle if subs_status['meet_up_subscribe'] else messages.negative_toggle,
    )

    await call.message.edit_text(msg, reply_markup=inline_keyboards.subscribe_menu)


async def change_subscribe(call: CallbackQuery, callback_data: dict):
    database: Database = call.bot.get('database')
    sub_type = callback_data['object']
    await database.subscribe_worker.toggle_subscribe(call.from_user.id, sub_type)

    subs_status = await database.subscribe_worker.get_subscribes(call.from_user.id)

    msg = messages.user_subscribes_status.format(
        hackathon_sub_status=messages.positive_toggle if subs_status[
            'hackathon_subscribe'] else messages.negative_toggle,
        lecture_sub_status=messages.positive_toggle if subs_status['lecture_subscribe'] else messages.negative_toggle,
        meet_up_sub_status=messages.positive_toggle if subs_status['meet_up_subscribe'] else messages.negative_toggle,
    )

    await call.message.edit_text(msg, reply_markup=inline_keyboards.subscribe_menu)
    await call.answer("Успешно")


async def toggle_all(call: CallbackQuery, callback_data: dict):
    database: Database = call.bot.get('database')
    sub_type = callback_data['object']

    if sub_type == 'sub':
        status = True

        await database.subscribe_worker.update_subscribe(call.from_user.id, 'hackathon_subscribe', status)
        await database.subscribe_worker.update_subscribe(call.from_user.id, 'lecture_subscribe', status)
        await database.subscribe_worker.update_subscribe(call.from_user.id, 'meet_up_subscribe', status)
    else:
        status = False

        await database.subscribe_worker.update_subscribe(call.from_user.id, 'hackathon_subscribe', status)
        await database.subscribe_worker.update_subscribe(call.from_user.id, 'lecture_subscribe', status)
        await database.subscribe_worker.update_subscribe(call.from_user.id, 'meet_up_subscribe', status)

    subs_status = await database.subscribe_worker.get_subscribes(call.from_user.id)

    msg = messages.user_subscribes_status.format(
        hackathon_sub_status=messages.positive_toggle if subs_status[
            'hackathon_subscribe'] else messages.negative_toggle,
        lecture_sub_status=messages.positive_toggle if subs_status['lecture_subscribe'] else messages.negative_toggle,
        meet_up_sub_status=messages.positive_toggle if subs_status['meet_up_subscribe'] else messages.negative_toggle,
    )
    await call.message.edit_text(msg, reply_markup=inline_keyboards.subscribe_menu)

    await call.answer("Успешно")


async def subscribe_back(call: CallbackQuery):
    await call.message.edit_text('Главное меню', reply_markup=inline_keyboards.main_menu)
    await call.answer()


def register_subscribes(dp: Dispatcher):
    dp.register_callback_query_handler(show_subscribe_menu, callbacks.navigation.filter(to='subscribes'))
    dp.register_callback_query_handler(change_subscribe, callbacks.change_subscribe.filter(action='change_sub'))
    dp.register_callback_query_handler(toggle_all, callbacks.change_subscribe.filter(action='all_toggle'))
    dp.register_callback_query_handler(subscribe_back, callbacks.change_subscribe.filter(action='back'))
