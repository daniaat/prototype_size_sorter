/* 
  Arduino code to control 5 servo motors which will be used to controls the fo doors in part C, and a doo in part B in the design. 

  Poject: Size Sorting  
  Authors: Mostafa Elkabir & Taha Anwar 
 */

// get servo library // 
#include <Servo.h>

// create servo objects// 

Servo myservo_CW;  
Servo myservo_CE;  
Servo myservo_CN;  
Servo myservo_CS;  
Servo myservo_B; 

void setup() { 
  ///// inbitilization of servos used to controll the doors
  myservo_CW.attach(5);  // attaches the servo on pin 5 to the servo object // FOR PART C west door   
  myservo_CE.attach(6);  // attaches the servo on pin 6 to the servo object // FOR PART C EAST DOOR
  myservo_CN.attach(9);  // attaches the servo on pin 9 to the servo object // FOR PART C NORTH SIDE DOOR
  myservo_CS.attach(10);  // attaches the servo on pin 10 to the servo object // PART C SOUTH DOOR  
  myservo_B.attach(11);  // attaches the servo on pin 11 to the servo object // PART B door
}

void loop() {

int command = 0; 

// first hear the command comming from the RPI, and then send the corresponding control signals //// 
 switch (command) {
    case 0:    
      myservo_CW.write(0);              
      delay(150); 
      break;
    case 1:    
      myservo_CW.write(45);             
      delay(150); 
      break;
    case 2:    
      myservo_CN.write(0); 
      delay(150)
      break; 
    case 3:    
      myservo_CN.write(45);             
      delay(150); 
]      break;
    case 4:    
      myservo_CE.write(0);              
      delay(150); 
      break;
    case 5:    
      myservo_CE.write(45);
      break;
   case 6:    
      myservo_CS.write(0);             
      delay(150); 
      break;
    case 7:    
      myservo_CS.write(45);              
      delay(150); 
      break;
    case 8:    
      myservo_B.write(0); 
      delay(150); 
      break;
    case 9:    
      myservo_B.write(45);  
      delay(150); 
      break;
  } 
}
