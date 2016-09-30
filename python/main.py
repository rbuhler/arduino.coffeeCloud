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
sProxy   = 'http://proxy:8080'
sSensor  = 'Python'

#RANDOM VALUE (pretend a real random reading)
iValue = random.randrange(0, 100)

# CURRENT DATE
# Get the current date
dToday      = datetime.datetime.now()
# Cast current date format into Tuple
dDate_tuple = dToday.timetuple()
# Cast the Tuple format into UTC (seconds from January 1970)
dDate_UTC   = calendar.timegm( dDate_tuple )
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
											'value'     : iValue, 
											'timestamp' : dDate_UTC
											},{
											'sensor'    : sSensor, 
											'value'     : iValue, 
											'timestamp' : dDate_UTC
											}]
								}
						})
				# )

from cl_HanaIoT import cl_HanaIoT
oHana = cl_HanaIoT(sMessage)
oHana.writeDown()