'''
This module connects us to our postgreSQL instance
'''
import os
import asyncpg as pg


async def init_db():
    '''
    Initialize our database and create a connection pool.
    '''
    user = os.environ['PSQL_USER']
    database = os.environ['PSQL_DB']
    password = os.environ['PSQL_PASS']

    return await pg.create_pool(
        database=database,
        user=user,
        password=password
    )


def get_pool(req):
    '''
    Return the connection pool from an incoming request object
    '''
    return req.app['pool']


async def insert_name_statement(req, name, statement):
    '''
    Associate a statement with a fictional character
    '''
    pool = get_pool(req)

    async with pool.acquire() as connection:
        async with connection.transaction():
            try:
                stmt = await connection.execute('''
                                            INSERT INTO state (name, state)
                                            VALUES ($1, $2)
                                            RETURNING name_id
                                                ''', name, statement)
                print(stmt)
                return str(stmt)
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

