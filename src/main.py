'''
Module docstring.
'''
import asyncio
from aiohttp import web
import db.psql_client as db_psql


ROUTES = web.RouteTableDef()


@ROUTES.get('/')
async def root_handle(req):
    '''
    Handles a GET request to root
    '''
    return web.Response(text=str(req.headers) + '\n')


@ROUTES.get('/name/{name}')
async def name_handle(req):
    '''
    Handles other routes
    '''
    name = req.match_info.get('name', 'Anon')
    text = 'Hello, ' + name + '\n'
    return web.Response(text=text)


@ROUTES.put('/name/{name}')
async def name_post(req):
    '''
    Testing errors
    '''
    name = req.match_info.get('name', False)
    if name is False:
        return web.Response(status=400)
    return web.Response()


async def init_app():
    '''
    Initialize the application server
    '''
    app = web.Application()

    app['pool'] = await db_psql.init_db()

    app.add_routes(ROUTES)

    return app


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()
    APP = LOOP.run_until_complete(init_app())
    web.run_app(APP)
