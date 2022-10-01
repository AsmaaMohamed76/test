//Asmaa Mohamed
#include <SoftwareSerial.h>
#include <NewPing.h>

SoftwareSerial mySerial(2, 3); // RX | TX
#define trig A1 //analog input 1 (Trigger pin)
#define echo A2 //analog input 2 ( echo pin)

//Ahmed Magdy
#define maximum_distance 200
boolean goesForward = false;
int distance = 100;

NewPing sonar(trig, echo, maximum_distance); //sensor function

//Asmaa Mohamed
char command ;
//motors
int forward_motor_left = 13 ;
int forward_motor_right = 11;
int reverse_motor_left = 12;
int reverse_motor_right = 10;

//to stop the car
void stop()
{
  digitalWrite(forward_motor_left, LOW);
  digitalWrite(reverse_motor_left, LOW);
  digitalWrite(forward_motor_right, LOW);
  digitalWrite(reverse_motor_right, LOW);
  Serial.println("Stop!");
}

//move forward
void forward()
{
  digitalWrite(forward_motor_left, HIGH);
  digitalWrite(reverse_motor_left, LOW);
  digitalWrite(forward_motor_right, HIGH);
  digitalWrite(reverse_motor_right, LOW);
  Serial.println("go forward!");

}
//move backward
void backward()
{
  digitalWrite(forward_motor_left, LOW);
  digitalWrite(reverse_motor_left, HIGH);
  digitalWrite(forward_motor_right, LOW);
  digitalWrite(reverse_motor_right, HIGH);
  Serial.println("go backward!");

}

//move to left
void left()
{
  digitalWrite(forward_motor_left, LOW);
  digitalWrite(reverse_motor_left, HIGH);
  digitalWrite(forward_motor_right, HIGH);
  digitalWrite(reverse_motor_right, LOW);
  Serial.println("go left!");

}

//move to right
void right()
{
  digitalWrite(forward_motor_left, HIGH);
  digitalWrite(reverse_motor_left, LOW);
  digitalWrite(forward_motor_right, LOW);
  digitalWrite(reverse_motor_right, HIGH);
  Serial.println("go right!");
  

}
//Asmaa Mohamed
void setup()
{
  Serial.begin(9600);
  mySerial.begin(9600);
  Serial.println("You're connected via Bluetooth");
  pinMode(forward_motor_left, OUTPUT);
  pinMode(reverse_motor_left, OUTPUT);
  pinMode(forward_motor_right, OUTPUT);
  pinMode(reverse_motor_right, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

//Ahmed Magdy
  distance = readPing();
  delay(100);
  
}

void loop()
{

 //Ahmed Magdy
  int distanceRight = 0;
  int distanceLeft = 0;
  delay(50);

  if (distance <= 20){
    stop();
    delay(300);
    backward();
    delay(400);
    stop();
    delay(300);
  }

   else{ 
    //Asmaa Mohamed
  command=Serial.read();
    command=(mySerial.read());
    switch(command){
    case 'F':  
       forward();
       delay(200);
      break;
    case 'B':  
       backward();
       delay(200);
      break;
    case 'L':  
       left();
       delay(200);
      break;
    case 'R':
      right();
      delay(200);
    case's':
       stop();
       delay(200); 
      break;
    }
   } 
    distance = readPing();
}  

//Ahmed Magdy
int readPing(){
  delay(70);
  int cm = sonar.ping_cm();
  if (cm==0){
    cm=250;
  }
  return cm;
}

   
