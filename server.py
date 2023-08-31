import asyncio
import websockets

async def handle_client(websocket, path):
    async for mess in websocket:
        print(f"Received message: {mess}")
        res = f"Server received: {mess}"
        await websocket.send(res)
        print(f"Sent response: {res}")

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
