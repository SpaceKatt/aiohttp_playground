'''
This module connects us to our postgreSQL instance
'''
import os
import asyncpg as pg

async def init_db():
    user = os.environ['PSQL_USER']
    database = os.environ['PSQL_DB']
    password = os.environ['PSQL_PASS']
    return pg.create_pool(database=database, user=user, password=password)
