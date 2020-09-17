#timeConversion from 12 hours to 24 hours method.

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    longhours = "00:00:00"
    meridian = s[-2:]
    hours = int(s[:s.index(":")])
    if(meridian == "PM" or meridian == "pm"):
        if(hours == 12):
            pass
        else:
            hours = hours+12
    else:
        if(hours == 12):
            hours = 0
    hours = str(hours).rjust(2,"0")
    longhours = hours+s[s.index(":"):-2]
    return longhours

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
