'''
Module docstring.
'''
import asyncio
from aiohttp import web
import db.psql_client as pg_cli


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

    statement = await pg_cli.retrieve_name_statement(req, name)

    text = text + str(statement[0]) + '\n'

    return web.Response(text=text)


@ROUTES.put('/name/{name}')
async def name_post(req):
    '''
    Testing errors
    '''
    name = req.match_info.get('name', False)
    if name is False:
        return web.Response(status=400)

    data = await req.json()
    statement = await pg_cli.insert_name_statement(req, name, data['state'])

    return web.Response(text=str(statement))


async def init_app():
    '''
    Initialize the application server
    '''
    app = web.Application()

    app['pool'] = await pg_cli.init_db()

    app.add_routes(ROUTES)

    return app


if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()
    APP = LOOP.run_until_complete(init_app())
    web.run_app(APP)
