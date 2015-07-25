# coding=utf-8

from adxl345 import ADXL345
import math, time, sys
import httplib
  
adxl345 = ADXL345()

STATUS = (
    STOPPED,
    MOVING_SLOWLY,
    MOVING_FAST
) = range(0, 3)

status = STOPPED
last_time_status_changed = 0

while True:
    axes = adxl345.getAxes(True)
    a = math.sqrt( axes['x']**2 + axes['y']**2) * 100

    if a < 30:
        a = 0
        # 1秒以内は「停止」にならない
        if status is not STOPPED \
                and 1 < (time.time() - last_time_status_changed):
            status = STOPPED
            # print "stopped"
            last_time_status_changed = time.time()
            sys.stdout.write("\r stopped      ")
    elif 100 < a:
        a = 100
        time_moving_fast = time.time()
        # 1秒以内は「速い」にならない
        if status is not MOVING_FAST \
                and 1 < (time.time() - last_time_status_changed):
            status = MOVING_FAST
            # print "moving fast"
            last_time_status_changed = time.time()
            sys.stdout.write("\r moving fast  ")
    else:
        # 1秒以内は「遅い」にならない
        if status is not MOVING_SLOWLY \
                and 1 < (time.time() - last_time_status_changed):
            status = MOVING_SLOWLY
            # print "moving slowly"
            last_time_status_changed = time.time()
            sys.stdout.write("\r moving slowly")

    # sys.stdout.write("\r%f" % last_time_status_stopped)
    # sys.stdout.write(
        # "\r stopped: %f" % (time.time() - last_time_status_stopped) +
        # " fast: %f" % (time.time() - last_time_status_moving_fast) +
        # " slowly: %f" % (time.time() - last_time_status_moving_slowly))
        # "\r %d " % status + " %f" % (time.time() - last_time_status_changed))
    sys.stdout.flush()
    time.sleep(0.01)

    # print "%.0f" % ( a )