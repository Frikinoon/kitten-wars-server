import sys

import asyncio
import websockets
import logging

import time


def main():
    init()

    return 0

def read_config():

    return True

def init():
    logging.basicConfig(level=logging.INFO)
    start_server = websockets.serve(hello, '0.0.0.0', 8080)
    asyncio.get_event_loop().run_until_complete(start_server)

    return True

def stop():
    asyncio.get_event_loop().stop()
    return True

def start_lobby():

    return True

async def hello(websocket, path):
    while True:
        try:
            echo = await websocket.recv()
            if path == "/board":
                await websocket.send("Board created!")
            elif path == "/player":
                await websocket.send("Registered!")
            elif path == "/start":
                await websocket.send("Started!")
            elif path == "/move":
                await websocket.send("Moved!")
            else:
                await websocket.send("Path: {}  Msg: {}".format(path, echo))
            logging.info("Message received: {} -> {}".format(path, echo))
        except websockets.exceptions.ConnectionClosed as ex:
            logging.info("Connection Closed with code {}".format(ex.code))
            break

if __name__ == "__main__":
    main()