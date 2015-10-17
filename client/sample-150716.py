# coding=utf-8

from adxl345 import ADXL345
import math, httplib, time, threading

class Requester(threading.Thread):
    def __init__(self):
        super(Requester, self).__init__()
        self.power = 0
        # self._conn = httplib.HTTPSConnection("hinoqi.sakura.ne.jp")
    def request(self, power):
        conn = httplib.HTTPSConnection("hinoqi.sakura.ne.jp")
        conn.request("GET", "/particle/push.php?p=" + str(power))
        # self._conn.request("GET", "/particle/push.php?p=" + str(power))
        print "requested"
# def request(param):
#     conn = httplib.HTTPSConnection("hinoqi.sakura.ne.jp")
#     conn.request("GET", "/particle/push.php?p=" + str(param))
#         request(power)

adxl345 = ADXL345()


aList = []
azBefore = 0
i = 0
requester = Requester()
requester.start()

while True:
    axes = adxl345.getAxes(True)
    # ax    = axes['x']
    ay    = axes['y']
    # azNew = axes['z']
    # print "{0:.2f}".format(ax)+","+"{0:.2f}".format(ay)+","+"{0:.2f}".format(azNew)
    # if 0 < ax and 0 < ay:
    #     # an = math.sqrt( ax**2 + ay**2 + azNew**2 ) * 200 - 160
    #     an = math.sqrt( ax**2 + ay**2 ) * 60
    #     # print int(math.sqrt( ax**2 + ay**2 ) * 60)
    # else:
    #     an = 0

    power = int(-ay * 40)
    if 100 < power:
        power = 100
    print power
    if 30 < power:
        requester.request(power)
        i = 0
        # request(power)
    i += 1
    if i == 200:
        # request(0)
        requester.request(0)
    an = 0  # Fake code
    aAve = an
    # azBefore = azNew
    # if an < 0:
    #     an = 0
    # aList.append(int(an))

    # if 3 < len(aList):
    #     aAve = (aList[-1] + aList[-2] + aList[-3] + aList[-4]) / 4
    # if 1 < len(aList):
    #     aAve = (aList[-1] + aList[-2]) / 2
    # else:
    #     aAve = 0
    n = int(aAve / 10)
    # if 5 < n:
    #     n -= 5
    # else:
    #     n = 0

    gage = ""
    if 1 <= n:
        for i in range(n):
            gage += "#"
    # print gage

    # if aAve < 10:
    #     aAve = 0
    # elif 100 < aAve:
    if 100 < aAve:
        aAve = 100
    # print aAve
    # request(aAve)
    # time.sleep(0.001)