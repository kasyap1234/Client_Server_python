import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            prompt = input("Enter message to send to server (or 'exit' to quit): ")
            await websocket.send(prompt)
            
            if prompt.lower() == "exit":
                break
            
            res = await websocket.recv()
            print(f"Received response: {res}")

asyncio.get_event_loop().run_until_complete(send_message())
