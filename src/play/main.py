'''
Testing ground!
'''
from aiohttp import web
import db.psql_play_client as pg_cli


PREFIX = '/play'
ROUTES = web.RouteTableDef()


@ROUTES.get(PREFIX)
async def root_handle(req):
    '''
    Duh
    '''
    names = await pg_cli.get_names(req)

    if not names:
        return web.Response(status=404)

    data = {
            'names': names,
            }

    return web.json_response(data)


@ROUTES.get(PREFIX + '/{name}')
async def name_handle(req):
    '''
    Handles other routes
    '''
    name = req.match_info.get('name', None)
    if name is None or not name.isalnum():
        return web.Response(status=400)

    statement = await pg_cli.retrieve_name_statement(req, name)
    if statement is False:
        return web.Response(status=404)

    text = 'Hello, ' + name + '\n'
    text += statement

    return web.Response(text=text)


@ROUTES.put(PREFIX + '/{name}')
async def name_put(req):
    '''
    Testing errors
    '''
    name = req.match_info.get('name', False)

    if name is False:
        return web.Response(status=400)

    data = await req.json()
    statement = await pg_cli.update_name_statement(req, name, data['state'])

    if not statement:
        return web.Response(status=404)

    return web.Response()


@ROUTES.post(PREFIX + '/{name}')
async def name_post(req):
    '''
    Testing errors
    '''
    name = req.match_info.get('name', False)
    if name is False:
        return web.Response(status=400)

    data = await req.json()
    statement = await pg_cli.insert_name_statement(req, name, data['state'])
    if not statement:
        return web.Response(status=409)

    return web.Response(text=statement)
