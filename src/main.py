import yaml
import tinytuya
import logging
import re
from config import config
#from device import device
import numpy as np
#import cv2
from PIL import ImageGrab
import statistics
from findcolavg import averageColor

global y  # defines the x and y coordinates from where we will capture colors
global x  # 

# logging
log = logging.basicConfig(filename=config.log, level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
#log.info("-±- New Session -±-")

lights = {}

config = config()

for x in range(0, 3): # set up all devices in config as tuya bulbs
    print("setting up device " + str(x))
    lights.update({x : tinytuya.BulbDevice(config.getuuid(x), config.getip(x), config.getlk(x))})
    lights[x].set_version(3.3)
    lights[x].turn_on()
    if config.debug: print("status of device_" + x + " is " + lights[x].status())
    lights[x].set_colour(50,255,50) # set color to green to show connection successfull.
    lights[x].set_brightness(500) # set half bright to show connection successfull.

# thank you u/Spiredlamb (https://www.reddit.com/r/learnpython/comments/ly8doh/comment/gpt1yfl/?utm_source=share&utm_medium=web2x&context=3)
def mostFrequent(List):
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 

step = 50
num_pixel = 1440//step * 2560//step
count = 0
while True:
    img = ImageGrab.grab()
    imgNP = np.array(img)

    im_arr = np.frombuffer(img.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((img.size[1], img.size[0], 4))
    r = g = b = 0
    pixelArray = []
    for y in range(0, 1440, step):
        for x in range(0, 2560, step):
            px = im_arr[y][x]
            pixelArray.append([px[0], px[1], px[2]])
    mostFrequentColor = averageColor(pixelArray)

    for x in range(0, 3):
        #
        lights[x].set_colour(mostFrequentColor[0], mostFrequentColor[1], mostFrequentColor[2])
        #lights[x].set_brightness(1000)
    #print(mostFrequentColor)

    #count += 1


