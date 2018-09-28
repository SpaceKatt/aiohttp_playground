'''
Authentication module.
'''
from aiohttp import web
from os import path

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


@ROUTES.post(PREFIX + '/register')
async def register_user(req):
    '''
    Registers a user.
    '''
    pass


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
