'''
Runs the webserver.
'''
from aiohttp import web
import asyncio
import uvloop

# Database connection
import db.psql_client as pg_cli

# app routes
import play.main as play
import auth.main as auth


ROUTES = web.RouteTableDef()


@ROUTES.get('/')
async def root_handle(req):
    '''
    Tells the malcontent to go root themselves off our lawn.
    '''
    return web.Response(status=400, text='Root off our lawn.\n')


async def init_app():
    '''
    Initialize the database, then application server
    '''
    app = web.Application()

    app['pool'] = await pg_cli.init_db()

    app.add_routes(ROUTES)
    app.add_routes(play.ROUTES)
    app.add_routes(auth.ROUTES)

    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    LOOP = asyncio.get_event_loop()
    APP = LOOP.run_until_complete(init_app())

    web.run_app(APP, host='127.0.0.1')
