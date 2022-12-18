from aiogram.dispatcher.filters.state import StatesGroup, State


class Survey(StatesGroup):
    starting_completing = State()
    name_ans = State()
    stack_ans = State()
    about_me_ans = State()
    control_ask_to_save = State()
