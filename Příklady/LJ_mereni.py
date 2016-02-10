# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 18:04:14 2016

@author: XAXA
"""

import time
import u3
d = u3.U3()
d.configU3()

d.getCalibrationData()




for i in range(20):
    ain0bits, = d.getFeedback(u3.AIN(0)) # Read from raw bits from AIN0


    ainValue = d.binaryToCalibratedAnalogVoltage(ain0bits, isLowVoltage = False, channelNumber = 0)
    print ainValue
    time.sleep(0.00005)

d.close()