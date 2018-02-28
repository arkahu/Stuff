# -*- coding: utf-8 -*-
"""
ESP8266 code for controlling Adafruit 320x240 TFT FeatherWing.

Fonts are read from fontlibrary file.
"""

import fontlib_rot as flib
import machine, ili9341, rgb
spi = machine.SPI(1, baudrate=32000000)
display = ili9341.ILI9341(spi, cs=machine.Pin(0), dc=machine.Pin(15))


def reset():
    display.fill(0)

#define color (R,G,B)
r = rgb.color565(255,0,0)

def boollist(num):
    listbool = []
    for a in range(0,8):
            listbool.append (bool( num & (1<<a)))
    return listbool


def drawtext(text, color=r, func=display.fill_rectangle, scaling=1):
    #fill_rectangle(x, y, width, height, color)
    x = 240 - 8*scaling 
    ylocal = 0 

    #each character in text
    for char in text:

        fontlist = flib.givefont(char)
        #each pixel line in char
        for line in fontlist:
            cbool = boollist(line)[::-1] #may need reversing [::-1]
            xlocal = x
            
            #each pixel in line
            for b in cbool:
                if b == True:
                    dcolor = color
                else:
                    dcolor = 0
                func(xlocal,ylocal,scaling,scaling,dcolor)
                xlocal += scaling
            ylocal += 1
        ylocal +=2 #space between chars
        if ylocal >= 320-8*scaling:
            ylocal = 0
            x -= 8*scaling +2 # down character size + row space
            if x < 0 :
                return 'out of lines' 


