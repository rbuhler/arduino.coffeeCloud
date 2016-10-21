import sys
import random
import datetime
import calendar
import json

sys.path.append('lib')

# DEVICE IDENTIFICATION
sAccount   = '' #'p1941020166trial'
sDevice    = '' #'9e8f52bf-281c-4fbc-9a34-9cd8e58710b5'
sToken     = '' #'31479766523918bd1ef473b1d1a8b1a2'
sMsgType   = '' #'ba2434ef5c2b4bc8de83'
sProxy     = '' #'http://proxy:8080'

sSensor    = '' #'Python'
iValue     = 0
iTimeStamp = 0

sPort      = '/dev/cu.usbmodem411'
iBRate     = 9600

#RANDOM VALUE (pretend a real random reading)
# iValue1 = random.randrange(0, 100)
# iValue2 = random.randrange(0, 100)
# iValue3 = random.randrange(0, 100)

# CURRENT DATE
# nTimes = 0
# while nTimes <= 2:
# # Get the current date
# 	dToday      = datetime.datetime.now() + datetime.timedelta(seconds = 5 * nTimes)
# # Cast current date format into Tuple
# 	dDate_tuple = dToday.timetuple()
# # Cast the Tuple format into UTC (seconds from January 1970)
# 	if nTimes == 0:
# 		dDate_UTC1 = calendar.timegm( dDate_tuple )
# 	if nTimes == 1:
# 		dDate_UTC2 = calendar.timegm( dDate_tuple )
# 	if nTimes == 2:
# 		dDate_UTC3 = calendar.timegm( dDate_tuple )

# 	nTimes += 1


# Get the current date
dToday      = datetime.datetime.now()
# Cast current date format into Tuple
dDate_tuple = dToday.timetuple()
# Cast the Tuple format into UTC (seconds from January 1970)
dDate_UTC  = calendar.timegm( dDate_tuple )
# Nice source: http://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/



# sMessage = json.dumps( jMessage )


# PREPARE THE CALL'S PARAMETERS
sMessage = json.dumps({'arg':{
								'account'  : sAccount,
								'device'   : sDevice,
								'devToken' : sToken,
								'messType' : sMsgType,
								'proxy'    : sProxy,
								'messages' : [{
											'sensor'    : sSensor, 
											'value'     : iValue, 
											'timestamp' : dDate_UTC 
											},{
											'sensor'    : sSensor, 
											'value'     : iValue, 
											'timestamp' : dDate_UTC
											},{
											'sensor'    : sSensor, 
											'value'     : iValue, 
											'timestamp' : dDate_UTC
											}]
								}
						})

# Import the class: file -> class
from cl_Arduino import cl_Arduino
from cl_HanaIoT import cl_HanaIoT

# Instanciate the object
oArduino = cl_Arduino()
oHana    = cl_HanaIoT(sMessage)

# Call a method
# Open
oConn = oArduino.serialOpenConn(sPort, iBRate)
# Read
oArduino.serialReadJson(oConn)
print('\n')
oArduino.serialReadJson(oConn)
print('\n')
oArduino.serialReadJson(oConn)
print('\n')
oArduino.serialReadJson(oConn)
print('\n')
oArduino.serialReadJson(oConn)
# Close
oArduino.serialCloseConn(oConn)

# oHana.printMsg()
# oHana.sendMsg()