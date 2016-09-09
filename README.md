# arduino.buhler.coffeeCloud
The main idea here is to present an implementation of an IoT project.
**The problem**
Monitor the "ready light" of a coffee machine and advise the user whenever the coffee is ready.
**The solution**
An Arduino UNO connected to a luminosity sensor checks for the "ready light" to turn on (meaning time for coffee).
From time to time the coffee machine status is sent to the cloud and from there the user can check such status in a UI5 web page.

## SAP HANA
### SAP HANA Cloud Documentation and References
**Youtube**
>[Internet of Things (IoT) Services](https://www.youtube.com/playlist?list=PLkzo92owKnVxzjoxwJdaa400E_UqkzE8J)
>>[SAP HANA Academy - IoT Services: Getting Started [2.2.1]](https://youtu.be/EiIInSB8pFk)
>>[SAP HANA Academy - IoT Services: Using MMS - Send [2.2.1]](https://youtu.be/buB6H62UAd0?list=PLkzo92owKnVxzjoxwJdaa400E_UqkzE8J)

**SAP Hep**
https://help.hana.ondemand.com/iot/frameset.htm?ad829c660e584c329200022332f04d00.html

**Open Source & SAP**
http://sap.github.io/index.html?sort=asc&filter=featured

### SAP Hana Trial
https://account.hanatrial.ondemand.com
#### Internet of Things Services
**Message Type**
_luminositySensor_
**ID:** ba2434ef5c2b4bc8de83

**Device Type**
_arduino_
**ID:** 896f81d5a9f94374f154
**Device Registration Token:** 66bf280b7b66e6239f0ddd782d4e2ee

**Device**
_uno_
**Token:** 15ece4ba7d4b2f537c7eb6435db4fdf
**ID:** c15203e5-9530-4b8c-be0f-ee6b9f024496

**Deploy the Message Management Service**
**Host:** https://hanatrial.ondemand.com
**Account ID:** p1941020166trial
**User Name:** P1941020166

**HTTP API**

**End Point:** https://iotmmsp1941020166trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/c15203e5-9530-4b8c-be0f-ee6b9f024496

**Message:**
```
{
    "mode":"sync",
    "messageType":"ba2434ef5c2b4bc8de83",
    "messages":[
        {
            "sensor":"sensor1",
            "value":"20",
            "timestamp":1473460985
        }
    ]
}
```

## NODE JS
* [Arduino and NodeJS Communication With Serial Ports](http://danialk.github.io/blog/2014/04/12/arduino-and-nodejs-communication-with-serial-ports/)