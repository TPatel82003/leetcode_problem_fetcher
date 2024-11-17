import asyncio
from ..util.fetch import fetch_leetcode_question
import websockets
import logging
import json
# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

async def handler(websocket):
    client_address = websocket.remote_address
    logger.info(f"New connection from {client_address}")
    
    try:
        async for message in websocket:
            logger.info(f"Received message from {client_address}: {message}")
            question_object = json.loads(message)
            fetch_leetcode_question(question_object["titleSlug"])
            await websocket.send(f"Echo: {message}")
            logger.info(f"Sent echo back to {client_address}")
    except websockets.exceptions.ConnectionClosed as e:
        logger.warning(f"Connection closed with {client_address}: {e.code} - {e.reason}")

async def main():
    server = await websockets.serve(handler, "localhost", 1234)
    logger.info("WebSocket server started on ws://localhost:1234")
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
