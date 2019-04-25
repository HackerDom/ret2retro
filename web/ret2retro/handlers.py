import aiohttp_jinja2
from aiohttp import web

from ret2retro.exceptions import ValidationError
from ret2retro.transform import process_image_async
from ret2retro.validate import clean_file


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}


async def transform_image(request):
    multipart_data = await request.post()
    try:
        *_, content = clean_file(multipart_data)
    except ValidationError as ve:
        response = aiohttp_jinja2.render_template('index.html', request, {
            'errors': {
                ve.field_name: ve.errors
            }
        })
        response.set_status(400)
        return response
    name, result, extension = await process_image_async(content)
    return web.Response(body=result, content_type=f'image/{extension}', headers={
        'Content-Disposition': f'attachment; filename="{name}.{extension}"'
    }, status=200)


async def redirect_to_main(request):
    return web.HTTPFound('/')