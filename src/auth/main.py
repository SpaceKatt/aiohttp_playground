'''
Authentication module.
'''
from aiohttp import web
from os import path
import re

import aiofiles
import db.psql_client as pg_cli


PREFIX = '/auth'
ROUTES = web.RouteTableDef()


@ROUTES.get(PREFIX)
async def root_handle(req):
    '''
    Health check.
    '''
    try:
        file_path = path.join(path.dirname(path.abspath(__file__)),
                              './docs/auth.md')
        async with aiofiles.open(file_path, mode='r') as f:
            content = await f.read()
            return web.Response(text=content)
    except Exception:
        return web.Response(status=500)


def valid_user_info(user_json):
    if not user_json['username'].isalnum():
        return False

    # Validate email
    if not re.match('[^@]+@[^@]+\.[^@]+', user_json['email']):
        return False

    return True


@ROUTES.post(PREFIX + '/register')
async def register_user(req):
    '''
    Registers a user.
    '''
    data = await req.json()

    if not valid_user_info(data):
        return web.Response(status=400)

    return web.Response(status=201)


@ROUTES.get(PREFIX + '/login')
async def login_user(req):
    '''
    Login using a user's credentials.
    '''
    pass


@ROUTES.get(PREFIX + '/me')
async def get_user_info(req):
    '''
    Get user's information.
    '''
    pass
