Simple test of Micropython on ESP8266 microcontroller.

Prints text on TFT display, runs webserver on the MCU with a webpage that can
input data to the TFT. Has some issues, poorly tested and not optimized. Based 
heavily on Adafruit examples.

Tested with...
Hardware:
Adafruit Feather HUZZAH with ESP8266 WiFi
Adafruit 320x240 TFT FeatherWing

Firmware:
esp8266-20171101-v1.9.3.bin

Adafruit libraries:
rgb.py
ili9341.py
https://github.com/adafruit/micropython-adafruit-rgb-display


The MIT License (MIT)

Copyright (c) 2018 Arttu H.
