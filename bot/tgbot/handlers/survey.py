import datetime

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

import tgbot.keyboards.inline_keyboards as inline_keyboards
import tgbot.misc.callbacks as callbacks
import tgbot.misc.messages as messages
from tgbot.misc import states


async def request_to_update_form(call: CallbackQuery):
    # todo get information about user, add text for user's form
    await call.message.edit_text("Вот моя анкета!!!!", reply_markup=inline_keyboards.form_about_me_update)
    # await states.Survey.starting_completing.set()
    await call.answer()


async def form_competing_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    await call.message.answer("Вы отказались от заполнения анкеты")
    await call.answer()
    await state.finish()


async def form_competition_ask_1(call: CallbackQuery):
    await call.message.delete()

    await call.message.answer("Введите Фамилию и Имя через символ пробела:")
    await states.Survey.name_ans.set()
    await call.answer()


async def form_competition_ask_1_2(message: Message, state: FSMContext):
    await state.update_data(usrFullName=message.text)
    await states.Survey.birth_ans.set()
    await message.answer("Введите дату своего рождения в формате dd.mm.yyyy:")


async def form_competition_ask_2(message: Message, state: FSMContext):
    date = message.text
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        await message.answer("Неверный формат даты. Используйте формат: dd.mm.yyyy:")
        return
    await state.update_data(usrBirthDate=message.text)
    await states.Survey.stack_ans.set()
    await message.answer("Введите свой стек:")


async def form_competition_ask_3(message: Message, state: FSMContext):
    await state.update_data(usrStack=message.text)
    await states.Survey.about_me_ans.set()
    await message.answer("Расскажите о себе:")


async def form_competition_control_ask(message: Message, state: FSMContext):
    await state.update_data(usrAboutMe=message.text)
    user_data = await state.get_data()

    msg = messages.user_information_for_check.format(
        user_full_name=user_data["usrFullName"],
        user_birth_date=user_data["usrBirthDate"],
        user_stack=user_data["usrStack"],
        user_about_me=user_data["usrAboutMe"]
    )

    await message.answer(msg, reply_markup=inline_keyboards.control_asking_to_save_form)
    await states.Survey.control_ask_to_save.set()


async def form_success_saved(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    await call.message.answer("Ваша анкета успешно сохранена!")
    await state.finish()
    await call.answer()


async def cansel_for_control_sending(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    await call.message.answer("Отправка анкеты отменена")
    await state.finish()
    await call.answer()


def register_survey(dp: Dispatcher):
    dp.register_callback_query_handler(form_competing_cancel, callbacks.change_to_write_form.filter(answer="cancel"),
                                       state=states.Survey.starting_completing)
    dp.register_callback_query_handler(form_competition_ask_1, callbacks.change_to_write_form.filter(answer="yes"),
                                       state=states.Survey.starting_completing)
    dp.register_callback_query_handler(form_competing_cancel, callbacks.change_to_update_form.filter(answer="cancel"),
                                       state=states.Survey.starting_completing)
    dp.register_callback_query_handler(form_competition_ask_1, callbacks.change_to_update_form.filter(answer="yes"),
                                       state=states.Survey.starting_completing)

    dp.register_message_handler(form_competition_ask_1_2, state=states.Survey.name_ans)
    dp.register_message_handler(form_competition_ask_2, state=states.Survey.birth_ans)
    dp.register_message_handler(form_competition_ask_3, state=states.Survey.stack_ans)
    dp.register_message_handler(form_competition_control_ask, state=states.Survey.about_me_ans)
    dp.register_callback_query_handler(cansel_for_control_sending,
                                       callbacks.control_ask.filter(answer="cancel"),
                                       state=states.Survey.control_ask_to_save)
    dp.register_callback_query_handler(form_success_saved,
                                       callbacks.control_ask.filter(answer="ok"),
                                       state=states.Survey.control_ask_to_save)
    dp.register_callback_query_handler(request_to_update_form, callbacks.navigation.filter(to='form'))
