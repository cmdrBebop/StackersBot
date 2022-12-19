import asyncpg

from tgbot.services.db.workers.worker_base import Worker
import tgbot.services.db.workers as workers


class UserStackWorker(Worker):
    table_name = 'web_user_stacks'

    async def create(self):
        """
        Table creates by Django ORM

        Fields:


        :return:
        """
        pass

    async def add_new_stack(self, telegram_id: int, stack_id: int) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (user_id, stack_id) VALUES ({telegram_id}, {stack_id})   
        '''

        await self.execute(sql)

    async def get_stack_ids(self, telegram_id: int) -> list[asyncpg.Record]:
        sql = f'''
        SELECT * FROM {self.table_name} WHERE user_id={telegram_id}
        '''

        return [i['stack_id'] for i in (await self.fetch(sql))]
