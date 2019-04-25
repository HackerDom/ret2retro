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

def add_pictured_frame(im):
    font_size = min(im.size[0], im.size[1])//20
    text_color = (256, 256, 256)
    back_color = (256, 256, 256)
    shift = min(im.size[0], im.size[1])//13
    length = 2*shift
    width =  shift//8

    text =  "PLAY >"
    font = ImageFont.truetype(os.path.join(PATH, "Samson.ttf"), size=font_size)
    location = (1.8*shift, 1.8*shift)
    d = ImageDraw.Draw(im)
    d.rectangle((shift, shift, shift + length, shift + width), fill=back_color)
    d.rectangle((shift, shift, shift + width, shift + length), fill=back_color)
    d.text(location, text, font=font, fill=text_color)

    text =  "03:13:37"
    font = ImageFont.truetype(os.path.join(PATH, "Samson.ttf"), size=font_size)
    text_size = font.getsize(text)
    location = (im.size[0] - 1.8*shift-text_size[0], 1.8*shift)
    d = ImageDraw.Draw(im)
    d.rectangle((im.size[0] - shift - length, shift, im.size[0] - shift, shift + width), fill=back_color)
    d.rectangle((im.size[0] - shift - width, shift, im.size[0] - shift, shift + length), fill=back_color)
    d.text(location, text, font=font, fill=text_color)

    up = 1.5
    text1 = "#RUCTF"
    text2 =  "#ret2retro"
    font = ImageFont.truetype(os.path.join(PATH, "Samson.ttf"), size=font_size)
    text_size2 = font.getsize(text2)
    text_size1 = font.getsize(text1)
    location1 = (im.size[0] - 1.8*shift-text_size1[0], im.size[1] - (up+0.8)*shift - 2*text_size1[1])
    location2 = (im.size[0] - 1.8*shift - text_size2[0], im.size[1] - (up+0.8)*shift - text_size2[1])
    d = ImageDraw.Draw(im)
    d.rectangle((im.size[0] - shift - length, im.size[1] - up*shift - width, im.size[0] - shift, im.size[1] - up*shift), fill=back_color)
    d.rectangle((im.size[0] - shift - width, im.size[1] - up*shift - length, im.size[0] - shift, im.size[1] - up*shift), fill=back_color)
    d.text(location2, text2, font=font, fill=text_color)
    d.text(location1, text1, font=font, fill=text_color)

    text1 =  "YEKATERINBURG"
    text2 = "APR. 26-29 2019"
    font = ImageFont.truetype(os.path.join(PATH, "Samson.ttf"), size=font_size)
    text_size = font.getsize(text)
    location2 = (1.8*shift, im.size[1] - (up+0.8)*shift-text_size[1])
    location1 = (1.8*shift, im.size[1] - (up+0.8)*shift-2*text_size[1])
    d = ImageDraw.Draw(im)
    d.rectangle((shift, im.size[1] - up*shift - width, shift + length, im.size[1] - up*shift), fill=back_color)
    d.rectangle((shift, im.size[1] - up*shift - length, shift + width, im.size[1] - up*shift), fill=back_color)
    d.text(location2, text2, font=font, fill=text_color)
    d.text(location1, text1, font=font, fill=text_color)
    return im

def add_text(im, num):
    font_size = min(im.size[0], im.size[1])//10
    text_color = (0, 0, 0)
    back_color = (256, 256, 256)
    text =  "HACKERNESS: {0:.3f}".format(num)
    font = ImageFont.truetype(os.path.join(PATH, "Samson.ttf"), size=font_size)
    text_size = font.getsize(text)

    loc_x = (im.size[0]-text_size[0])//2
    loc_y = im.size[1]-font_size*1.1

    location = (loc_x, loc_y)
    d = ImageDraw.Draw(im)
    d.rectangle((loc_x - text_size[0]*0.02, loc_y + text_size[1]*0.2, loc_x + text_size[0]*1.01, loc_y + text_size[1]*1.15), fill=back_color)
    d.text(location, text, font=font, fill=text_color)
    return im


def apply_transformations(im: ImageType, funcs: TransformationList) -> ImageType:
    transformed = im
    for func, args in funcs:
        transformed = func(transformed, **args)
    return transformed


def glitch(im, score):
    output = apply_transformations(im, STATIC_TRANSFORM)
    output = add_pictured_frame(output)
    output = add_text(output, score)
    return output


def glitch_bytes_io(img_bytes, score):
    im = Image.open(img_bytes)
    result = glitch(im, score)

    buffer = BytesIO()
    result.save(buffer, format='png')
    buffer.name = 'test.png'
    buffer.seek(0)
    return buffer.read()
