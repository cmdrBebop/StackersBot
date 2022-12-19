from aiogram.utils.callback_data import CallbackData

navigation = CallbackData('nav', 'to', 'payload')
change_subscribe = CallbackData('change_subscribe', 'action', 'object')
survey = CallbackData('survey', 'to')
update_survey = CallbackData('update_survey', 'to')
control_ask = CallbackData("save_form", "answer")
