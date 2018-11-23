from PIL import Image
import numpy as np
def main():

        im = Image.open("mario-big.png")
        pixelValues = np.array(im)
        xDim = int(input("Enter xDim: "))
        yDim = int(input("Enter yDim: "))
        imageXDim = im.size[0]
        imageYDim = im.size[1]

        xFactor = imageXDim / xDim
        yFactor = imageYDim / yDim
        xSamples = range(0, imageXDim, xFactor)
        ySamples = range(0, imageYDim, yFactor)

        outputArray = [[0] * xDim for i in range(yDim)]
        for x in xSamples:
                for y in ySamples:
                        print(pixelValues[y][x]) # confusingly, the original image is 24x32 but this array is 32x24


def printList(listComprehension):
        for i in listComprehension:
                print(i)

main()
# This file is dumb and i should just use the PIL Image.thumbnail method
