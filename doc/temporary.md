# Technical Details

## Login

**USER**

1. ID: P1941020166

2. ACCOUNT: p1941020166trial

## Quick access
[Internet of Things Services Cockpit]
(https://iotcockpitiotservices-p1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.cockpit/)

[Message Management Service Cockpit]
(https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/)

## IoT Service
| Key | Data| Obs |
|-----|-----|-----| 
| sAccount    | "p1941020166trial" | |
| sDevice     | "1e4d608a-01c9-4060-b7b3-71e4b91e31a8"   | Arduino |
| sToken      | "1a81e19d91978bddfbeb3a6a3d45e25"        | |
| sMsgType    | "56a55910fd4abd99f088"                   | sensorLuminosity |
| sMsgType    | "7cfead179919a98cbed9"                   | sensorHeader |
| sDeviceType | "686c2b88de3953d81948"                   | coffeeMachine | 
| OAuth       | "3c5139d3f08e7bbf7ece190fbd7a26a"        | |

## OData sintax

**Metadata**

https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/$metadata

**DATA**

https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_56A55910FD4ABD99F088

**TOP**

https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_56A55910FD4ABD99F088?$top=1

**JSON**

https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_56A55910FD4ABD99F088?$top=1&$format=json

## Postman Rest Client
0. Enter the device ID at the end of the URL;
1. Authorization: OAuth2;
2. Headers: 
*	Authorization - Bearer 2946c09c57262d7ea9331dfddb2ead
*	Content Type - application/json
3. Change from Get to Post;
4. Body:
````
{
        "mode":"sync",
        "messageType":"ba2434ef5c2b4bc8de83",
        "messages":[
            {
                "sensor":"sensor1",
                "value":"20",
                "timestamp":1413191650
            	
            }
        ]
}
````
5. Click Send.
