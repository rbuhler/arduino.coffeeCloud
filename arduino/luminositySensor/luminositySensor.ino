
int analogPin=0;   //define a variável como entrada analógica
          //no pino 0 para o Módulo Sensor de Luz.
int ledVerde=8;   //inicializando uma variável denominada
          //ledVerde no pino digital 8 do Arduino.

int ledAmarelo=9;   //inicializando uma variável denominada
                    //ledAmarelo no pino digital 9 do Arduino.
int ledVermelho=10; //inicializando uma variável denominada
                    //ledVermelho no pino digital 13 do Arduino.
int valAnalog;      //variável para armazenar o valor analógico
                    //lido pelo sensor LDR.
int tensao;         //variável para armazenar o valor da tensão
                    //após a conversão do valor analógico lido.
///////////
// SETUP //
///////////
void setup()
{
//Serial.begin(9600);   //setando a comunicação via porta
//serial à uma velocidade de
//9600bps(baud).

 pinMode(ledVerde, OUTPUT);   //configurando o pino8(ledVerde)
                              //como uma SAÍDA digital.

 pinMode(ledAmarelo, OUTPUT);   //configurando o pino9(ledAmarelo)
                                //como uma SAÍDA digital.

 pinMode(ledVermelho, OUTPUT);  //configurando o pino10(ledVermelho)
                //como uma SAÍDA digital.
 
 digitalWrite(ledVerde, LOW);     //Apaga o LED Verde.
 digitalWrite(ledAmarelo, LOW);   //Apaga o LED Amarelo.
 digitalWrite(ledVermelho, LOW);  //Apaga o LED Vermelho.
}
///////////
// LOOP //
///////////
void loop()
{
 valAnalog = analogRead(analogPin); //Lê o pino de entrada
                  //analógico zero (A0).

 /*
 Para converter os valores lidos pelo Módulo em tensão, deve-se
 ler o valor do sensor LDR do Módulo conectado na porta analógica
 do Arduino, cuja leitura varia de 0 a 1023, divide-se essa
 faixa em 5 seções, isso resultará no mapeamento do intervalo
 de 0V a 5V.
 */
 tensao = map(valAnalog, 0, 1023, 0, 5);

 //Serial.println(tensao); //imprime o conteúdo da variável
 //tensao e salta uma linha.

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
