import urllib3
import certifi

# It is absolutely CRITICAL that you use certificate validation to ensure and guarantee that
# 1. you are indeed sending the message to *.hanatrial.ondemand.com and
# 2. that you avoid the possibility of TLS/SSL MITM attacks which would allow a malicious person to capture the OAuth token
# URLLIB3 DOES NOT VERIFY CERTIFICATES BY DEFAULT
# Therefore, install urllib3 and certifi and specify the PoolManager as below to enforce certificate check
# See https://urllib3.readthedocs.org/en/latest/security.html for more details

sDevice  = "9e8f52bf-281c-4fbc-9a34-9cd8e58710b5"
sToken   = "31479766523918bd1ef473b1d1a8b1a2"
sMsgType = "ba2434ef5c2b4bc8de83"

# use with or without proxy
http = urllib3.PoolManager(
	cert_reqs='CERT_REQUIRED', # Force certificate check.
	ca_certs=certifi.where(),  # Path to the Certifi bundle.
)
 
http = urllib3.proxy_from_url('http://proxy:8080')

# interaction for a specific Device instance - replace 'd000-e000-v000-i000-c000-e001' with your specific Device ID

# url = 'https://iotmms_on_your_trial_system.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/d000-e000-v000-i000-c000-e001' << todo
url = "https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/" + sDevice

headers = urllib3.util.make_headers()

# use with authentication
# please insert correct OAuth token
headers['Authorization'] = 'Bearer ' + sToken
headers['Content-Type'] = 'application/json;charset=utf-8'

# send message of Message Type 'm0t0y0p0e1' and the corresponding payload layout that you defined in the IoT Services Cockpit
body='{"mode":"async", "messageType":"' + sMsgType + '", "messages":[{"sensor":"python", "value":"98", "timestamp":1413191650}]}'

try:
	r = http.urlopen('POST', url, body=body, headers=headers)
	print("\n")
	print("[Status return] " + str(r.status))
	print("[Return msg   ] " + str(r.data))

except urllib3.exceptions.SSLError as e:
	print (e)