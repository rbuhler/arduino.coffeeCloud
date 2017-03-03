import sys
# import random
import json

sys.path.append('./lib')

# DEVICE IDENTIFICATION
sAccount   = ''
sDevice    = ''
sToken     = ''
sMsgType   = ''
sProxy     = '' #'http://proxy:8080'

sSensor    = ''
iValue     = 0
iTimeStamp = 0

iSleep     = 3

# Import the class: file -> class
from cl_Arduino  import cl_Arduino
from cl_HanaIoT  import cl_HanaIoT
from cl_TimeDate import cl_TimeDate

# Instanciate the object
oArduino  = cl_Arduino()
oHana     = cl_HanaIoT()
oTimeDate = cl_TimeDate()

# ---------------------------------------------------
# Set the JSON
jMessage = json.dumps({'args':{
    'index':"index_val", 
    'sensor':123, 
    'timestamp':123456, 
    'message':[{
        'sensor':"python", 
        'value':94, 
        'timestamp':1413191650}]
}})
# Add new info to the JSON 
aMessage = json.loads(jMessage)
# ---------------------------------------------------

# Header message
sMsgTypeHeader = 'a1f391674bec8ba68277'
# Message Data
iIndex  = oTimeDate.getUTC()
sSensor = aMessage[u'args'][0][u'messages'][0][u'sensor']
dDate   = oTimeDate.getDate()
tTime   = oTimeDate.getTime()

jMessage = json.dumps({
	'args'     :[{
	'account'  : aMessage[u'args'][0][u'account'],
	'device'   : aMessage[u'args'][0][u'device'],
	'devToken' : aMessage[u'args'][0][u'devToken'],
	'messType' : sMsgTypeHeader,
	'proxy'    : aMessage[u'args'][0][u'proxy'],
	'messages' :[{'index':iIndex, 'sensor':sSensor, 'date':dDate, 'time':tTime }]
	}]
})

# jMessage = json.dumps(aHeaderMessage)

print( jMessage )
print('\n')
# Send Header
# oHana.printMsg(jMessage)
oHana.sendMsg(jMessage)

while True:
	# Gets the current date and time UTC format
	dDate_UTC = oTimeDate.getUTC()

# 	# Read Serial Port
# 	jMessage = oArduino.serialReadJson(oConn)
# 	# Add new info to the JSON 
# 	aMessage = json.loads(jMessage)

# ---------------------------------------------------
	# Set the JSON
    jMessage = json.dumps({'args':{
        'index':"index_val", 
        'sensor':123, 
        'timestamp':123456, 
        'message':[{
            'sensor':"python", 
            'value':94, 
            'timestamp':1413191650}]
    }})
	# Add new info to the JSON 
	aMessage = json.loads(jMessage)
# ---------------------------------------------------

 	aMessage[u'args'][0][u'messages'][0][u'index']     = iIndex
 	aMessage[u'args'][0][u'messages'][0][u'timestamp'] = dDate_UTC

	jMessage = json.dumps(aMessage)

	print( jMessage )
	print('\n')
	# Send Message
	# oHana.printMsg(jMessage)
	oHana.sendMsg(jMessage)

	oTimeDate.delay( iSleep )
# Close
oArduino.serialCloseConn( oConn )
