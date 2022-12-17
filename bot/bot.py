import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aioredis import Redis

from tgbot.config import load_config
from tgbot import handlers
from tgbot import filters
from tgbot import middlewares


logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(middlewares.EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    for aiogram_filter in filters.filters:
        dp.filters_factory.bind(aiogram_filter)


def register_all_handlers(dp):
    for register in handlers.register_functions:
        register(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        handlers=(logging.FileHandler(r'logs.log'), logging.StreamHandler())
    )
    logger.info('Starting bot')
    config = load_config('.env')

    storage = RedisStorage2() if config.bot.use_redis else MemoryStorage()
    bot = Bot(token=config.bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)
    redis = Redis()

    bot['config'] = config
    bot['redis'] = redis

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e:
        logger.error('Bot stopped!')
        raise e
