from adxl345 import ADXL345
import math
  
adxl345 = ADXL345()
    
while True:
    axes = adxl345.getAxes(True)
    a = math.sqrt( axes['x']**2 + axes['y']**2) * 100

    if a < 10:
        a = 0
    elif 100 < a:
        a = 100

    print "%.0f" % ( a )