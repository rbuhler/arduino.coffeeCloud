
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
import json

class cl_HanaIoT:
	'Common class for interacting with Hana IoT service'

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
		self.nMessages   = len(jMessage['arg']['messages'])
		self.aMessage = []

		nTimes = self.nMessages
		while nTimes > 0:
			nTimes -= 1
			self.aMessage.insert(nTimes, jMessage['arg']['messages'][nTimes])

# Print message in the console
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def writeDown(self):
		print('\n')
		print('NUmber of messages: ' + str(self.nMessages))
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

# Post the message to the IoT service
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	# def send_msg():

	# # use with or without proxy
	# http = urllib3.PoolManager(
	# 	cert_reqs='CERT_REQUIRED', # Force certificate check.
	# 	ca_certs=certifi.where(),  # Path to the Certifi bundle.
	# )
	 
	# if self.sProxy != '' :
	# 	http = urllib3.proxy_from_url( self.sProxy )	

	# url = 'https://iotmms'+ self.sAccount + '.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/' + self.sDevice

	# headers = urllib3.util.make_headers()

	# # use with authentication
	# # please insert correct OAuth token
	# headers['Authorization'] = 'Bearer ' + self.sToken
	# headers['Content-Type'] = 'application/json;charset=utf-8'

	# # send message of Message Type 'm0t0y0p0e1' and the corresponding payload layout that you defined in the IoT Services Cockpit
	# aBody_mode     = '"mode":"async"'
	# aBody_msgType  = 'messageType":"' + self.sMsgType
	# aBody_messages = 
	
	# # BEGIN LOOP
	# 	aMessages = '{'+'"sensor": '+''+'"value": '+'"timestamp" :'+'},'
	# # END LOOP
	
	# aBody_messages = '"messages":[' + aMessages + ']'



	# aBody = '{' + aBody_mode + ',' + aBody_msgType + ',' + aBody_messages + '}'


	# body='{"mode":"async", "messageType":"' + self.sMsgType + '", "messages":[{"sensor":"python", "value":"95", "timestamp":1413191650}]}'

	# try:
	# 	r = http.urlopen('POST', url, body=body, headers=headers)
	# 	print('\n')
	# 	print('[Status return] ' + str(r.status))
	# 	print('[Return msg   ] ' + str(r.data))

	# except urllib3.exceptions.SSLError as e:
	# 	print (e)