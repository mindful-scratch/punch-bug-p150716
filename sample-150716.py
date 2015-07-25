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
    a = math.sqrt( axes['x']**2 + axes['y']**2) * 60

    def request(param):
        conn = httplib.HTTPSConnection("hinoqi.sakura.ne.jp")
        conn.request("GET", "/particle/push.php?p=" + str(param))

    if a < 30:
        a = 0
        if status is not STOPPED \
                and 1 < (time.time() - last_time_status_changed):
            status = STOPPED
            last_time_status_changed = time.time()
    elif 100 < a:
        a = 100
        time_moving_fast = time.time()
        if status is not MOVING_FAST \
                and 1 < (time.time() - last_time_status_changed):
            status = MOVING_FAST
            last_time_status_changed = time.time()
    else:
        # 1秒以内は「遅い」にならない
        if status is not MOVING_SLOWLY \
                and 1 < (time.time() - last_time_status_changed):
            status = MOVING_SLOWLY
            last_time_status_changed = time.time()
    request(a)

    sys.stdout.write("\r%03d" % a)
    sys.stdout.flush()
    time.sleep(0.01)