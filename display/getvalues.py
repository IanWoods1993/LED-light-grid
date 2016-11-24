from neopixel import *
from PIL import Image
from math import floor

LED_COUNT      = 150
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

SCREEN_X       = 12       # Number of pixels in the x dimension of the screen
SCREEN_Y       = 12       # Number of pixels in the y dimension of the screen


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
points = []
im = Image.open("../images/mario.jpg") #Can be many different formats.
pix = im.load()
xDim = im.size[0]
yDim = im.size[1]
xStepSize = int(xDim / SCREEN_X)
yStepSize = int(yDim / SCREEN_Y)
shouldBreak = False
for i in range (0, xDim, xStepSize): 
    for j in range(0, yDim, yStepSize):
        points.append(pix[i, j])
        if(len(points) > SCREEN_X * SCREEN_Y):
            shouldBreak = True
            break
    if (shouldBreak):
        break

print(type(points[1][1]))

for i in range (0, len(points)):
    print("setting pixel " + str(i) + " with color " + str(points[i][0]) + " " + str(points[i][1]) + " " + str(points[i][2]))
    strip.setPixelColor(i, Color(points[i][0], points[i][1], points[i][2]))

strip.show() #will need to translate between this, which thinks it's linear, and the actual orientation

