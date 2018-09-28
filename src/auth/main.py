'''
Authentication module.
'''
from aiohttp import web
import db.psql_client as pg_cli


PREFIX = '/auth'
ROUTES = web.RouteTableDef()


@ROUTES.get(PREFIX)
async def root_handle(req):
    '''
    Health check.
    '''
    return web.Response()


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
