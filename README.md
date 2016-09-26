# arduino.buhler.coffeeCloud

<div style="text-align: justify;">
The project _From Cofee to Cloud_ aims at presenting an example of implementing Internet of Things (IoT) in a quick and easy way. 

The use case is the monitoring of a cofee machine where a luminosity sensor keeps reading the **ready light** until it gets on, meaning cofee ready to be served. This way its status can be monitored remotelly and send an alert to the interested users (cofee addicteds).

For such an application it will make necessary the join of frontend and backend software development toghether with an integration with hardware for collecting data from the _external world_. In a try to bring to this example more simplicity it was choosen the support of SAP cloud environment, the programming language Python and Arduino hardware compatible.

Making use of the Hana Cloud infrastructure, more preciselly the Internet of Things (IoT) Service, it will be prepared an environment to receive and share data collected from a device.

For the task of colleting data it will be used an Arduino board connected to a luminosity sensor. The reading is sent via serial port to a auxiliar device that's listening such port. The data is packed and sent to the cloud infrastructure.

In the other side it makes necessary to provide a interface the final user may have access with the data collected and interact with. 

The choosen technology for that is HTML5 with the use of Open UI5 library for better results.

</div>


## SAP Hana Cloud Platform
[SAP Hana Cloud Platform Cockpit](https://account.hanatrial.ondemand.com)
## Hana IoT Services

## HTML5/UI5
[Open UI5](http://openui5.org/)

### Source of information
[Youtube - Internet of Things (IoT) Services](https://www.youtube.com/playlist?list=PLkzo92owKnVxzjoxwJdaa400E_UqkzE8J)
[Help - SAP HANA Cloud Platform Internet of Things Services](https://help.hana.ondemand.com/iot/frameset.htm?ad829c660e584c329200022332f04d00.html)
[SAP GitHub - Open Source & SAP](http://sap.github.io/index.html?sort=asc&filter=featured)

## Draft
The main idea here is to present an implementation of an IoT project.
**The problem**
Monitor the "ready light" of a coffee machine and advise the user when the coffee is ready.
**The solution**
An Arduino UNO connected to a luminosity sensor checks for the "ready light" to turn on (meaning time for coffee).
From time to time the coffee machine status is sent to the cloud and from there the user can check such status in a UI5 web page.

#### Internet of Things Services
Atrribute        | Value
-----------------|
Message Type     | _luminositySensor_ 
Device Type      | _arduino_
Device           | _uno_ 

## Google Chrome add-on Postman
[Chrome Web Store](https://www.google.com.br/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&sqi=2&ved=0ahUKEwiH-ejl9YrPAhXLIpAKHWpVDBkQFggoMAA&url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fpostman%2Ffhbjgbiflinjbdggehcddcbncdddomop%3Fhl%3Den&usg=AFQjCNE_Yq59TT1ZExzJ68FTldg4ho_lGw&sig2=s2A-KDOCEgGroyvXH0nKHA&bvm=bv.132479545,d.Y2I)
**Postman Rest Client**
1. Enter the device ID at the end of the URL; _(Send and receive messages through HTTP)_
2. Authorization: OAuth2;
3. Headers: 
*   Authorization - Bearer **<Device Token>**
*   Content Type - application/json
4. Change from Get to Post;
5. Body:
````
{
        "mode":"sync",
        "messageType":"<Message ID>",
        "messages":[
            {
                "sensor":"sensor1",
                "value":"20",
                "timestamp":1413191650   
            }
        ]
}
````
6. Click Send.

## Python
[Python Software Foundation](https://www.python.org/)
[Python Object Oriented](https://www.tutorialspoint.com/python/pdf/python_classes_objects.pdf)

## NODE JS
* [Arduino and NodeJS Communication With Serial Ports](http://danialk.github.io/blog/2014/04/12/arduino-and-nodejs-communication-with-serial-ports/)