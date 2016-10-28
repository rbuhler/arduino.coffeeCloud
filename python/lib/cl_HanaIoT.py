
import json
import urllib3
import certifi

class cl_HanaIoT:
	'Common class for interacting with Hana IoT service'

# Print message in the console
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def printMsg(self, json_msg):
		aJson = json.loads(json_msg)

		sAccount  = aJson[u'args'][0][u'account']
		sDevice   = aJson[u'args'][0][u'device']
		sToken    = aJson[u'args'][0][u'devToken']
		sMsgType  = aJson[u'args'][0][u'messType']
		sProxy    = aJson[u'args'][0][u'proxy']

		aMessages = aJson[u'args'][0][u'messages'][0]
		jMessages = json.dumps(aMessages)

		print('\n')
		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
		print ('Account  : ' + sAccount)
		print ('Device   : ' + sDevice)
		print ('Token    : ' + sToken)
		print ('Msg.Type : ' + sMsgType)
		print ('Proxy    : ' + sProxy)

		print('\n')
		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')

		print (jMessages)

		print ('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
		print('\n')

# Post the message to the IoT service
# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
	def sendMsg(self, json_msg):

		aJson = json.loads(json_msg)

		sAccount  = aJson[u'args'][0][u'account']
		sDevice   = aJson[u'args'][0][u'device']
		sToken    = aJson[u'args'][0][u'devToken']
		sMsgType  = aJson[u'args'][0][u'messType']
		sProxy    = aJson[u'args'][0][u'proxy']

		aMessages = aJson[u'args'][0][u'messages'][0]
		jMessages = json.dumps(aMessages)

		# use with or without proxy
		http = urllib3.PoolManager(
			cert_reqs='CERT_REQUIRED', # Force certificate check.
			ca_certs=certifi.where(),  # Path to the Certifi bundle.
		)	 
		# set the proxy when applicable
		if sProxy != '' :
			http = urllib3.proxy_from_url( sProxy )	

		print('-------------------- \n')
		# URL preparation
		url = 'https://iotmms'+ sAccount + '.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/' + sDevice
		print('URL : ' + url)
		print('\n')

		# HEADERS preparation
		aHeader = urllib3.util.make_headers()
		# use with authentication
		aHeader['Authorization'] = 'Bearer ' + sToken
		aHeader['Content-Type'] = 'application/json;charset=utf-8'
		
		# BODY preparation
		aBody_mode     = '"mode":"async"'
		aBody_msgType  = '"messageType":"' + sMsgType + '"'
			
		aBody_messages = '"messages" : [' + jMessages + ']'

		aBody = '{' + aBody_mode + ', ' + aBody_msgType + ', ' + aBody_messages + '}'
		print('Body : ' + aBody)
		print('\n')

		print('-------------------- \n')
		try:
			r = http.urlopen('POST', url, body=aBody, headers=aHeader)
			print('\n')
			print('[Status return] ' + str(r.status))
			print('[Return msg   ] ' + str(r.data))

		except urllib3.exceptions.SSLError as e:
			print (e)