import asyncpg

from tgbot.services.db.workers.worker_base import Worker
import tgbot.services.db.workers as workers


class StackWorker(Worker):
    table_name = 'web_message'

    async def create(self):
        """
        Table creates by Django ORM

        Fields:


        :return:
        """
        pass

    async def add_new_message(self, profile_id, text, created_at) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (profile_id, text, created_at) VALUES ({profile_id}, '{text}', {created_at})   
        '''

        await self.execute(sql)
