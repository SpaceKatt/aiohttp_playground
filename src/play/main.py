'''
Testing ground!
'''
from aiohttp import web
import db.psql_client as pg_cli


ROUTES = web.RouteTableDef()


@ROUTES.get('/name/{name}')
async def name_handle(req):
    '''
    Handles other routes
    '''
    name = req.match_info.get('name', None)

    if not name or not name.isalnum():
        return web.Response(status=400)

    text = 'Hello, ' + name + '\n'

    statement = await pg_cli.retrieve_name_statement(req, name)

    if statement is False:
        return web.Response(status=404)

    text += statement + '\n'

    return web.Response(text=text)


@ROUTES.put('/name/{name}')
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


@ROUTES.post('/name/{name}')
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
