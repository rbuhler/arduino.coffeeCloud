import sys
sys.path.append('lib')

import random

import datetime
import calendar

# import postMessage

import json

# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
import cl_HanaIoT

# DEVICE IDENTIFICATION
sAccount = 'p1941020166trial'
sDevice  = '9e8f52bf-281c-4fbc-9a34-9cd8e58710b5'
sToken   = '31479766523918bd1ef473b1d1a8b1a2'
sMsgType = 'ba2434ef5c2b4bc8de83'
# sProxy   = 'http://proxy:8080'
sProxy   = ''
sSensor  = 'Python'

#RANDOM VALUE (pretend a real random reading)
iValue1 = random.randrange(0, 100)
iValue2 = random.randrange(0, 100)
iValue3 = random.randrange(0, 100)

# CURRENT DATE
nTimes = 0
while nTimes <= 2:
# Get the current date
	dToday      = datetime.datetime.now() + datetime.timedelta(seconds = 5 * nTimes)
# Cast current date format into Tuple
	dDate_tuple = dToday.timetuple()
# Cast the Tuple format into UTC (seconds from January 1970)
	if nTimes == 0:
		dDate_UTC1 = calendar.timegm( dDate_tuple )
	if nTimes == 1:
		dDate_UTC2 = calendar.timegm( dDate_tuple )
	if nTimes == 2:
		dDate_UTC3 = calendar.timegm( dDate_tuple )

	nTimes += 1

# dDate_UTC   = 0
# Nice source: http://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/

# PREPARE THE CALL'S PARAMETERS
sMessage = json.dumps({'arg':{
								'account'  : sAccount,
								'device'   : sDevice,
								'devToken' : sToken,
								'messType' : sMsgType,
								'proxy'    : sProxy,
								'messages' : [{
											'sensor'    : sSensor, 
											'value'     : iValue1, 
											'timestamp' : dDate_UTC1
											},{
											'sensor'    : sSensor, 
											'value'     : iValue2, 
											'timestamp' : dDate_UTC2
											},{
											'sensor'    : sSensor, 
											'value'     : iValue3, 
											'timestamp' : dDate_UTC3
											}]
								}
						})

from cl_HanaIoT import cl_HanaIoT
oHana = cl_HanaIoT(sMessage)
oHana.printMsg()

# oHana.sendMsg()
