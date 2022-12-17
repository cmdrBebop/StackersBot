import asyncpg

from bot.tgbot.services.db.workers.worker_base import Worker
import bot.tgbot.services.db.workers as workers


class UsersWorker(Worker):
    table_name = 'bot_user'

    async def create(self):
        """
        Table creates by Django ORM

        Fields:


        :return:
        """
        pass

    async def add_new_user(self, telegram_id, username, mention) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (telegram_id, username, mention) VALUES ({telegram_id}, '{username}', '{mention}')   
        '''

        await self.execute(sql)
