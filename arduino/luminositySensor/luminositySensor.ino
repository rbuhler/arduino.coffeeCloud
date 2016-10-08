
// Hardware Config
int analogPin=0;    //no pino 0 para o Módulo Sensor de Luz.

int ledVerde=8;     //ledVerde no pino digital 8 do Arduino.
int ledAmarelo=9;   //ledAmarelo no pino digital 9 do Arduino.
int ledVermelho=10; //ledVermelho no pino digital 13 do Arduino.

int valAnalog;      //variável para armazenar o valor analógico
                    
int tensao;         //variável para armazenar o valor da tensão

// Device Hana IoT SetUp
String sAccount  = "p1941020166trial";
String sDevice   = "9e8f52bf-281c-4fbc-9a34-9cd8e58710b5";
String sToken    = "31479766523918bd1ef473b1d1a8b1a2";
String sMsgType  = "ba2434ef5c2b4bc8de83";
String sProxy    = "";

String sSensorId = "ArdoLumy";

void setup()
{
Serial.begin(9600); //serial à uma velocidade de 9600bps(baud).

 pinMode(ledVerde, OUTPUT);   //configurando o pino8(ledVerde) como uma SAÍDA digital.
 pinMode(ledAmarelo, OUTPUT);   //configurando o pino9(ledAmarelo) como uma SAÍDA digital.
 pinMode(ledVermelho, OUTPUT);  //configurando o pino10(ledVermelho) como uma SAÍDA digital.
 
 digitalWrite(ledVerde, LOW);     //Apaga o LED Verde.
 digitalWrite(ledAmarelo, LOW);   //Apaga o LED Amarelo.
 digitalWrite(ledVermelho, HIGH);  //Liga o LED Vermelho.
}

void loop()
{
 valAnalog = analogRead(analogPin); //Lê o pino de entrada analógico zero (A0).
 /*
 Para converter os valores lidos pelo Módulo em tensão, deve-se
 ler o valor do sensor LDR do Módulo conectado na porta analógica
 do Arduino, cuja leitura varia de 0 a 1023, divide-se essa
 faixa em 5 seções, isso resultará no mapeamento do intervalo
 de 0V a 5V.
 */
 tensao = map(valAnalog, 0, 1023, 0, 5);
 Serial.println(tensao);
 
 if (tensao < 2) { 
  digitalWrite(ledVerde, HIGH); //Acende o LED Verde.
  digitalWrite(ledAmarelo, LOW); //Apaga o LED Amarelo.
  digitalWrite(ledVermelho, LOW); //Apaga o LED Vermelho.
  
 }else
  if(tensao < 4)
 {
  digitalWrite(ledAmarelo, HIGH); //Acende o LED Amarelo.
  digitalWrite(ledVerde, HIGH); //Apaga o LED Verde.
  digitalWrite(ledVermelho, LOW); //Apaga o LED Vermelho.
  
 }else{
  digitalWrite(ledVermelho, HIGH); //Acende o LED Vermelho.
  digitalWrite(ledVerde, HIGH); //Apaga o LED Verde.
  digitalWrite(ledAmarelo, HIGH); //Apaga o LED Amarelo.
  
 }
}

// LIBRARY
void trafficLightGreen()
{
  digitalWrite(ledVerde, HIGH);
  digitalWrite(ledAmarelo, LOW);
  digitalWrite(ledVermelho, LOW); 
}

void trafficLightYellow()
{
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarelo, HIGH);
  digitalWrite(ledVermelho, LOW); 
}

void trafficLightYellow()
{
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarelo, LOW);
  digitalWrite(ledVermelho, HIGH); 
}
