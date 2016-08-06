import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def hello(websocket, path):
    while True:
        if path == "/board":
            await websocket.send("Board created!")
        elif path == "/player":
            await websocket.send("Registered!")
        elif path == "/start":
            await websocket.send("Started!")
        elif path == "/move":
            await websocket.send("Moved!")
        else:
            await websocket.send("What the heck are you doing?!")
        try:
            echo = await websocket.recv()
            logging.info("Message received: {} -> {}".format(path, echo))
        except websockets.exceptions.ConnectionClosed as ex:
            logging.info("Connection Closed with code {}".format(ex.code))
            break

start_server = websockets.serve(hello, '0.0.0.0', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
