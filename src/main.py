'''
Module docstring.
'''
from aiohttp import web


ROUTES = web.RouteTableDef()


@ROUTES.get('/')
async def root_handle(req):
    '''
    REEE
    '''
    return web.Response(text='Get OUTTA here...\n')


@ROUTES.get('/{name}')
async def name_handle(req):
    '''
    REee
    '''
    name = req.match_info.get('name', 'Anon')
    text = 'Hello, ' + name + '\n'
    return web.Response(text=text)

if __name__ == '__main__':
    APP = web.Application()

    APP.add_routes(ROUTES)

    web.run_app(APP)
