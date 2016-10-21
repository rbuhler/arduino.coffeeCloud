
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
import urllib3
import certifi

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
	def printMsg(self):
		print('\n')
		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
		print ('Account  : ' + self.sAccount)
		print ('Device   : ' + self.sDevice)
		print ('Token    : ' + self.sToken)
		print ('Msg.Type : ' + self.sMsgType)
		print ('Proxy    : ' + self.sProxy)

		nCount = 0
		while nCount < self.nMessages:		
			print ('+ Message ' + str(nCount + 1) )
			print ('\t' + 'Sensor    : ' + self.aMessage[nCount]['sensor'])
			print ('\t' + 'Value     : ' + str(self.aMessage[nCount]['value']))
			print ('\t' + 'TimeStamp : ' + str(self.aMessage[nCount]['timestamp']))
			nCount += 1

		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
		print('\n')

# Post the message to the IoT service
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def sendMsg(self):

		# use with or without proxy
		http = urllib3.PoolManager(
			cert_reqs='CERT_REQUIRED', # Force certificate check.
			ca_certs=certifi.where(),  # Path to the Certifi bundle.
		)	 
		# set the proxy when applicable
		if self.sProxy != '' :
			http = urllib3.proxy_from_url( self.sProxy )	

		# URL preparation
		url = 'https://iotmms'+ self.sAccount + '.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/' + self.sDevice
		print('URL : ' + url)


		# HEADERS preparation
		aHeader = urllib3.util.make_headers()
		# use with authentication
		aHeader['Authorization'] = 'Bearer ' + self.sToken
		aHeader['Content-Type'] = 'application/json;charset=utf-8'
		
		# BODY preparation
		aBody_mode     = '"mode":"async"'
		aBody_msgType  = '"messageType":"' + self.sMsgType + '"'
			
		aBody_messages = '"messages":['
		nCount = 0
		while nCount < self.nMessages:
			sLine = '{'
			sLine = sLine + '"sensor":' + '"' + (self.aMessage[nCount]['sensor'] + '"' + ', ')
			sLine = sLine + '"value":' + str(self.aMessage[nCount]['value']) + ', '
			sLine = sLine + '"timestamp":' + str(self.aMessage[nCount]['timestamp'])

			if nCount + 1  != self.nMessages:
				sLine = sLine + '},'
			if nCount + 1 == self.nMessages:
				sLine = sLine + '}'

			aBody_messages = aBody_messages + sLine
			nCount += 1

		aBody_messages = aBody_messages + ']'

		aBody = '{' + aBody_mode + ', ' + aBody_msgType + ', ' + aBody_messages + '}'
		print('Body : ' + aBody)
		print('\n')

		try:
			r = http.urlopen('POST', url, body=aBody, headers=aHeader)
			print('\n')
			print('[Status return] ' + str(r.status))
			print('[Return msg   ] ' + str(r.data))

		except urllib3.exceptions.SSLError as e:
			print (e)