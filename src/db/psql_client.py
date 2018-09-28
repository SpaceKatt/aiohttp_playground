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
