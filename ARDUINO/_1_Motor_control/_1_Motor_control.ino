

//---------------------------------------------------------------- HEADER Declare
#include <Servo.h>

//---------------------------------------------------------------- PIN Declare

Servo myservo;
int ServoPin = 6;
int Motor_direction = 13;
int Motor_pwm = 11;
int Motor_break = 8;
int Serial_data;

//---------------------------------------------------------------- Initialisation( same baudrate as python script)
void setup()
{
  Serial.begin(57600);                                        
  myservo.attach(ServoPin);

  //-------------------------------------------------------------- PINMODE Setting
  pinMode(Motor_direction, OUTPUT);
  pinMode(Motor_pwm, OUTPUT);
  pinMode(Motor_break, OUTPUT);
  myservo.write(80);
}

void loop()
{
  if(Serial.available())
  {
    Serial_data = (Serial.read());
    Serial_algorithm(Serial_data);
  }
}

//---------------------------------------------------------------- Fuction_Serial
void Serial_algorithm(int _data)
{
  if(_data == 10){digitalWrite(Motor_direction, HIGH); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(30);}       // FR30
  else if(_data == 11){digitalWrite(Motor_direction, HIGH); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(60);}  // FR15
  else if(_data == 12){digitalWrite(Motor_direction, HIGH); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(80);}   // FS00
  else if(_data == 13){digitalWrite(Motor_direction, HIGH); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(105);}   // FL15
  else if(_data == 14){digitalWrite(Motor_direction, HIGH); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(130);}   // FL30

  else if(_data == 15){digitalWrite(Motor_direction, NULL); analogWrite(Motor_pwm, 0); digitalWrite(Motor_break, HIGH); myservo.write(30);}   // HR30
  else if(_data == 16){digitalWrite(Motor_direction, NULL); analogWrite(Motor_pwm, 0); digitalWrite(Motor_break, HIGH); myservo.write(60);}   // HR15
  else if(_data == 17){digitalWrite(Motor_direction, NULL); analogWrite(Motor_pwm, 0); digitalWrite(Motor_break, HIGH); myservo.write(80);}    // HS00
  else if(_data == 18){digitalWrite(Motor_direction, NULL); analogWrite(Motor_pwm, 0); digitalWrite(Motor_break, HIGH); myservo.write(105);}    // HL15
  else if(_data == 19){digitalWrite(Motor_direction, NULL); analogWrite(Motor_pwm, 0); digitalWrite(Motor_break, HIGH); myservo.write(130);}    // HL30

  else if(_data == 20){digitalWrite(Motor_direction, LOW); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(30);}   // BR30
  else if(_data == 21){digitalWrite(Motor_direction, LOW); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(60);}   // BR15
  else if(_data == 22){digitalWrite(Motor_direction, LOW); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(80);}   // BS00
  else if(_data == 23){digitalWrite(Motor_direction, LOW); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(105);}   // BL15
  else if(_data == 24){digitalWrite(Motor_direction, LOW); analogWrite(Motor_pwm, 255); digitalWrite(Motor_break, LOW); myservo.write(130);}   // BL30
}

