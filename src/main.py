'''
Module docstring.
'''
from aiohttp import web


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

if __name__ == '__main__':
    APP = web.Application()

    APP.add_routes(ROUTES)

    web.run_app(APP)
