"""
This example uses Python's built-in threading module to reach faster streaming 
speeds than streamTest.py.

On a Ubuntu 9.10 machine with a AMD Athlon(tm) 64 X2 Dual Core Processor 5200+,
we got speeds up to 50kHz.

On a Mac OS 10.6 machine with a 2.53 GHz Intel Core 2 Duo Processor, we got
speeds up to 50kHz.

On a Mac OS 10.5 machine with a 1.42 GHz G4 Processor, we saw max speeds of
about 40kHz.
"""

import copy
import sys
import threading
from datetime import datetime

try:
  import Queue
except ImportError: # Python 3
  import queue as Queue
import time
import u3


# MAX_REQUESTS is the number of packets to be read.
MAX_REQUESTS = 2500

d = None

d = u3.U3()

# to learn the if the U3 is an HV
d.configU3()

# For applying the proper calibration to readings.
d.getCalibrationData()

# Set the FIO0 to Analog

d.configIO(FIOAnalog = 2)
print "configuring U3 stream"

d.streamConfig( NumChannels = 1, PChannels = [ 1 ], NChannels = [ 31 ], Resolution = 3, SampleFrequency = 20100 )


if d is None:
    print "Configure a device first.\nPlease open streamTest-threading.py in a text editor and uncomment the lines for your device, starting at about line 16.\n\nExiting..."
    sys.exit(0)
    
class StreamDataReader(object):
    def __init__(self, device):
        self.device = device
        self.data = Queue.Queue()
        self.dataCount = 0
        self.missed = 0
        self.running = False

    def readStreamData(self):
        self.running = True
        
        start = datetime.now()
        self.device.streamStart()
        while self.running:
            # Calling with convert = False, because we are going to convert in
            # the main thread.
            returnDict = self.device.streamData(convert = False).next()
            
            self.data.put_nowait(copy.deepcopy(returnDict))
            
            self.dataCount += 1
            if self.dataCount > MAX_REQUESTS:
                self.running = False
        
        print "stream stopped."
        self.device.streamStop()
        stop = datetime.now()

        total = self.dataCount * self.device.packetsPerRequest * self.device.streamSamplesPerPacket
        print "%s requests with %s packets per request with %s samples per packet = %s samples total." % ( self.dataCount, d.packetsPerRequest, d.streamSamplesPerPacket, total )
        
        print "%s samples were lost due to errors." % self.missed
        total -= self.missed
        print "Adjusted number of samples = %s" % total
        
        runTime = (stop-start).seconds + float((stop-start).microseconds)/1000000
        print "The experiment took %s seconds." % runTime
        print "%s samples / %s seconds = %s Hz" % ( total, runTime, float(total)/runTime )
d.writeRegister(5000,1)
time.sleep(1)

Umax=0
Umin=0

sdr = StreamDataReader(d)

sdrThread = threading.Thread(target = sdr.readStreamData)

# Start the stream and begin loading the result into a Queue
sdrThread.start()


start=time.clock()

while time.clock()-start<30:

    result = sdr.data.get(True, 1)
        

         
    r = d.processStreamData(result['result'])
    print "Average of", len(r['AIN1']), "reading(s):", sum(r['AIN1'])/len(r['AIN1']) ,     "max =", max(r['AIN1']),"V","min =", min(r['AIN1']),"V"
    
    q=min(r['AIN1']) 
    if Umin>q:
        Umin=min(r['AIN1'])
    w=max(r['AIN1']) 
    if Umax<w:
        Umax=max(r['AIN1'])
print d.processStreamData(result['result'])




print"Umax =", Umax, "Umin =",Umin






"""



d.configU3()

# For applying the proper calibration to readings.
d.getCalibrationData()
# Set the FIO0 to Analog
d.configIO(FIOAnalog = 1)
print "configuring U3 stream"
d.streamConfig( NumChannels = 0, PChannels = [ 1 ], NChannels = [ 31 ], Resolution = 3, SampleFrequency = 20100 )








d.writeRegister(5000,2)
time.sleep(1)




start=time.clock()
while time.clock()-start<3:
    result = sdr.data.get(True, 1)     
    r = d.processStreamData(result['result'])
    print "Average of", len(r['AIN0']), "reading(s):", sum(r['AIN0'])/len(r['AIN0'])      
       
    
print max(r['AIN0'])




"""












sdr.running = False