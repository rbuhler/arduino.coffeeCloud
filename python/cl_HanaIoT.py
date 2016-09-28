import random

import datetime
import calendar

import postMessage

import json

class HanaIoT:
	'Common class for interacting with Hana IoT service'

# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Class Constructor
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def __init__(self, json_msg):

	#JSON object
		jMessage = json.loads(json_msg)

		self.sAccount    = jMessage['arg']['account']
		self.sDevice     = jMessage['arg']['device']
		self.sToken      = jMessage['arg']['devToken']
		self.sMsgType    = jMessage['arg']['messType']
		self.sProxy      = jMessage['arg']['proxy']
		# Loop at the messages
		nTimes      = len(jMessage['arg']['messages'])

		self.aMessage = []
		while nTimes > 0:
			nTimes -= 1
			self.aMessage.insert(nTimes, jMessage['arg']['messages'][nTimes])

# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# JSON description
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# arg{
# 	"account"	: "Edm.String",
# 	"device"   	: "Edm.String",
# 	"devToken" 	: "Edm.String",
# 	"messType"	: "Edm.String",
# 	"proxy"		: "Edm.String",
# 	"messages"	:[{
# 					"sensor"	:"Edm.String", 
# 					"value" 	:"Edm.Int", 
# 					"timestamp"	:"Edm.DateTime"
# 				}]
# 	}
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
# Print message in the console
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def writeDown(self):

		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
		print ('Account  : ' + self.sAccount)
		print ('Device   : ' + self.sDevice)
		print ('Token    : ' + self.sToken)
		print ('Msg.Type : ' + self.sMsgType)
		print ('Proxy    : ' + self.sProxy)
		print ('Message.Sensor    : ' + self.aMessage[0]['sensor'])
		print ('Message.Value     : ' + str(self.aMessage[0]['value']))
		print ('Message.TimeStamp : ' + str(self.aMessage[0]['timestamp']))
		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
		print('\n')


# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*

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
# oHana = HanaIoT( json.dumps({'arg':{
								'account'  : sAccount,
								'device'   : sDevice,
								'devToken' : sToken,
								'messType' : sMsgType,
								'proxy'    : sProxy,
								'messages' : [{
											'sensor'    : sSensor, 
											'value'     : iValue, 
											'timestamp' : dDate_UTC
											}]
								}
						})
				# )

oHana = HanaIoT(sMessage)
oHana.writeDown()

# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
#
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	# def send_msg(json_msg):

	# # use with or without proxy
	# http = urllib3.PoolManager(
	# 	cert_reqs='CERT_REQUIRED', # Force certificate check.
	# 	ca_certs=certifi.where(),  # Path to the Certifi bundle.
	# )
	 
	# if sProxy != '' :
	# 	http = urllib3.proxy_from_url( sProxy )	

	# url = 'https://iotmms'+ sAccount + '.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/' + sDevice

	# headers = urllib3.util.make_headers()

	# # use with authentication
	# # please insert correct OAuth token
	# headers['Authorization'] = 'Bearer ' + sToken
	# headers['Content-Type'] = 'application/json;charset=utf-8'

	# # send message of Message Type 'm0t0y0p0e1' and the corresponding payload layout that you defined in the IoT Services Cockpit
	# body='{"mode":"async", "messageType":"' + sMsgType + '", "messages":[{"sensor":"python", "value":"95", "timestamp":1413191650}]}'

	# try:
	# 	r = http.urlopen('POST', url, body=body, headers=headers)
	# 	print('\n')
	# 	print('[Status return] ' + str(r.status))
	# 	print('[Return msg   ] ' + str(r.data))

	# except urllib3.exceptions.SSLError as e:
	# 	print (e)