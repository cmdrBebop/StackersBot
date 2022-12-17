import logging
from abc import abstractmethod

import asyncpg


class Worker:
    """
    Base for workers
    """

    @property
    @abstractmethod
    def table_name(self):
        raise NotImplementedError

    def __init__(self, database: str, user: str, password: str, host: str = 'localhost', port: int = 5432):
        self._db_name = database
        self._user = user
        self._password = password
        self._host = host
        self._port = port

        self.pool: asyncpg.pool.Pool | None = None

        self._logger = logging.getLogger(__name__)

    async def connect(self) -> None:
        """
        Create pool for a worker if it doesn't exist

        :return:
        """
        if not self.pool:
            self.pool = await asyncpg.create_pool(database=self._db_name, user=self._user, host=self._host,
                                                  password=self._password, port=self._port)

    async def execute(self, *args, **kwargs) -> None:
        if not self.pool:
            await self.connect()

        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.execute(*args, **kwargs)

    async def fetch(self, *args, **kwargs) -> list[asyncpg.Record]:
        if not self.pool:
            await self.connect()

        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetch(*args, **kwargs)

    async def fetchone(self, *args, **kwargs) -> asyncpg.Record:
        if not self.pool:
            await self.connect()

        async with self.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetchrow(*args, **kwargs)

    @abstractmethod
    async def create(self) -> None:
        """
        Create current worker's table
        :return:
        """
        raise NotImplementedError

    async def drop(self) -> None:
        sql = f'DROP TABLE {self.table_name}'

        await self.execute(sql)

    async def truncate(self) -> None:
        sql = f'TRUNCATE TABLE {self.table_name}'

        await self.execute(sql)

    async def select(self, columns: list[str] = '*', record_id: int = None) -> asyncpg.Record | list[asyncpg.Record] | None:
        """
        Select record or records from a current worker's table

        :param columns: List of required table columns, by default "*"
        :param record_id: Id of the required entry, by default None
        :return: asyncpg.Record if record_id is not None
                 list[asyncpg.Record] if record_id is None
        """
        sql = f'SELECT {", ".join(columns)} FROM {self.table_name}'

        if record_id:
            sql += f' WHERE id={record_id}'
            return await self.fetchone(sql)
        else:
            return await self.fetch(sql)
