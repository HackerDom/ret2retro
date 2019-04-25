import hashlib

from glitcher.main import glitch_bytes_io

from io import BytesIO

from functools import partial
from asyncio import get_event_loop
from concurrent.futures import ProcessPoolExecutor

from ret2retro.storages.fs_storage import FsStorage
from ret2retro.config import UPLOAD_PATH, IS_PRODUCTION

process_pool_executor = ProcessPoolExecutor()


def process_image(data):
    storage = FsStorage(UPLOAD_PATH)
    md5 = hashlib.md5()
    md5.update(data)
    name = md5.hexdigest()[:16]
    filename = f'{name}.png'
    transformed_data = storage.get_resource(filename)
    if not transformed_data:
        buffer = BytesIO(data)
        transformed_data = glitch_bytes_io(buffer, 0.1)
        storage.add_resource(filename, transformed_data)
    extension = 'png'
    return filename, transformed_data, extension


async def process_image_async(data):
    loop = get_event_loop()
    if IS_PRODUCTION:
        name, transformed_image, extension = await loop.run_in_executor(
            process_pool_executor,
            partial(process_image, data)
        )
    else:
        name, transformed_image, extension = process_image(data)
    return name, transformed_image, extension
