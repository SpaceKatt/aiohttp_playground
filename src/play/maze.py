'''
Maze for crawler validation
'''
from aiohttp import web


PREFIX = '/maze'
ROUTES = web.RouteTableDef()
HOST = 'http://127.0.0.1:8080'


ROUTES.get(PREFIX)


@ROUTES.get(PREFIX)
async def handle_HEAD(req):
    return web.Response(status=200, content_type='text/html', text='''
            <html>
            reee <a href="{0}/maze/rotator">Reeee</a>
            </html>
    '''.format(HOST))


@ROUTES.get(PREFIX + '/selector')
async def handle_enter_maze(req):
    return web.HTTPFound('{}/maze/selector/one'.format(HOST))


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
            reee <a href="{0}/maze/selector">Reeee</a> <br>
            reee <a href="{0}/maze/selector/one">Reeee</a> <br>
            reee <a href="{0}/maze/selector/two">Reeee</a> <br>
            reee <a href="{0}/maze/selector/three">Reeee</a> <br>
            </html>
    '''.format(HOST))


@ROUTES.get(PREFIX + '/rotator')
async def handle_selector(req):
    return web.HTTPFound('{}/maze/rotator/one'.format(HOST))


@ROUTES.get(PREFIX + '/rotator/{card}')
async def handle_selector_rotate(req):
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
        return web.HTTPFound(HOST + PREFIX + '/selector')

    return web.Response(status=200, content_type='text/html', text='''
            <html>
            reee <a href="{0}/maze/rotator/{1}">Reeee</a> <br>
            </html>
    '''.format(HOST, linked_list[card]))
