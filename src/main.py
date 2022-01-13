import pyyaml
import tinytuya
import logging
import re
from config import config
from device import device
import struct
import operator
import Quartz.CoreGraphics as CG 
import sys
from pixelval import ScreenPixel

global y  # defines the x and y coordinates from where we will capture colors
global x  # 

# logging
log = logging.basicConfig(filename=config.log, level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log.info("-±- New Session -±-")

lights = {}

for x in range(0, config.n_lights): # set up all devices in config as tuya bulbs
    lights.update({x : tinytuya.OutletDevice(config.getuuid(x), config.getip(x), config.getlk(x))})
    lights[x].set_version(3.3)
    if config.debug: print("status of device_" + x + " is " + lights[x].status())
    lights[x].set_colour(50,255,50) # set color to green to show connection successfull.
    lights[x].set_brightness(500) # set half bright to show connection successfull.


    



