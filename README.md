# arduino.buhler.coffeeCloud
The main idea here is to present an implementation of an IoT project.
**The problem**
Monitor the "ready light" of a coffee machine and advise the user whenever the coffee is ready.
**The solution**
An Arduino UNO connected to a luminosity sensor checks for the "ready light" to turn on (meaning time for coffee).
From time to time the coffee machine status is sent to the cloud and from there the user can check such status in a UI5 web page.

## SAP HANA
### SAP Hana Trial
https://account.hanatrial.ondemand.com

### SAP HANA Cloud Documentation
#### SAP HANA Cloud Platform Internet of Things Services
https://help.hana.ondemand.com/iot/frameset.htm?ad829c660e584c329200022332f04d00.html

#### Internet of Things Services
**Message**
_readyLight_
**ID:** 75b60827bafbff23e216

**Device Type**
_luminositySensor_
**ID:** c58066b6aa56063ac0b4
**Device Registration Token:** 13d88b9f91293cfa9590d53e36bb55

**Device**
_arduinoUnoLuminositySensor_
**Token:** fee5a590a457cdf81848a331750498b
**ID:** f73d52ec-2e89-4db0-8ed2-74011788c7f1

**Deploy the Message Management Service**
**Host:** https://hanatrial.ondemand.com
**Account ID:** p1941020166trial
**User Name:** P1941020166

## NODE JS
_Arduino and NodeJS Communication With Serial Ports_
http://danialk.github.io/blog/2014/04/12/arduino-and-nodejs-communication-with-serial-ports/