
//Asmaa Mohamed
//motors
int left_motor_1 = 6;
int left_motor_2 = 7;
int right_motor_1 = 5;
int right_motor_2 = 4;

// set push button pins
int back_button = 8; //backwards
int left_button = 9; //backwards
int right_button = 10; //forward
int forward_button = 11; //right 

// initialize button states
int back_button_st = 0;
int left_button_st = 0;
int Fwd_button_st = 0;
int right_button_st = 0; 
//to stop the car
void stop(){
digitalWrite(left_motor_1, LOW);
  digitalWrite(left_motor_2, LOW);
  digitalWrite(right_motor_1, LOW);
  digitalWrite(right_motor_2, LOW);
}

//Ahmed Nabil
//move forward
void move_forward()
{
  digitalWrite(left_motor_1, HIGH);
  digitalWrite(left_motor_2, LOW);
  digitalWrite(right_motor_1, HIGH);
  digitalWrite(right_motor_2, LOW);

}
//move backward
void move_backward()
{
  digitalWrite(left_motor_1, LOW);
  digitalWrite(left_motor_2, HIGH);
  digitalWrite(right_motor_1, LOW);
  digitalWrite(right_motor_2, HIGH);

}

//move to left
void rotate_left()
{
  digitalWrite(left_motor_1, LOW);
  digitalWrite(left_motor_2, HIGH);
  digitalWrite(right_motor_1, HIGH);
  digitalWrite(right_motor_2, LOW);

}

//move to right
void rotate_right()
{
  digitalWrite(left_motor_1, HIGH);
  digitalWrite(left_motor_2, LOW);
  digitalWrite(right_motor_1, LOW);
  digitalWrite(right_motor_2, HIGH);

}
//Asmaa Mohamed
void setup()
{
  pinMode(left_motor_1, OUTPUT);
  pinMode(left_motor_2, OUTPUT);
  pinMode(right_motor_1, OUTPUT);
  pinMode(right_motor_2, OUTPUT);
  pinMode(back_button,INPUT);
  pinMode(right_button,INPUT);
  pinMode(left_button,INPUT);
  pinMode(forward_button,INPUT);
  Serial.begin(9600);
}
//Ahmed Nabil
void loop()
{
  //back button pushed down (on)
  if (digitalRead(back_button)== HIGH){
    move_backward();
  }
  // right button pushed down (on)
  if (digitalRead(right_button)== HIGH){
    move_forward();
  }
  //left button pushed down (on)
  if (digitalRead(left_button)== HIGH){
    rotate_left();
  }
  // forward button pushed down (on)
  if (digitalRead(forward_button)== HIGH){
    rotate_right();
  }
  
  stop();
   
}
