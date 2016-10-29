# arduino.buhler.coffeeCloud

![FromCoffeeToCloud](https://github.com/rbuhler/arduino.buhler.coffeeCloud/blob/master/%20pictures/coffeeBanner.jpeg)

## From Coffee to Cloud 
 <div style="text-align: justify;">

The project _From Coffee to Cloud_ aims at presenting an example of implementing Internet of Things (IoT) in a quick and easy way. 

### Use Case
The use case is the monitoring of a coffee machine where a luminosity sensor keeps reading the **ready light** until it gets on, meaning coffee ready to be served. This way its status can be monitored remotely by the interested users (coffee addicted).

For such an application it makes necessary the join of front end and backend software development together with an integration with hardware for collecting data from the _external world_. In a try to bring to this example more simplicity it was chosen the support of SAP cloud environment, the programming language Python and Arduino hardware compatible.

### Hana Cloud Platform
Making use of the Hana Cloud infrastructure, more preciselly the Internet of Things (IoT) Service, it will be prepared an environment to receive and share data collected from a device.
- [SAP Hana Cloud Platform Cockpit](https://account.hanatrial.ondemand.com)
- [Help - SAP HANA Cloud Platform Internet of Things Services](https://help.hana.ondemand.com/iot/frameset.htm?ad829c660e584c329200022332f04d00.html)
- [Youtube - Internet of Things (IoT) Services](https://www.youtube.com/playlist?list=PLkzo92owKnVxzjoxwJdaa400E_UqkzE8J)

### Arduino
For the task of colleting data it will be used an Arduino board connected to a luminosity sensor. 
- [Arduino](https://www.arduino.cc/)

### Python
The reading is sent via serial port to a auxiliar device that's listening such port. The data is packed and sent to the cloud infrastructure.
- [Python Software Foundation](https://www.python.org/)
- [Python Object Oriented](https://www.tutorialspoint.com/python/pdf/python_classes_objects.pdf)
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Switch Statement](https://pypi.python.org/pypi/switch/1.1.0)
- [OS_flavor_name_version](https://github.com/hpcugent/easybuild/wiki/OS_flavor_name_version)
 </div>

## Hands On
 <div style="text-align: justify;">
In order to handle the data collected by the hardware an infrastructure shall be prepared. For such job Hana CLoud Platforma provides the Internet of Things Service that makes the service way easer.

The support proposed implementation follows what is described next:

### Internet of Things Services

![IoTHana](https://github.com/rbuhler/arduino.buhler.coffeeCloud/blob/master/%20pictures/IoThana.png) 

- Form the **SAP HANA Cloud Platform Cockpit** root;
- Left Panel:
 - Choose **Services**;
 - Enable **Internet of Things**;
 - Choose **Go to Service**.
 </div>
 
 <div style="text-align: justify;">
### Data Base
In order to create a new binding for the IoT service tables into the Hana XS infrastructure it makes necessay a little customizing.

**SAP HANA Cloud Platform Cockpit**
- Form the **SAP HANA Cloud Platform Cockpit** root;
- Left Panel:
 - **Persistance**;
 - **Database & Schemas**;
 - Pushbutton **New**;
 - Inform a **Database ID**;
 - Choose **Database System:** HANA MDC;
 - Enter **Password**;
 - Repeat **Password**;
 _(notice that the user is SYSTEM)_
 - Choose **Save**.

- Form the **SAP HANA Cloud Platform Cockpit** root;
- Left Panel:
 - **Applications**;
 - **Java Applications**;
 - Choose the IoT application;
 - **Configuration**;
 - **Data Source Bindings**;
 - Delete the current binding;
 - Choose **New Binding**;
 - Enter a **Data Source**;
 - Choose **DB/Schema ID**;
 - Enter **Database User :** SYSTEM;
 - Enter **Password**;
 - Choose **Save**.
 
- Form the **SAP HANA Cloud Platform Cockpit** root;
- Left Panel:
 - **Applications**;
 - **Java Applications**;
 - Choose the IoT application;
 - Choose **Overview**;
 - Choose **Stop** pushbutton;
 - Choose **Start** pushbutton.
 
</div>

### Arduino
![Arduino and Luminisity Sensor](https://github.com/rbuhler/arduino.buhler.coffeeCloud/blob/master/%20pictures/arduinoLuminisity.jpg)

[Sketch](https://github.com/rbuhler/arduino.buhler.coffeeCloud/blob/master/arduino/luminositySensor/luminositySensor.ino)

[Library ArduinoJson](https://github.com/bblanchon/ArduinoJson)

**JSON**
````
args:[{
	account,
	device,
	devToken,
	messType,
	proxy,
	messages : [{ 
			index, 
			sensor, 
			timestamp, 
			value, 
			user
		}]
	}]
````

### Python
[Python - From Coffee to Cloud](https://github.com/rbuhler/arduino.buhler.coffeeCloud/tree/master/python)

**Algorithm**
````
BEGIN
	read port
	if read is FALSE
		print "Error message"
	
	else
		create JSON_Header
		HTTPpost JSON_Header
		loop
			read port
			adjust JSON_Message
			HTTPPost JSON_Message
			delay 3
		endloop
		
	endif
	
END
````

### Real World

#### Observation Tower 
![Observation Tower](https://github.com/rbuhler/arduino.buhler.coffeeCloud/blob/master/%20pictures/observationTower.jpg)

#### Cofee Machine
![Coffee Machine](https://github.com/rbuhler/arduino.buhler.coffeeCloud/blob/master/%20pictures/coffeeMachine.jpg)

## More Info and Supporting Tools

### Source of information
- [SAP GitHub - Open Source & SAP](http://sap.github.io/index.html?sort=asc&filter=featured)
- [Open UI5](http://openui5.org/)

### Google Chrome add-on Postman
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

Rodrigo Bühler
