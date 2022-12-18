from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import tgbot.misc.callbacks as callbacks

main_menu = InlineKeyboardMarkup(row_width=1)
main_menu.add(
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


def get_back_button(to: str, payload: str = '') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton('Назад', callback_data=callbacks.navigation.new(to=to, payload=payload))
    )

    return keyboard


form_about_me_start = InlineKeyboardMarkup(row_width=1)
form_about_me_start.add(
    InlineKeyboardButton('Да, хочу рассказать о себе',
                         callback_data=callbacks.change_to_write_form.new(answer='yes')),
    InlineKeyboardButton('Отказаться от заполнения анкеты',
                         callback_data=callbacks.change_to_write_form.new(answer='cancel'))
)

conrol_asking_to_save_form = InlineKeyboardMarkup(row_width=2)
conrol_asking_to_save_form.add(
    InlineKeyboardButton('Сохранить анкету', callback_data=callbacks.control_ask.new(answer="ok"))
)
conrol_asking_to_save_form.row(
    InlineKeyboardButton('Заполнить заново', callback_data=callbacks.control_ask.new(answer="again")),
    InlineKeyboardButton('Отмена', callback_data=callbacks.control_ask.new(answer="cancel"))
)


# keySubsMenu = InlineKeyboardMarkup(row_width=2,
#                                       inline_keyboard=[
#                                           [
#                                               InlineKeyboardButton(
#                                                   text="Статус подписки на хакатоны",
#                                                   callback_data=callSubsMenu.new(subsFor="ХакатоныПодп")
#                                               )],
#                                           [InlineKeyboardButton(
#                                               text="Статус подписки на лекции",
#                                               callback_data=callSubsMenu.new(subsFor="ЛекцииПодп")
#                                           )],
#                                           [InlineKeyboardButton(
#                                               text="Статус подписки на Митапы",
#                                               callback_data=callSubsMenu.new(subsFor="МитапыПодп"))
#                                           ],
#                                             [InlineKeyboardButton(
#                                               text="Подписка на все",
#                                               callback_data=callSubsMenu.new(subsFor="followAll")
#                                             )
#                                             ,InlineKeyboardButton(
#                                               text="Отписка от всего",
#                                               callback_data=callSubsMenu.new(subsFor="unfollowAll")
#                                             )
#                                         ],
#                                             [InlineKeyboardButton(
#                                               text="Назад",
#                                               callback_data=callSubsMenu.new(subsFor="Cancel")
#                                           )]
#                                       ])
