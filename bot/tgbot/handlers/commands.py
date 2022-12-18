from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.misc import messages
from tgbot.keyboards import keyBrdMainMenu

async def command_start(message: Message):
    await message.reply(messages.hello.format(username=message.from_user.username))


async def main_menu(message: Message):
    await message.answer(text="Главное меню", reply_markup=keyBrdMainMenu)

async def subscriptionMenu(Call: CallbackQuery):
    #async ..... messages.textOfUsersSubscribtions()

async def statisticMenu(Call: CallbackQuery):
    #async ......messages.textOfUserStatistic()

async def closeMenu(Call: CallbackQuery):
    pass

async def register_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state='*')
    dp.register_message_handler(main_menu, commands=["menu"], state="*")

    dp.register_inline_handler(subscriptionMenu, callbacks.callBMainMenu.filter(childMenu="Подписки"))
    dp.register_inline_handler(statisticMenu, callbacks.callBMainMenu.filter(childMenu="Статистика"))
    dp.register_inline_handler(closeMenu, callbacks.callBMainMenu.filter(childMenu="Закрыть"))


