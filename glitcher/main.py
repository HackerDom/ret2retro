#! python3
import os, sys
sys.path.append(os.path.dirname(__file__))

import effects
import os
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
from effects import TransformationList

ImageType = Image.Image

STATIC_TRANSFORM = [
    (effects.convert, {'mode': 'RGB'}),
    (effects.split_color_channels, {'offset': 10}),
    (effects.sharpen, {'factor': 5.0}),
    (effects.add_transparent_pixel, {}),
    (effects.shift_corruption, {"offset_mag" : 8, "coverage" : 0.2, "width" : 8})
]

PATH = os.path.dirname(__file__)

WHITE = Image.open(os.path.join(PATH, "white.png"))
CTF = Image.open(os.path.join(PATH, "ctf.jpg")).convert("L")


def add_frame(photo):
    size = photo.size
    white = WHITE.resize(size)
    ctf = CTF.resize(size)
    merged = Image.composite(white, photo, ctf)
    return merged


def add_text(im, num):
    width = im.size[0]
    hight = im.size[1]
    font_size = hight//10
    location_x = width//3
    location_y = 6*hight//7
    location = (location_x, location_y)
    text_color = (20, 20, 100)

    helvetica = ImageFont.truetype(os.path.join(PATH, "Samson.ttf"), size=font_size)
    d = ImageDraw.Draw(im)
    d.text(location, "Hacker: {0:.1f}%".format(num*100), font=helvetica, fill=text_color)
    return im


def apply_transformations(im: ImageType, funcs: TransformationList) -> ImageType:
    transformed = im
    for func, args in funcs:
        transformed = func(transformed, **args)
    return transformed


def glitch(im, score):
    output = apply_transformations(im, STATIC_TRANSFORM)
    output = add_frame(output)
    output = add_text(output, score)
    return output


#не работает :(
def glitch_bytes_io(img_bytes, score):
    im = Image.open(img_bytes)
    result = glitch(im, score)

    buffer = BytesIO()
    result.save(buffer, format='png')
    return buffer.read()
