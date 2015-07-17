# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

from adxl345 import ADXL345
import math
  
adxl345 = ADXL345()
    
while True:
	axes = adxl345.getAxes(True)
	a = math.sqrt( axes['x']**2 + axes['y']**2) * 100
	print "%.0f" % ( a )
