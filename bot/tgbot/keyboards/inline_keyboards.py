from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.misc.callbacks import callBMainMenu, callSubsMenu

keyBrdMainMenu = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="Подписки",
                                                  callback_data=callBMainMenu.new(childMenu="Подписки")
                                              )],
                                          [InlineKeyboardButton(
                                              text="Статистика",
                                              callback_data=callBMainMenu.new(childMenu="Статистика")
                                          )],
                                          [InlineKeyboardButton(
                                              text="Закрыть",
                                              callback_data=callBMainMenu.new(childMenu="Закрыть"))
                                          ]
                                      ])

keySubsMenu = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="Статус подписки на хакатоны",
                                                  callback_data=callSubsMenu.new(subsFor="ХакатоныПодп")
                                              )],
                                          [InlineKeyboardButton(
                                              text="Статус подписки на лекции",
                                              callback_data=callSubsMenu.new(subsFor="ЛекцииПодп")
                                          )],
                                          [InlineKeyboardButton(
                                              text="Статус подписки на Митапы",
                                              callback_data=callSubsMenu.new(subsFor="МитапыПодп"))
                                          ],
                                            [InlineKeyboardButton(
                                              text="Подписка на все",
                                              callback_data=callSubsMenu.new(subsFor="followAll")
                                            )
                                            ,InlineKeyboardButton(
                                              text="Отписка от всего",
                                              callback_data=callSubsMenu.new(subsFor="unfollowAll")
                                            )
                                        ],
                                            [InlineKeyboardButton(
                                              text="Назад",
                                              callback_data=callSubsMenu.new(subsFor="Cancel")
                                          )]
                                      ])