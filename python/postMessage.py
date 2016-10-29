# # -------------------------------------------
# # SCRIPT INTERFACE
# # -------------------------------------------
# # argv{
# # 	"account"	: "Edm.String",
# # 	"device"   	: "Edm.String",
# # 	"devToken" 	: "Edm.String",
# # 	"messType"	: "Edm.String",
# # 	"proxy"		: "Edm.String",
# # 	"messages"	:[{
# # 					"sensor"	:"Edm.String", 
# # 					"value" 	:"Edm.Int", 
# # 					"timestamp"	:"Edm.DateTime"
# # 				}]
# # 	}

# import urllib3
# import certifi
# import sys

# # It is absolutely CRITICAL that you use certificate validation to ensure and guarantee that
# # 1. you are indeed sending the message to *.hanatrial.ondemand.com and
# # 2. that you avoid the possibility of TLS/SSL MITM attacks which would allow a malicious person to capture the OAuth token
# # URLLIB3 DOES NOT VERIFY CERTIFICATES BY DEFAULT
# # Therefore, install urllib3 and certifi and specify the PoolManager as below to enforce certificate check
# # See https://urllib3.readthedocs.org/en/latest/security.html for more details

# # def main( sAccount, sDevice, sToken, sMsgType, sProxy ):
# def main( sMessage ):

# # sAccount = sys.argv[1]
# # sDevice  = sys.argv[2]
# # sToken   = sys.argv[3]
# # sMsgType = sys.argv[4]
# # sProxy   = sys.argv[5]

# # use with or without proxy
# 	http = urllib3.PoolManager(
# 		cert_reqs='CERT_REQUIRED', # Force certificate check.
# 		ca_certs=certifi.where(),  # Path to the Certifi bundle.
# 	)
	 
# 	if sProxy != '' :
# 		http = urllib3.proxy_from_url( sProxy )	

# 	url = 'https://iotmms'+ sAccount + '.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/' + sDevice

# 	headers = urllib3.util.make_headers()

# 	# use with authentication
# 	# please insert correct OAuth token
# 	headers['Authorization'] = 'Bearer ' + sToken
# 	headers['Content-Type'] = 'application/json;charset=utf-8'

# 	# send message of Message Type 'm0t0y0p0e1' and the corresponding payload layout that you defined in the IoT Services Cockpit
# 	body='{"mode":"async", "messageType":"' + sMsgType + '", "messages":[{"sensor":"python", "value":"95", "timestamp":1413191650}]}'

# 	try:
# 		r = http.urlopen('POST', url, body=body, headers=headers)
# 		print('\n')
# 		print('[Status return] ' + str(r.status))
# 		print('[Return msg   ] ' + str(r.data))

# 	except urllib3.exceptions.SSLError as e:
# 		print (e)