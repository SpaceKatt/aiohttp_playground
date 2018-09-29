'''
This module connects us to our postgreSQL instance
'''
import asyncpg as pg
import uuid as uuid_generator
from hashlib import sha256
from .psql_client import get_pool
import traceback


def hash_password(uuid, password):
    pre_image = uuid + password
    return sha256(pre_image.encode('utf-8')).hexdigest()


async def insert_new_user(req, user_obj):
    '''
    Creates a new user in our database
    '''
    pool = get_pool(req)

    uuid = str(uuid_generator.uuid4())
    passhash = hash_password(uuid, user_obj['password'])

    async with pool.acquire() as connection:
        async with connection.transaction():
            try:
                result = await connection.execute('''
                            INSERT INTO end_user (uuid, username,
                                                  email, passhash)
                            VALUES ($1, $2, $3, $4)
                                                  ''',
                                                  uuid,
                                                  user_obj['username'],
                                                  user_obj['email'],
                                                  passhash)
                print(result)
                return {'status': 201}
            except pg.exceptions.UniqueViolationError as err:
                result = {
                    'status': 400
                }

                if 'Key (username)' in err.detail:
                    result['error'] = 'Username already exists'
                elif 'Key (email)' in err.detail:
                    result['error'] = 'Email already exists'
                else:
                    result['error'] = err.detail

                return result
            except Exception:
                traceback.print_exc()
                return {'status': 500}
