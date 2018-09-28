'''
This module connects us to our postgreSQL instance
'''
import asyncpg as pg
from .psql_client import get_pool


async def insert_new_user(req, user_obj):
    '''
    Creates a new user in our database
    '''
    pool = get_pool(req)

    pass
