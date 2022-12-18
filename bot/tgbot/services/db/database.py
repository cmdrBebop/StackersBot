import logging

import tgbot.services.db.workers as workers


class Database:
    """
    Interface for interacting with workers.
    Each worker has his own pool
    """

    def __init__(self, password: str, user: str, database: str, host: str = 'localhost', port: int = 5432):
        self.host = host
        self.password = password
        self.user = user
        self.database = database
        self.port = port

        self._connect_data = {
            'host': host,
            'password': password,
            'database': database,
            'user': user,
            'port': port
        }

        self.users_worker = workers.UsersWorker(**self._connect_data)

        self.workers = [
            self.users_worker,
        ]

        self.logger = logging.getLogger(__name__)

    async def create_all(self):
        [await worker.create() for worker in self.workers]

        self.logger.debug('All tables created')

    async def drop_all(self):
        [await worker.drop() for worker in self.workers]

        self.logger.debug('All tables dropped')

    async def truncate_all(self):
        [await worker.truncate() for worker in self.workers]

        self.logger.debug('All tables truncated')

    async def close_pools(self):
        [await worker.pool.close() for worker in self.workers if worker.pool]

        self.logger.debug('All pools closed')
