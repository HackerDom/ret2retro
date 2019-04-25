import os, sys
sys.path.append(os.path.dirname(__file__))
from main import glitch_bytes_io
from io import BytesIO

PATH = os.path.dirname(__file__)

input_path = os.path.join(PATH, "pict", "a.jpg")
output_dir = os.path.join(PATH, "pict")
result = ""
with open(input_path, "rb") as file:
    result = glitch_bytes_io(BytesIO(file.read()), 0.555)
basename = os.path.basename(input_path)
outname = '{}_glitch1.png'.format(os.path.splitext(basename)[0])

with open(outname, "wb") as file:
    file.write(result)

