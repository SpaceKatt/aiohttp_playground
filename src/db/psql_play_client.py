'''
This module connects us to our postgreSQL instance
'''
import asyncpg as pg
from .psql_client import get_pool


async def insert_name_statement(req, name, statement):
    '''
    Associate a statement with a fictional character
    '''
    pool = get_pool(req)

    async with pool.acquire() as connection:
        async with connection.transaction():
            try:
                await connection.execute('''
                                     INSERT INTO state (name, state)
                                     VALUES ($1, $2)
                                     RETURNING name_id
                                         ''', name, statement)
                return True
            except pg.exceptions.UniqueViolationError:
                return False


async def retrieve_name_statement(req, name):
    '''
    Retrieves a statement from a fictional character
    '''
    pool = get_pool(req)

    async with pool.acquire() as connection:
        async with connection.transaction():
            stmt = await connection.fetchrow('''
                                        SELECT state FROM state
                                        WHERE $1 = name
                                          ''', name)
            if stmt is None:
                return False
            else:
                return str(stmt['state'])


async def update_name_statement(req, name, statement):
    '''
    Associate a statement with a fictional character
    '''
    pool = get_pool(req)

    async with pool.acquire() as connection:
        async with connection.transaction():
            stmt = await connection.execute('''
                                        UPDATE state
                                        SET state = $1
                                        WHERE
                                          name = $2
                                            ''', statement, name)
            if stmt is None or stmt == 'UPDATE 0':
                return False
            else:
                return True
            return False


async def get_names(req):
    '''
    Associate a statement with a fictional character
    '''
    pool = get_pool(req)

    async with pool.acquire() as connection:
        async with connection.transaction():
            stmt = await connection.fetch('''SELECT name FROM state''')
            if stmt is None:
                return False
            else:
                return [elm['name'] for elm in stmt]
