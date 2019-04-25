import os, sys
sys.path.append(os.path.dirname(__file__))
from main import glitch_bytes_io
from io import BytesIO

input_path = r"C:\Users\elizu\ructf\glitcher\glitch_me\glitch_me\a.jpg"
output_dir = r"C:\Users\elizu\ructf\glitcher\glitch_me\glitch_me"
result = ""
with open(input_path, "rb") as file:
    result = glitch_bytes_io(BytesIO(file.read()), 0.555)
basename = os.path.basename(input_path)
outname = '{}_glitch1.png'.format(os.path.splitext(basename)[0])

with open(outname, "wb") as file:
    file.write(result)

