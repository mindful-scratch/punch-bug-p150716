# coding=utf-8

from adxl345 import ADXL345
import math, httplib
  
adxl345 = ADXL345()

def request(param):
    conn = httplib.HTTPSConnection("hinoqi.sakura.ne.jp")
    conn.request("GET", "/particle/push.php?p=" + str(param))

while True:
    axes = adxl345.getAxes(True)
    a = math.sqrt( axes['x']**2 + axes['y']**2) * 40

    if a < 10:
        a = 0
    elif 100 < a:
        a = 100
    request(a)