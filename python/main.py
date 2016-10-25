import sys
# import random
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

iBRate     = 9600

iSleep     = 3

# MAC OSX
sPort      = '/dev/cu.usbmodem411'

# Import the class: file -> class
from cl_Arduino  import cl_Arduino
from cl_HanaIoT  import cl_HanaIoT
from cl_TimeDate import cl_TimeDate

# Instanciate the object
oArduino = cl_Arduino()
# oHana    = cl_HanaIoT(sMessage)
oTimeDate = cl_TimeDate()

# Open
oConn = oArduino.serialOpenConn(sPort, iBRate)
iIndex = oTimeDate.timeUTC()
print('Index : ' + str(iIndex))


if oConn ==  None:
	print('[Coffee to Cloud] Unable to open the port')
else:
	while True:
		# Gets the current date and time UTC format
		dDate_UTC = oTimeDate.timeUTC()

		# Read Serial Port
		jMessage = oArduino.serialReadJson(oConn)

		# Add new info to the JSON 
		aMessage = json.loads(jMessage)
		aMessage[u'args'][0][u'messages'][0][u'timestamp'] = dDate_UTC
		aMessage[u'args'][0][u'index'] = iIndex

		jMessage = json.dumps(aMessage)

		print( jMessage )
		print('\n')
		# oHana.sendMsg()

		oTimeDate.delay( iSleep )
	# Close
	oArduino.serialCloseConn( oConn )
	