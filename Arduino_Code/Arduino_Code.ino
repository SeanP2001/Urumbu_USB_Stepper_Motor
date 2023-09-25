//
// This code is a lightly modified version of the original 
// code written by Neil Gershenfeld and Quentin Bolsee.
//
// Original code available here: 
// https://gitlab.cba.mit.edu/neilg/urumbu/-/tree/master/serialstep/serialstep.ino
//
// This work may be reproduced, modified, distributed,
// performed, and displayed for any purpose, but must
// acknowledge this project. Copyright is retained and
// must be preserved. The work is provided as is; no
// warranty is provided, and users accept all liability.
//

#define LEDA 2
#define LEDC 4
#define EN 5
#define DIR 8
#define STEP 9
#define M1 14
#define M0 15
#define NSTEPS 1000
#define DELAYHIGH 10
#define DELAYLOW 1000
#define BLINK 100
#define BUTTON 31

void setup() {
   SerialUSB.begin(9600);
   digitalWrite(LEDA,HIGH);
   pinMode(LEDA,OUTPUT);
   digitalWrite(LEDC,LOW);
   pinMode(LEDC,OUTPUT);
   digitalWrite(EN,LOW);
   pinMode(EN,OUTPUT);
   digitalWrite(STEP,LOW);
   pinMode(STEP,OUTPUT);
   digitalWrite(DIR,LOW);
   pinMode(DIR,OUTPUT);
}

void loop() {
   if (SerialUSB.available()) {
      char c = SerialUSB.read();
      if (c == 'f') {
         digitalWrite(DIR,HIGH);
         digitalWrite(STEP,HIGH);
         delayMicroseconds(2);
         digitalWrite(STEP,LOW);
      }
      else if (c == 'r') {
         digitalWrite(DIR,LOW);
         digitalWrite(STEP,HIGH);
         delayMicroseconds(2);
         digitalWrite(STEP,LOW);
      }
   }
}
