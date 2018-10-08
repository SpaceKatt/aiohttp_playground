'''
Maze for crawler validation
'''
from aiohttp import web


PREFIX = '/maze'
ROUTES = web.RouteTableDef()


ROUTES.get(PREFIX)


@ROUTES.get(PREFIX)
async def handle_HEAD(req):
    return web.Response(status=200, content_type='text/html', text='''
            <html>
            reee <a href="./maze/selector/one">Reeee</a>
            </html>
    ''')


@ROUTES.get(PREFIX + '/selector/')
async def handle_enter_maze(req):
    return web.HTTPFound('/maze/selector/one')


@ROUTES.get(PREFIX + '/selector/{card}')
async def handle_wildcard_maze(req):
    '''
    Servers the same page three times
    '''
    linked_list = {
            "one": "two",
            "two": "three",
            "three": "out"
    }

    card = req.match_info.get('card', None)

    if card is None or card not in linked_list:
        return web.Response(status=404)

    return web.Response(status=200, content_type='text/html', text='''
            <html>
            reee <a href="./">Reeee</a> <br>
            reee <a href="./one">Reeee</a> <br>
            reee <a href="./two">Reeee</a> <br>
            reee <a href="./three">Reeee</a> <br>
            </html>
    ''')
