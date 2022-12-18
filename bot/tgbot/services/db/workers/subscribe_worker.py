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

    async def add_subscribes(self, telegram_id, hackaton_sub, lecture_sub, meet_up_sub, vacancy_sub) -> None:
        sql = f'''
        INSERT INTO {self.table_name} (user_id, hackaton_subscribe, lecture_subscribe, meet_up_subscribe, vacancy_subscribe)
         VALUES ({telegram_id}, {hackaton_sub}, {lecture_sub}, {meet_up_sub}, {vacancy_sub})   
        '''

        await self.execute(sql)
