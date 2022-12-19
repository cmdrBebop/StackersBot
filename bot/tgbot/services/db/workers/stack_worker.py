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

    async def add_new_stack(self, stack: str) -> asyncpg.Record:
        sql = f'''
        INSERT INTO {self.table_name} (title) VALUES ('{stack}') RETURNING id   
        '''

        return await self.fetchone(sql)

    async def get_stack_by_id(self, stack_id: int) -> asyncpg.Record:
        sql = f'''
        SELECT * FROM {self.table_name} WHERE id={stack_id}
        '''

        return await self.fetchone(sql)

    async def get_stack_by_title(self, stack: str) -> asyncpg.Record | None:
        sql = f'''
        SELECT * FROM {self.table_name} WHERE title='{stack}'
        '''

        return await self.fetchone(sql)

    async def set_stack(self, stack: str) -> int | None:
        record = await self.get_stack_by_title(stack)
        if not record:
            return (await self.add_new_stack(stack))['id']
