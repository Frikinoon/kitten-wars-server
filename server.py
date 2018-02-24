import sys

import asyncio
import websockets
import logging

import time
import argparse as PRS


def main():
    init()

    return 0

def read_config():
    parser = PRS.ArgumentParser()
    parser.add_argument("-w", "--width", help="Board width.")
    parser.add_argument("-h", "--height", help="Board height.")

    return True

def init():
    logging.basicConfig(level=logging.INFO)
    start_server = websockets.serve(process_connection, '0.0.0.0', 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    return True

def stop():
    asyncio.get_event_loop().stop()
    return True

def start_lobby():

    return True

def process_message(message):
    answer = "rcvd"

    return answer

async def process_connection(websocket, path):
    while True:
        try:
            msg = await websocket.recv()
            answer = process_message(msg)
            await websocket.send("Path: {}  Msg: {}".format(path, answer))

            logging.info("Message received: {} -> {}".format(path, msg))
        except websockets.exceptions.ConnectionClosed as ex:
            logging.info("Connection Closed with code {}".format(ex.code))
            break

if __name__ == "__main__":
    main()