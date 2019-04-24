import aiohttp_jinja2
from aiohttp import web, MultipartReader

from ret2retro.transform import process_image_async


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'title': 'ret2retro'}


async def transform_image(request):
    multipart_data = await request.post()
    image_content = multipart_data['image'].file.read()
    result = await process_image_async(image_content)
    return web.Response(body=result, status=200)


async def redirect_to_main(request):
    return web.HTTPFound('/')
