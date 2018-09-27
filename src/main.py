'''
Module docstring.
'''
import asyncio
from aiohttp import web
import db.psql_client as pg_cli
import play.main as play


ROUTES = web.RouteTableDef()


@ROUTES.get('/')
async def root_handle(req):
    '''
    Handles a GET request to root
    '''
    return web.Response(text=str(req.headers) + '\n')


async def init_app():
    '''
    Initialize the application server
    '''
    app = web.Application()

    app['pool'] = await pg_cli.init_db()

    app.add_routes(ROUTES)
    app.add_routes(play.ROUTES)

    return app


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()
    APP = LOOP.run_until_complete(init_app())
    web.run_app(APP)
