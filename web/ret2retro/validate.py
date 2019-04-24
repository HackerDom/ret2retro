from aiohttp.web_request import FileField

from ret2retro.config import ALLOWED_UPLOAD_CONTENT_TYPES
from ret2retro.exceptions import ValidationError


def clean_file(multipart_data):
    if 'image' not in multipart_data:
        raise ValidationError('image', ['Обязательное поле'])
    image_part = multipart_data['image']
    if not isinstance(image_part, FileField):
        raise ValidationError('image', ['Обязательное поле'])
    content_type = image_part.content_type
    if content_type not in {f'image/{t}' for t in ALLOWED_UPLOAD_CONTENT_TYPES}:
        raise ValidationError('image', [f'Форматы которые поддерживают {", ".join(ALLOWED_UPLOAD_CONTENT_TYPES)}'])
    image_file = image_part.file
    name, data = image_part.filename, image_file.read()
    return name, content_type, data
