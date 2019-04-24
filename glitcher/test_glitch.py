import os, sys
sys.path.append(os.path.dirname(__file__))
from PIL import Image
from main import glitch

input_path = r"C:\Users\elizu\ructf\glitcher\glitch_me\glitch_me\a.jpg"
output_dir = r"C:\Users\elizu\ructf\glitcher\glitch_me\glitch_me"
im = Image.open(input_path)
output = glitch(im, 0.5555)
basename = os.path.basename(input_path)
outname = '{}_glitch.png'.format(os.path.splitext(basename)[0])
out_path = os.path.join(output_dir, outname)
output.save(out_path)
im.close()

