# -*- coding: utf-8 -*-#
import socketio

sio = socketio.Client()


@sio.on('connect')
def on_connect():
    print('I\'m connected!')


@sio.on('custom message', namespace='/socket.io/')
def on_message(data):
    print(data)
    # print('I received a message!')


@sio.on('new message', namespace='/socket.io/')
def on_message(data):
    print('I received a custom message!')


@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')


def main():
    # sio.connect('http://192.168.1.117:8888/socket.io/')
    # sio.connect('http://test.qmovies.tv:8089/socket.io/')
    # sio.connect('http://13.232.77.146:5034/socket.io/')
    # sio.connect('http://47.52.2.140:5034/socket.io/')
    # sio.emit('custom message', {'data': 'hello'})
    # sio.send("hello")
    sio.connect('http://localhost:8081')


if __name__ == '__main__':
    main()
