# XmasLights2016
Notes for next year / whenever I run this again / whoever uses this thing

You have to use sudo to run most of the python files that touch the light library.

The getvalues.py script is used for feeding in an image and displaying it on the light strip. This is a crappy name, and I should change it.

I'm gonna use the term superpixel to mean a block of 8x8 pixels (ie, one of the wooden cutouts with a bunch of LEDs on them that I'm gonna make).

There are a bunch of files, A.py - Z.py. It looks like they're static methods that display a letter. Great! But they will only work if the superpixel grid is nX1 - ie, a straight line. I need to alter it so it can display something sensible in any orientation.
