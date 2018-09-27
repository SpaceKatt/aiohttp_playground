'''
This module connects us to our postgreSQL instance
'''
import os
import asyncpg as pg

async def init_db():
    user = os.environ['PSQL_USER']
    database = os.environ['PSQL_DB']
    password = os.environ['PSQL_PASS']
    return await pg.create_pool(
        database=database,
        user=user,
        password=password
    )

def get_pool(req):
    return req.app['pool']

async def insert_name_statement(req, name, statement):
    '''
    Inserts a statement into a named tuple
    '''
    pool = get_pool(req)
    print('uhohhh')
    async with pool.acquire() as connection:
        async with connection.transaction():
            stmt = await connection.execute('''
                                        INSERT INTO state (name, state)
                                        VALUES ($1, $2)
                                            ''', name, statement)
            return stmt

async def retrieve_name_statement(req, name):
    '''
    Retrieves something we stored
    '''
    pool = get_pool(req)
    async with pool.acquire() as connection:
        async with connection.transaction():
            stmt = await connection.fetch('''
                                        SELECT state FROM state
                                        WHERE $1 = name
                                          ''', name)
            return stmt
