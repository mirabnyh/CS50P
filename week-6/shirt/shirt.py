import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

root1, extension1 = os.path.splitext(sys.argv[1])
root2, extension2 = os.path.splitext(sys.argv[2])

if extension1.lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
if extension2.lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
if extension1.lower() != extension2.lower():
    sys.exit("Input and output have different extensions ")

try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(image, size, Image.Resampling.BICUBIC, 0.0, (0.5, 0.5))
    image.paste(shirt, shirt)
    image.save(sys.argv[2])
    
except FileNotFoundError:
    sys.exit("Input does not exist")
