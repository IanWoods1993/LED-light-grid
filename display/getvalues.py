from PIL import Image
from math import floor
SCREEN_X = 3
SCREEN_Y = 3
points = []
im = Image.open("mario.jpg") #Can be many different formats.
pix = im.load()
xDim = im.size[0]
yDim = im.size[1]
xStepSize = int(xDim / SCREEN_X)
yStepSize = int(yDim / SCREEN_Y)
print("x: " + str(xDim) + " y: " + str(yDim))
for i in range (0, xDim, xStepSize): 
    for j in range(0, yDim, yStepSize):
        points.append(pix[i, j])
        if(len(points) > SCREEN_X * SCREEN_Y):
            break

for elemt in points:
    print(elemt)
#pix[x,y] = value # Set the RGBA Value of the image (tuple)
    #ie if it was a 32 pix tall image, i'd want to jump by 2
