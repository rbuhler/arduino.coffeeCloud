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

## IoT Service (rodrigo.buhler@ymail.com)
| Key | Data| Obs |
|-----|-----|-----| 
| sAccount    | "p1941020166trial" | |
| sDevice     | "1e4d608a-01c9-4060-b7b3-71e4b91e31a8"   | Arduino |
| sToken      | "1a81e19d91978bddfbeb3a6a3d45e25"        | |
| sMsgType    | "56a55910fd4abd99f088"                   | sensorLuminosity |
| sMsgType    | "7cfead179919a98cbed9"                   | sensorHeader |
| sDeviceType | "686c2b88de3953d81948"                   | coffeeMachine | 
| OAuth       | "3c5139d3f08e7bbf7ece190fbd7a26a"        | |

## IoT Service (share.buhler@gmail.com)
| Key | Data| Obs |
|-----|-----|-----| 
| sAccount    | "p1942282297trial"                       | |
| sDevice     | "4fd19277-4cfe-4377-9d00-dd5ca8740a44"   | Arduino |
| sToken      | "2d879287145519929e12402e378660"         | |
| sMsgType    | "70e9ae6a70c545c342e8"                   | sensorLuminosity |
| sMsgType    | "a1f391674bec8ba68277"                   | sensorHeader |
| sDeviceType | "67ef61393837bb7e700b"                   | coffeeMachine | 
| OAuth       | "d4a2926a993d4bada63df11fbc4e3ee"

[IoT Cockpit](https://iotcockpitiotservices-p1942282297trial.hanatrial.ondemand.com/com.sap.iotservices.cockpit)

[Messages Cockpit](https://iotmmsp1942282297trial.hanatrial.ondemand.com/com.sap.iotservices.mms/)

## OData sintax

**Metadata**

https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/$metadata
### HEADER
1. COMPLETE LIST
https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_7CFEAD179919A98CBED9?$format=json

2. FILTER BY DATE
https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_7CFEAD179919A98CBED9?$filter=C_DATE%20eq%20%2728/10/2016%27&$format=json


### READINGS
1. COMPLETE LIST
https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_56A55910FD4ABD99F088?$select=C_INDEX&$format=json

2. FILTER BY INDEX
https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/app.svc/NEO_1PI6OECY8GIGSO4N81ITA138M.T_IOT_56A55910FD4ABD99F088?$filter=C_INDEX%20eq%201477617795&$format=json

### Source:
https://msdn.microsoft.com/en-us/library/gg309461(v=crm.7).aspx#BKMK_filter

http://www.odata.org/documentation/odata-version-2-0/uri-conventions/

https://www.asp.net/web-api/overview/odata-support-in-aspnet-web-api/using-select-expand-and-value

http://go.sap.com/developer/tutorials/iot-part10-hcp-services-hanaxs.html

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
