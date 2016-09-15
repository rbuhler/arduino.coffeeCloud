#"messages":[{"sensor":"python", "value":"95", "timestamp":1413191650}]}'

import json

# String JSON
# sMessage = json.dumps(['msg',{'sensor':"python", 'value':94, 'timestamp':1413191650}])
sMessage = json.dumps({'message':[{'sensor':"python", 'value':94, 'timestamp':1413191650}, {'sensor':"python", 'value':93, 'timestamp':1413191650}]})

print (json.dumps(sMessage))
print('\n')

#JSON object
jMessage = json.loads(sMessage)
print(json.dumps(jMessage))
print('\n')

print('Depth : ' + str(len(jMessage['message'])))
print('\n')

print(jMessage['message'][0]['sensor'])
print('\n')

print(jMessage['message'][1]['value'])