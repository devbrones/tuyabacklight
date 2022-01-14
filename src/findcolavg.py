# create sum of all in r and divide sum by amount of numbers (2560*1400) [1][2][3]
# do the same for the other two values

def averageColor(array):
    avgr1 = 0
    avgg1 = 0
    avgb1 = 0
    avgr2 = 0
    avgg2 = 0
    avgb2 = 0
    for x in range(1508): # set your own resolution here.
        avgr1 += array[x][0]
        avgg1 += array[x][1]
        avgb1 += array[x][2]
    avgr2 = avgr1/1508
    avgg2 = avgg1/1508 
    avgb2 = avgb1/1508 
    retarr = [round(avgr2), round(avgg2), round(avgb2)]
    return retarr