#include <Time.h>
#include <ArduinoJson.h>

// Hardware Config
int nLumiSensor=0;    //pin 0 : Luminosity sensor

int nGreenLED=8;    //digital pin  8 : GrenLED
int nYellowLED=9;   //digital pin  9 : YellowLED
int nRedLED=10;     //digital pin 13 : RedLED

int nAnalogRead;    //analog buffer

// JSON header message
String sAccount;
String sDevice;
String sToken;
String sMsgType;
String sProxy;
int sUser;
// JSON body message
String sSensorId;
int nRead;
int dTimestamp;

void setup()
{
Serial.begin(9600); //serial port speed : 9600bps(baud).

  pinMode(nGreenLED, OUTPUT);    //pin setup as digital output
  pinMode(nYellowLED, OUTPUT);   //pin setup as digital output
  pinMode(nRedLED, OUTPUT);      //pin setup as digital output
 
  digitalWrite(nGreenLED, LOW);  //LED switched off
  digitalWrite(nYellowLED, LOW); //LED switched off
  digitalWrite(nRedLED, LOW);    //LED switched off

  sAccount  = "p1941020166trial";
  sDevice   = "9e8f52bf-281c-4fbc-9a34-9cd8e58710b5";
  sToken    = "31479766523918bd1ef473b1d1a8b1a2";
  sMsgType  = "ba2434ef5c2b4bc8de83";
  sProxy    = "";
  sUser     = 0x0;

  sSensorId = "ArdoLumy";
  nRead        = 0;
  dTimestamp   = 0;
 
}

void loop()
{
 /*
 In order to convert the data read from the analog tension module 
 connected to the Arduino it makes necessary a little calculation procedure.
 
 The value range read from the module varies from 0 up to 1023, this
 way dividing by 5 we have intervals of 0v to 5v (volts).
 
 */
 nAnalogRead = analogRead(nLumiSensor);   // Reads the Luminosity sensor
 nRead = map(nAnalogRead, 0, 1023, 0, 5); // Calculates the intervals

// Step 1: Reserve memory space
  StaticJsonBuffer<400> jsonBuffer;

// Step 2: Build object tree in memory
  JsonObject& jRead = jsonBuffer.createObject();
    jRead["sensor"] = sSensorId;
    jRead["value"] = "nRead";
    jRead["timestamp"] = 123456;
  
  JsonObject& jMessage = jsonBuffer.createObject();
    jMessage["account"]  = sAccount;
    jMessage["device"]   = sDevice;
    jMessage["devToken"] = sToken;
    jMessage["messType"] = sMsgType;
    jMessage["proxy"]    = sProxy;
  JsonArray& messages = jMessage.createNestedArray("messages");
    messages.add(jRead);

  JsonObject& jArgs = jsonBuffer.createObject();
  JsonArray& args = jArgs.createNestedArray("args");
    args.add(jMessage);

// Step 3: Generate the JSON string
  jArgs.printTo(Serial);

 if (nRead < 2) { 
  trafficLightGreen();
 }else
  if(nRead < 4)
 {
  trafficLightYellow();
  
 }else{
  trafficLightRed();
  
 }
}

// LIBRARY
void trafficLightGreen()
{
  digitalWrite(nGreenLED, HIGH);
  digitalWrite(nYellowLED, LOW);
  digitalWrite(nRedLED, LOW); 
}

void trafficLightYellow()
{
  digitalWrite(nGreenLED, LOW);
  digitalWrite(nYellowLED, HIGH);
  digitalWrite(nRedLED, LOW); 
}

void trafficLightRed()
{
  digitalWrite(nGreenLED, LOW);
  digitalWrite(nYellowLED, LOW);
  digitalWrite(nRedLED, HIGH); 
}
