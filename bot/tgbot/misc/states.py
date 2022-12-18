from aiogram.dispatcher.filters.state import StatesGroup, State

class ToCompleteForm(StatesGroup):
    Starting_completing = State()
    Name_ans = State()
    Stack_ans = State()
    About_me_ans = State()
    Control_ask_to_save = State()
