import asyncio

import aioschedule
from aiogram import Bot

from bot.tgbot.config import Config
from bot.tgbot.services.schedulers.updates_from_server import get_updates_from_server

from bot.tgbot.services.db.database import Database


async def start_schedulers(config: Config, bot: Bot, db: Database):
    aioschedule.every(config.misc.updates_from_server_interval).minutes.do(get_updates_from_server, bot, db, config)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
