from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import tgbot.misc.callbacks as callbacks

main_menu = InlineKeyboardMarkup(row_width=1)
main_menu.add(
    InlineKeyboardButton('Моя анкета', callback_data=callbacks.navigation.new(to='form', payload='')),
    InlineKeyboardButton('Подписки', callback_data=callbacks.navigation.new(to='subscribes', payload='')),
    InlineKeyboardButton('Статистика', callback_data=callbacks.navigation.new(to='statistics', payload='')),
    InlineKeyboardButton('Закрыть', callback_data=callbacks.navigation.new(to='close', payload='')),
)

subscribe_menu = InlineKeyboardMarkup(row_width=1)
subscribe_menu.add(
    InlineKeyboardButton('Изменить статус подписки на Хакатоны',
                         callback_data=callbacks.change_subscribe.new(object='hackathon')),
    InlineKeyboardButton('Изменить статус подписки на Лекции',
                         callback_data=callbacks.change_subscribe.new(object='lecture')),
    InlineKeyboardButton('Изменить статус подписки на Митапы',
                         callback_data=callbacks.change_subscribe.new(object='meet_up'))
)
subscribe_menu.row(
    InlineKeyboardButton('Подписка на все', callback_data=callbacks.change_subscribe.new(object='sub_all')),
    InlineKeyboardButton('Отписка от всего', callback_data=callbacks.change_subscribe.new(object='unsub_all'))
)
subscribe_menu.add(
    InlineKeyboardButton('Назад', callback_data=callbacks.navigation.new(to='main_menu', payload=''))
)

form_about_me_start = InlineKeyboardMarkup(row_width=1)
form_about_me_start.add(
    InlineKeyboardButton('Да, хочу рассказать о себе',
                         callback_data=callbacks.change_to_write_form.new(answer='yes')),
    InlineKeyboardButton('Отказаться от заполнения анкеты',
                         callback_data=callbacks.change_to_write_form.new(answer='cancel'))
)

form_about_me_update = InlineKeyboardMarkup(row_width=1)
form_about_me_update.add(
    InlineKeyboardButton('Хочу обновить свою анкету :)',
                         callback_data=callbacks.change_to_update_form.new(answer='yes')),
    InlineKeyboardButton('Назад',
                         callback_data=callbacks.navigation.new(to='main_menu', payload=''))
)

control_asking_to_save_form = InlineKeyboardMarkup(row_width=2)
control_asking_to_save_form.add(
    InlineKeyboardButton('Сохранить анкету', callback_data=callbacks.control_ask.new(answer="ok"))
)
control_asking_to_save_form.row(
    InlineKeyboardButton('Заполнить заново', callback_data=callbacks.control_ask.new(answer="again")),
    InlineKeyboardButton('Отмена', callback_data=callbacks.control_ask.new(answer="cancel"))
)


def get_back_button(to: str, payload: str = '') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton('Назад', callback_data=callbacks.navigation.new(to=to, payload=payload))
    )

    return keyboard
