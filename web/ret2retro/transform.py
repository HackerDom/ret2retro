import hashlib

from glitcher.main import glitch_bytes_io

from io import BytesIO

from functools import partial
from asyncio import get_event_loop
from concurrent.futures import ProcessPoolExecutor


process_pool_executor = ProcessPoolExecutor()


def process_image(data):
    md5 = hashlib.md5()
    md5.update(data)
    name = md5.hexdigest()[:16]

    buffer = BytesIO(data)
    transformed_data = glitch_bytes_io(buffer, 0.1)
    extension = 'png'
    return name, transformed_data, extension


async def process_image_async(data):
    loop = get_event_loop()
    # name, transformed_image = await loop.run_in_executor(
    #     process_pool_executor,
    #     partial(process_image, data)
    # )
    name, transformed_image, extension = process_image(data)
    return name, transformed_image, extension
