#!/usr/bin/python

import time, sys
import gen_gradient
from dotstar import Adafruit_DotStar

primary = ['#e70000', '#ff8c00', '#ffef00', '#00811f', '#0044ff', '#760089']

colors = gen_gradient.calculate(primary)

factor = 2  # multiple of number of colors
numColors = len(colors)
numPixels = numColors * factor

# Here's how to control the strip from any two GPIO pins:
datapin = 17
clockpin = 27
strip = Adafruit_DotStar(numPixels, datapin, clockpin)
strip.begin()           # Initialize pins for output
strip.setBrightness(64)  # Limit brightness to ~1/4 duty cycle

change_every = int(numPixels / numColors)

def getRGB(h):
    cs = h.lstrip('#')
    return tuple(int(cs[i:i+2], 16) for i in (0, 2, 4))


every_pixel = []
for i in range(numPixels):
    pixel = int(i / change_every)
    every_pixel.append(colors[pixel])
print numColors

while True:
    for i in range(len(every_pixel)):
        rgb = getRGB(every_pixel[i-1])
        strip.setPixelColor(i, rgb[0], rgb[1], rgb[2])
    last_value = every_pixel.pop()
    every_pixel.insert(0, last_value)
    strip.show()                     # Refresh strip
    time.sleep(0.13)
