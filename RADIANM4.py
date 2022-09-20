from cmath import pi
import math
#Small functions to solve math from liber m4 book, number in the end is the exercis

#convert degrees to rads 1406
def degreesToRadians(d):
    rads = d*pi*(1/180)
    return rads

#Convert radians to degrees 1407
def radiansToDegrees(rads):
    degrees = rads*180*(1/pi)
    return degrees



#print(radiansToDegrees(1))

print(degreesToRadians(0.5))


 

