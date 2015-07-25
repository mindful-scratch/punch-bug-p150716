from adxl345 import ADXL345
import math
import httplib
  
adxl345 = ADXL345()

STATUS = (
    STOP,
    MOVING_SLOWLY,
    MOVING_FAST
) = range(0, 3)

status = STOP

while True:
    axes = adxl345.getAxes(True)
    a = math.sqrt( axes['x']**2 + axes['y']**2) * 100

    if a < 10:
        a = 0
        if status is not STOP:
            status = STOP
            print "stopped"
    elif 100 < a:
        a = 100
        if status is not MOVING_FAST:
            status = MOVING_FAST
            print "moving fast"
    else:
        if status is not MOVING_SLOWLY:
            status = MOVING_SLOWLY
            print "moving slowly"

    # print "%.0f" % ( a )