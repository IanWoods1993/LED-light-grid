def displayFromArray(strip, positions):
    for position in positions:
        strip.setPixelColor(position, Color(0, 0, 255))