int red_led = 12;
int yellow_led = 11;
int green_led = 10;
int push_button = 6;
int button;

void setup()
{
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  pinMode(push_button, INPUT);
}

void loop()
{
  //push up 
  button == LOW;
  button = digitalRead(push_button);
  //push down to change traffic lights
  if(button == HIGH)
  {
    //turn on red for 1 second
    digitalWrite(red_led, HIGH);
    delay(1000);
    digitalWrite(red_led, LOW);
    //turn on yellow for 1 second
    digitalWrite(yellow_led, HIGH);
    delay(1000);
    digitalWrite(yellow_led, LOW);
    //turn on green for 1 second
    digitalWrite(green_led, HIGH);
    delay(1000);
    //turn off green for 0.5 second
    digitalWrite(green_led, LOW);
    delay(500);
  }
  else
  {
    digitalWrite(red_led, LOW);
    digitalWrite(yellow_led, LOW);
    digitalWrite(green_led, LOW);
  }   
  
}
