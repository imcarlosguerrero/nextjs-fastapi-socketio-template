import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connection established")

@sio.event
async def disconnect():
    print("Disconnected from server")

# The connection will be established to the server at port 3000.
# This is port where the Next.js app is running.

async def main():
    await sio.connect(
        "ws://localhost:3000",
        socketio_path="/api/socket.io",
        transports=["websocket"],
    )
    await sio.wait()

if __name__ == "__main__":
    asyncio.run(main())