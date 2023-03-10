import datetime

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

import tgbot.keyboards.inline_keyboards as inline_keyboards
import tgbot.misc.callbacks as callbacks
import tgbot.misc.messages as messages
from tgbot.misc import states
from tgbot.services.db.database import Database


async def show_survey_menu(call: CallbackQuery):
    database: Database = call.bot.get('database')

    user = await database.users_worker.get_user(call.from_user.id)
    stack_ids = await database.user_stacks_worker.get_stack_ids(call.from_user.id)
    stacks = [(await database.stack_worker.get_stack_by_id(stack_id))['title'] for stack_id in stack_ids]
    msg = messages.user_information_for_check.format(
        user_full_name=user['second_name'] + user['first_name'],
        user_birth_date=user['birthdate'].strftime('%d.%m.%Y'),
        user_stack=','.join(stacks),
        user_about_me=user['about_user']
    )
    await call.message.edit_text(msg, reply_markup=inline_keyboards.form_about_me_update)
    await call.answer()


async def refuse_fill_survey(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Вы отказались от заполнения анкеты")
    await call.answer()


async def input_fullname(call: CallbackQuery):
    await call.message.edit_text("Введите Фамилию и Имя (Иванов Петя):")
    await states.Survey.name_ans.set()
    await call.answer()


async def input_birthday(message: Message, state: FSMContext):
    await state.update_data(usrFullName=message.text)
    await states.Survey.birth_ans.set()
    await message.answer("Введите дату своего рождения(01.01.1970):")


async def input_stack(message: Message, state: FSMContext):
    date = message.text
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        await message.answer("Неверный формат даты. Используйте формат: dd.mm.yyyy:")
        return
    await state.update_data(usrBirthDate=message.text)
    await states.Survey.stack_ans.set()
    await message.answer("Введите свой стек через запятую:")


async def input_about_yourself(message: Message, state: FSMContext):
    await state.update_data(usrStack=message.text)
    await states.Survey.about_me_ans.set()
    await message.answer("Расскажите о себе(какой опыт работы, чем увлекаешься и что бы хотел делать):")


async def get_survey(message: Message, state: FSMContext):
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
    database: Database = call.bot.get('database')
    await call.message.delete()

    user_data = await state.get_data()
    second_name, first_name = user_data["usrFullName"].split()

    stacks = user_data["usrStack"].split(',')
    for stack in stacks:
        stack_id = await database.stack_worker.set_stack(stack)
        if stack_id:
            await database.user_stacks_worker.add_new_stack(call.from_user.id, stack_id)

    await database.users_worker.add_survey_info(
        call.from_user.id, first_name, second_name,
        datetime.datetime.strptime(user_data["usrBirthDate"], '%d.%m.%Y').date(), user_data["usrAboutMe"]
    )

    await call.message.answer('Главное меню', reply_markup=inline_keyboards.main_menu)
    await call.answer('Ваша анкета успешно сохранена!')
    await state.finish()


async def cansel_for_control_sending(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    await call.message.answer('Главное меню', reply_markup=inline_keyboards.main_menu)
    await call.answer('Отправка анкеты отменена')
    await state.finish()


def register_survey(dp: Dispatcher):
    dp.register_callback_query_handler(input_fullname, callbacks.update_survey.filter(to='update_survey'))

    dp.register_callback_query_handler(input_fullname, callbacks.survey.filter(to='fill_survey'))
    dp.register_message_handler(input_birthday, state=states.Survey.name_ans)
    dp.register_message_handler(input_stack, state=states.Survey.birth_ans)
    dp.register_message_handler(input_about_yourself, state=states.Survey.stack_ans)
    dp.register_message_handler(get_survey, state=states.Survey.about_me_ans)

    dp.register_callback_query_handler(refuse_fill_survey, callbacks.survey.filter(to='cancel_survey'))

    dp.register_callback_query_handler(cansel_for_control_sending,
                                       callbacks.control_ask.filter(answer="cancel"),
                                       state=states.Survey.control_ask_to_save)
    dp.register_callback_query_handler(form_success_saved,
                                       callbacks.control_ask.filter(answer="ok"),
                                       state=states.Survey.control_ask_to_save)
    dp.register_callback_query_handler(show_survey_menu, callbacks.navigation.filter(to='form'))
