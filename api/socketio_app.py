from socketio import ASGIApp, AsyncServer
from api.logger import setup_logger
from api.app import app

logger = setup_logger("Socket.IO App")

# Set `cors_allowed_origins` to `["*"]` to allow connections from any origin.
# Alternatively, set it to a list of specific URLs to allow connections only from those URLs.
# By default, it allows connections from the same origin as the app.

socketio_server = AsyncServer(
    async_mode="asgi",
)

socketio_app = ASGIApp(
    socketio_server=socketio_server,
    socketio_path="/api/socket.io",
    other_asgi_app=app
)

@socketio_server.event
async def connect(sid, environ):
    logger.info(f"Client {sid} connected")
    
@socketio_server.event
async def disconnect(sid):
    logger.info(f"Client {sid} disconnected")