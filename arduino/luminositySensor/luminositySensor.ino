
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

  sAccount  = "p1941020166trial";
  sDevice   = "1e4d608a-01c9-4060-b7b3-71e4b91e31a8";
  sToken    = "1a81e19d91978bddfbeb3a6a3d45e25";
  sMsgType  = "56a55910fd4abd99f088";
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
