import os
import hashlib

from functools import partial
from asyncio import StreamReader, get_event_loop
from concurrent.futures import ProcessPoolExecutor

from ret2retro.config import UPLOAD_PATH

process_pool_executor = ProcessPoolExecutor()


def process_image(data):
    md5 = hashlib.md5()
    md5.update(data)
    name = md5.hexdigest()[:16]
    # Process image here
    return name, data


async def process_image_async(data):
    loop = get_event_loop()
    name, transformed_image = await loop.run_in_executor(
        process_pool_executor,
        partial(process_image, data)
    )
    return (name, transformed_image)
