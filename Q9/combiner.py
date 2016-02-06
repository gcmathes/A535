import math

def mag_add(mag1, mag2):
    F1 = 10 ** (-.4 * mag1)
    F2 = 10 ** (-.4 * mag2)
    combined = -2.5 * math.log10(F1 + F2)
    return combined

mag1 = input("First Magnitude Object : ")
mag2 = input("Second Magnitude Object : ")

print "Combined Magnitude : " + str(mag_add(mag1, mag2))
