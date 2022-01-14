import numpy as np
#import cv2
from PIL import ImageGrab

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

    mostFrequentColor = mostFrequent(pixelArray)
    print(mostFrequentColor)
    print(mostFrequentColor[0])

    count += 1
    #print(count)