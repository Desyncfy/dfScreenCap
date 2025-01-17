import asyncio
import websockets
from time import sleep
import utils


async def connect_and_auth():

    async with websockets.connect("ws://127.0.0.1:31375") as websocket:
        # look at me putting things in variables for code readablity
        requested_scopes = "inventory"
        print("Waiting for authentication...")
        await websocket.send(f"scopes {requested_scopes}")
        while 1:
            response = await websocket.recv()
            print(f"INC {response}")
            # don't do anything until authentication
            if response == "auth":
                break # we exit the loop and allow stuff to run
        
        # Countdown
        for i in range(1,6):
            print(f"Activating in {6-i}...")
            sleep(1)

        # Logic Attempt 2
        while 1:
            utils.getScreenToCSV()
            
            latest = utils.readCSV("latest.csv")
            
            send = 'setinv [{Slot:1b,count:1,id:"minecraft:iron_nugget",components:{"minecraft:custom_data":{PublicBukkitValues:{',latest,'}}}}]'
            "".join(latest)
            await websocket.send(send)
            #sleep(2) # DiamondFire is taking way too long to process my bullcrap so give it some time


asyncio.run(connect_and_auth())
