# LED Light Grid
This is a project I work on not-very-often. 

The idea is to make 8x8 grids of [LED lights](https://www.amazon.com/gp/product/B00ZHB9M6A/ref=oh_aui_search_detailpage?ie=UTF8&psc=1) into what I've been calling a "superpixel". This is a display element that can display a single letter on 64 individual light-pixels. It's useful to introduce this terminology because these grids are fixed and an effective unit of meaning.

Hooking the Raspberry Pi up to the lights is done as follows:
https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring

Helpful documentation: 
http://pi4j.com/pins/model-3b-rev1.html

Notes for next year / whenever I run this again / whoever uses this thing

This used to be a python project but is now a processing project. Processing is better for this because it's easy to use with these light controllers called FadeCandy.

FadeCandy controllers can be hooked together via a network and that makes it easy to have lots of lights running together.

Start the fcserver.exe executable to start the fadecandy server. Better instructions can be found here https://github.com/scanlime/fadecandy

Without that stuff this would be way harder.
