'''
Runs the webserver.
'''
from aiohttp import web
import aiofiles
import asyncio
# import uvloop
from os import path

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
    try:
        file_path = path.join(path.dirname(path.abspath(__file__)),
                              './static/root.html')
        async with aiofiles.open(file_path, mode='r') as f:
            content = await f.read()
            return web.Response(
                    body=content,
                    headers={
                        'Content-Type': 'text/html'
                    },
            )
    except Exception:
        return web.Response(status=500)


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


LOOP = asyncio.get_event_loop()
APP = LOOP.run_until_complete(init_app())


if __name__ == '__main__':
    web.run_app(APP, host='127.0.0.1')
