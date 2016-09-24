# arduino.buhler.coffeeCloud
The main idea here is to present an implementation of an IoT project.

**The problem**
Monitor the "ready light" of a coffee machine and advise the user when the coffee is ready.

**The solution**
An Arduino UNO connected to a luminosity sensor checks for the "ready light" to turn on (meaning time for coffee).
From time to time the coffee machine status is sent to the cloud and from there the user can check such status in a UI5 web page.

## SAP HANA
### SAP HANA Cloud Documentation and References

[Youtube - Internet of Things (IoT) Services](https://www.youtube.com/playlist?list=PLkzo92owKnVxzjoxwJdaa400E_UqkzE8J)

[Help - SAP HANA Cloud Platform Internet of Things Services](https://help.hana.ondemand.com/iot/frameset.htm?ad829c660e584c329200022332f04d00.html)

[SAP GitHub - Open Source & SAP](http://sap.github.io/index.html?sort=asc&filter=featured)

### SAP Hana Trial
https://account.hanatrial.ondemand.com

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
6. Click Send.____

## Python
[Python Software Foundation](https://www.python.org/)
[Python Object Oriented](https://www.tutorialspoint.com/python/pdf/python_classes_objects.pdf)

## NODE JS
* [Arduino and NodeJS Communication With Serial Ports](http://danialk.github.io/blog/2014/04/12/arduino-and-nodejs-communication-with-serial-ports/)