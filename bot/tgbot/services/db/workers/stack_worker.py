import asyncpg

from tgbot.services.db.workers.worker_base import Worker
import tgbot.services.db.workers as workers


class StackWorker(Worker):
    table_name = 'web_stack'

    async def create(self):
        """
        Table creates by Django ORM

        Fields:


        :return:
        """
        pass

    async def add_new_stack(self, stack) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (title) VALUES ('{stack}')   
        '''

        await self.execute(sql)
