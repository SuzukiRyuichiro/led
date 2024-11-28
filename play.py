import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 60, brightness=1)
pixels.fill((0,0,255))

pixels[20] = (189,40,32)

time.sleep(2)

x= 0
while x<60:

    pixels[x] = (255, 0, 0)
    pixels[x-5] = (255, 0, 100)
    pixels[x-10] = (0, 0, 255)
    #Add 1 to the counter
    x=x+1
    #Add a small time pause which will translate to 'smoothly' changing colour
    time.sleep(0.05)
    if x == 60:
        x = 0

