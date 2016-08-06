import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def hello(websocket, path):
    while True:
        try:
            echo = await websocket.recv()
            logging.info("Message received: {}".format(echo))
            await websocket.send(echo)
        except websockets.exceptions.ConnectionClosed as ex:
            logging.info("Connection Closed with code {}".format(ex.code))
            break

start_server = websockets.serve(hello, '0.0.0.0', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
