from PIL import Image
import numpy as np

def pixelValuesFromImage():
	im = Image.open("mario-big.png")
	pixelValues = np.array(im)
	xDim = int(input("Enter xDim: "))
	yDim = int(input("Enter yDim: "))
	size = xDim, yDim
	im.thumbnail(size, Image.BILINEAR)
	im.save("tmp.png", "PNG")
	im = Image.open("tmp.png")
	pixelValues = np.array(im)
	print(pixelValues)

pixelValuesFromImage()
