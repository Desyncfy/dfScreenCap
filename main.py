import asyncio
import websockets
from time import sleep
import screentominecraft

async def connect_and_auth():

    async with websockets.connect("ws://127.0.0.1:31375") as websocket:
        # look at me putting things in variables for code readablity
        requested_scopes = "movement"
        await websocket.send(f"scopes {requested_scopes}")
        while True:
            response = await websocket.recv()
            print(f"INC {response}")
            # don't do anything until authentication
            if response == "auth":
                break # we exit the loop and allow stuff to run
        
        # commands
        await websocket.send("mode play")
        sleep(10)
        await websocket.send("mode code")

asyncio.run(connect_and_auth())
