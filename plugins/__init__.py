# Don't Remove Credit @Spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_77
# Ask Doubt on telegram @Spideyofficial_777

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
