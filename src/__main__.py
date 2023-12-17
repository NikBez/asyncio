import aiohttp
import asyncio

from src.db.connection import connection
from src.swapi import swapi_handler


async def main():
    await connection.init_models()
    await swapi_handler()


if __name__ == "__main__":
    asyncio.run(main())
