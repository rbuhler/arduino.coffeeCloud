
#include <ArduinoJson.h>

// Hardware Config
int iLumiSensor=0;    //pin 0 : Luminosity sensor

int iGreenLED=8;    //digital pin  8 : GrenLED
int iYellowLED=9;   //digital pin  9 : YellowLED
int iRedLED=10;     //digital pin 13 : RedLED

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

  pinMode(iGreenLED, OUTPUT);    //pin setup as digital output
  pinMode(iYellowLED, OUTPUT);   //pin setup as digital output
  pinMode(iRedLED, OUTPUT);      //pin setup as digital output
 
  digitalWrite(iGreenLED, LOW);  //LED switched off
  digitalWrite(iYellowLED, LOW); //LED switched off
  digitalWrite(iRedLED, LOW);    //LED switched off

  sAccount  = "p1941020166trial";
  sDevice   = "9e8f52bf-281c-4fbc-9a34-9cd8e58710b5";
  sToken    = "31479766523918bd1ef473b1d1a8b1a2";
  sMsgType  = "ba2434ef5c2b4bc8de83";
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
    jRead["sensor"]    = sSensorId;
    jRead["value"]     = iRead;
  
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

 if (iRead < 2) { 
  trafficLightGreen();
 }else
  if(iRead < 4)
 {
  trafficLightYellow();
 }else{
  trafficLightRed();
  
 }
}

// LIBRARY
void trafficLightGreen()
{
  digitalWrite(iGreenLED, HIGH);
  digitalWrite(iYellowLED, LOW);
  digitalWrite(iRedLED, LOW); 
}

void trafficLightYellow()
{
  digitalWrite(iGreenLED, LOW);
  digitalWrite(iYellowLED, HIGH);
  digitalWrite(iRedLED, LOW); 
}

void trafficLightRed()
{
  digitalWrite(iGreenLED, LOW);
  digitalWrite(iYellowLED, LOW);
  digitalWrite(iRedLED, HIGH); 
}
