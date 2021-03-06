import math
import re
from util.timeConvert import convert
def makeSlotTime(daytime_sep,strend_sep,day_time):
    
    day,time=day_time.strip().split(daytime_sep,1)
    day=day[:3].upper()
    start,time=map(lambda x: convert(float(x)),re.findall("\d+\.\d+",time))
    # print(start,time)
    # print('olaola')
    return day,start,time

