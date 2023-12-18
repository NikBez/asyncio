import asyncio

from aiohttp import ClientSession
from src.config import settings
from src.db import connection
from src.db.models import Swapi


async def swapi_handler():
    counter = 1
    while counter < 100:
        swapi_chunk = [
            get_swapi_data(person_id)
            for person_id in range(counter, counter + settings.chunk_size)
        ]
        result = await asyncio.gather(*swapi_chunk)
        cleared_persons = await clear_empty_elements(result)
        asyncio.create_task(
            connection.insert_all(
                [Swapi().from_dict(person) for person in cleared_persons]
            )
        )
        counter += settings.chunk_size
    tasks = asyncio.all_tasks() - {asyncio.current_task()}
    await asyncio.gather(*tasks)
    await connection.close_connection()


async def get_swapi_data(person_id: int):
    session = ClientSession()
    response = await session.get(f"https://swapi.dev/api/people/{person_id}/")
    json_response = await response.json()
    json_response["id"] = person_id
    await session.close()
    return json_response


async def clear_empty_elements(chunk: list):
    cleared_chunk = []
    for person in chunk:
        if not person.get("detail") == "Not found":
            cleared_chunk.append(person)
    return cleared_chunk
