import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)
if __name__ == '__main__':
    web.run_app(app, port=8081)