
#include <ArduinoJson.h>

// Hardware Config
int iLumiSensor=0;    //pin 0 : Luminosity sensor

// JSON header message
String sAccount;
String sDevice;
String sToken;
String sMsgType;
String sProxy;
int iUser;
// JSON body message  
String sSensorId;
int iRead;

void setup()
{
Serial.begin(9600); //serial port speed : 9600bps(baud).

  sAccount  = "p1942282297trial";
  sDevice   = "4fd19277-4cfe-4377-9d00-dd5ca8740a44";
  sToken    = "2d879287145519929e12402e378660";
  sMsgType  = "70e9ae6a70c545c342e8";
  sProxy    = "";
  iUser     = 0x0;

  sSensorId  = "ArdoLumy";
  iRead      = 0;
}

void loop()
{

 iRead  = analogRead(iLumiSensor);   // Reads the Luminosity sensor
 
// Step 1: Reserve memory space
  StaticJsonBuffer<400> jsonBuffer;

// Step 2: Build object tree in memory
  JsonObject& jRead    = jsonBuffer.createObject();
    jRead["index"]     = 0;
    jRead["sensor"]    = sSensorId;
    jRead["timestamp"] = 0;    
    jRead["value"]     = iRead;
    jRead["user"]      = iUser;
    
  JsonObject& jMessage = jsonBuffer.createObject();
    jMessage["account"]  = sAccount;
    jMessage["device"]   = sDevice;
    jMessage["devToken"] = sToken;
    jMessage["messType"] = sMsgType;
    jMessage["proxy"]    = sProxy;
    
  JsonArray& messages    = jMessage.createNestedArray("messages");
    messages.add(jRead);

  JsonObject& jArgs = jsonBuffer.createObject();
  JsonArray& args   = jArgs.createNestedArray("args");
    args.add(jMessage);

// Step 3: Generate the JSON string
  jArgs.printTo(Serial);

}
