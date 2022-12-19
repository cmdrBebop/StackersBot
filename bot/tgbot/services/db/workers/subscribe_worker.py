import asyncpg

from tgbot.services.db.workers.worker_base import Worker
import tgbot.services.db.workers as workers


class SubscribeWorker(Worker):
    table_name = 'web_subscribe'

    async def create(self):
        """
        Table creates by Django ORM

        Fields:


        :return:
        """
        pass

    async def add_subscribes(self, telegram_id: int, hackathon_sub: bool = True, lecture_sub: bool = True,
                             meet_up_sub: bool = True, vacancy_sub: bool = True) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (user_id, hackathon_subscribe, lecture_subscribe, meet_up_subscribe, vacancy_subscribe)
         VALUES ({telegram_id}, {hackathon_sub}, {lecture_sub}, {meet_up_sub}, {vacancy_sub})   
        '''

        await self.execute(sql)

    async def get_subscribes(self, telegram_id: int) -> asyncpg.Record:
        sql = f'''
        SELECT hackathon_subscribe, lecture_subscribe, meet_up_subscribe, vacancy_subscribe FROM {self.table_name} WHERE id={telegram_id}
        '''

        return await self.fetchone(sql)

    async def update_subscribe(self, telegram_id: int, subscribe: str, sub_status: bool) -> None:
        sql = f'''
        UPDATE {self.table_name} SET {subscribe}={sub_status} WHERE id={telegram_id}
        '''

        await self.execute(sql)
