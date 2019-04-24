from functools import partial
from asyncio import StreamReader, get_event_loop
from concurrent.futures import ProcessPoolExecutor

process_pool_executor = ProcessPoolExecutor()


def process_image(data):
    # Process image here
    return data


async def process_image_async(data):
    loop = get_event_loop()
    transformed_image = await loop.run_in_executor(
        process_pool_executor,
        partial(process_image, data)
    )
    return transformed_image
