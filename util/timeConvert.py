import math
def convert(tme):
    tme=int(tme)+round(math.modf(tme)[0],2)/.6
    if(tme<7):
        tme+=12
    return tme