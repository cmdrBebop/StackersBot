from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

import tgbot.keyboards.inline_keyboards as inline_keyboards
from tgbot.misc import messages
from tgbot.misc import states
import tgbot.misc.callbacks as callbacks


async def command_start(message: Message):
    await message.reply(messages.hello.format(username=message.from_user.username))


async def change_to_start_filling(message: Message):
    await message.answer(text="Вы хотите заполнить анкету?\n Это поможет стать нам ближе",
                         reply_markup=inline_keyboards.form_about_me_start)
    await states.ToCompleteForm.Starting_completing.set()


async def form_competing_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Вы отказались от заполнения анкеты")
    await state.finish()


async def form_competition_ask_1(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите ФИО:")
    await state.update_data(msg=call.message)
    await states.ToCompleteForm.Name_ans.set()


async def form_competition_ask_2(message: Message, state: FSMContext):
    await state.update_data(usrFullName=message.text)
    await states.ToCompleteForm.Stack_ans.set()
    await message.answer("Введите свой стек:")


async def form_competition_ask_3(message: Message, state: FSMContext):
    await state.update_data(usrStack=message.text)
    await states.ToCompleteForm.About_me_ans.set()
    await message.answer("Расскажите о себе:")


async def form_competition_control_ask(message: Message, state: FSMContext):
    await state.update_data(usrAboutMe=message.text)
    user_data = await state.get_data()
    await message.answer(messages.user_information_for_check.format(userFullName=user_data["usrFullName"],
                                                                    userStack=user_data["usrStack"],
                                                                    userAboutMe=user_data["usrAboutMe"]),
                         reply_markup=inline_keyboards.conrol_asking_to_save_form)
    await states.ToCompleteForm.Control_ask_to_save.set()


async def form_success_saved(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await user_data["msg"].answer("Ваша анкета успешно сохранена!")
    await state.finish()

async def cansel_for_control_sending(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await user_data["msg"].answer("Отправка анкеты отменена")
    await state.finish()


async def command_main_menu(message: Message):
    await message.answer(text='Главное меню', reply_markup=inline_keyboards.main_menu)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state='*')
    dp.register_message_handler(command_main_menu, commands=['menu'], state="*")
    dp.register_message_handler(change_to_start_filling, commands=["fill"], state="*")
    dp.register_callback_query_handler(form_competing_cancel, callbacks.change_to_write_form.filter(answer="cancel"),
                                       state=states.ToCompleteForm.Starting_completing)
    dp.register_callback_query_handler(form_competition_ask_1, callbacks.change_to_write_form.filter(answer="yes"),
                                       state=states.ToCompleteForm.Starting_completing)
    dp.register_message_handler(form_competition_ask_2, state=states.ToCompleteForm.Name_ans)
    dp.register_message_handler(form_competition_ask_3, state=states.ToCompleteForm.Stack_ans)
    dp.register_message_handler(form_competition_control_ask, state=states.ToCompleteForm.About_me_ans)
    dp.register_callback_query_handler(cansel_for_control_sending,
                                       callbacks.control_ask.filter(answer="cancel"),
                                       state=states.ToCompleteForm.Control_ask_to_save)
    dp.register_callback_query_handler(form_success_saved,
                                       callbacks.control_ask.filter(answer="ok"),
                                       state=states.ToCompleteForm.Control_ask_to_save)
    # для ререгистации
