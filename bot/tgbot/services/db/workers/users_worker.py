import datetime

import asyncpg

from tgbot.services.db.workers.worker_base import Worker
import tgbot.services.db.workers as workers


class UsersWorker(Worker):
    table_name = 'web_user'

    async def create(self):
        """
        Table creates by Django ORM

        Fields:


        :return:
        """
        pass

    async def add_new_user(self, telegram_id: int, mention: str) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (tg_id, telegram_username, rating) VALUES ({telegram_id}, '{mention}', 0)
        '''

        await self.execute(sql)

    async def get_user(self, telegram_id: int) -> asyncpg.Record | None:
        sql = f'''
        SELECT * from {self.table_name} WHERE tg_id = {telegram_id}
        '''

        return await self.fetchone(sql)

    async def is_reg(self, telegram_id: int) -> bool:
        record = await self.get_user(telegram_id)
        if record:
            return True
        return False

    async def add_survey_info(self, telegram_id: int, first_name: str, second_name: str, birthdate: datetime.date,
                              about: str) -> None:
        print(type(birthdate))
        sql = f'''
        UPDATE {self.table_name} SET first_name='{first_name}', second_name='{second_name}',
        birthdate={str(birthdate)}::date, about='{about}' WHERE tg_id={telegram_id}
        '''

        await self.execute(sql)
