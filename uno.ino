
/* Comment this out to disable prints and save space */
#define BLYNK_PRINT SwSerial

#define dhtpin 3
#include <SoftwareSerial.h>
SoftwareSerial SwSerial(10, 11); // RX, TX 
#include <BlynkSimpleStream.h>
#include<dht.h>
dht DHT;
int light=7;
int water=2;
char auth[] = "your api code";  

BlynkTimer timer;
void setup()
{
  // Debug console
  SwSerial.begin(9600);
  
  // Blynk will work through Serial
  // Do not read or write this serial manually in your sketch
 
  Serial.begin(9600);
  Blynk.begin(Serial, auth);
  timer.setInterval(1000L, myTimerEvent);
}

void loop()
{
  
  Blynk.run();
  // You can inject your own code or combine it with other sketches.
  // Check other examples on how to communicate with Blynk. Remember
  // to avoid delay() function!
  timer.run();
}
void myTimerEvent()
{
  int check=DHT.read11(dhtpin);
  int sensor=DHT.temperature;
  int humidity=DHT.humidity;
  int soil=analogRead(A0);
  Blynk.virtualWrite(V7,soil);
 Blynk.virtualWrite(V5,sensor);
 Blynk.virtualWrite(V6,humidity);

}


