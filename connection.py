from time import time

import psycopg2

from logger import logger


class Connection:
    "Postgresql connection layer"

    def __init__(self, environ):
        self._connection_string = environ.get('CONN_STRING', '')
        self._conn = None
        self._connect()

    def _connect(self):
        try:
            self._conn = psycopg2.connect(self._connection_string)
            self._conn.set_session(autocommit=True)
        except psycopg2.Error as exc:
            logger.error('Connection._connect() error: %s', exc)
            self._conn = None

    def execute(self, query, params):
        "Execute query(SQL) with params(tuple)"

        output = False
        if not self._conn:
            self._connect()

        if self._conn and query and params:
            try:
                init_time, executed_query = time(), ''
                with self._conn.cursor() as cur:
                    cur.execute(query, params)
                    executed_query = cur.query
                    output = True
                logger.info('Connection.execute(%s) %d ms', executed_query, (time() - init_time) * 1000)
            except psycopg2.Error as exc:
                logger.error('Connection.execute(query: %s, params: %s) error: %s', query, params, exc)
                self._conn = None

        return output

__all__ = ['Connection']
