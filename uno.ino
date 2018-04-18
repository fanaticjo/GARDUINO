
/* Comment this out to disable prints and save space */
/*This file is part of GARDUINO.GARDUINO is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 of the License,or(at your option) any later version . 
GARDUINO is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details.You should have received a copy of the GNU General Public License along with GARDUINO.
If not, see <http://www.gnu.org/licenses/>. */
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


