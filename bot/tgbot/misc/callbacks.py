from aiogram.utils.callback_data import CallbackData

navigation = CallbackData('nav', 'to', 'payload')
change_subscribe = CallbackData('change_subscribe', 'object')
change_to_write_form = CallbackData("write_form", "answer")
change_to_update_form = CallbackData("write_form", "answer")
control_ask = CallbackData("save_form", "answer")