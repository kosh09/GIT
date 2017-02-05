
//---------------------------------------------------------------- HEADER Declare
#include <SoftwareSerial.h>

//---------------------------------------------------------------- BLUETOOTH Declare
SoftwareSerial BTSerial(2, 3); // RX, TX

//---------------------------------------------------------------- PIN Declare
int PIN_ANALOG_X = 0;
int PIN_ANALOG_Y = 1;
int PIN_BUTTON_DOWN = 4;
int PIN_BUTTON_LEFT = 5;

int LED_1 = 12;
int LED_2 = 13;
boolean STATE_L = true;
boolean STATE_D = false;

boolean old_STATE_L;
boolean old_STATE_D;

int DOWN;
int LEFT;
int X;
int Y;

//---------------------------------------------------------------- Initialisation( same baudrate as python script)
void setup()
{
  BTSerial.begin(57600);

  //-------------------------------------------------------------- PINMODE Setting
  pinMode(PIN_BUTTON_LEFT, INPUT_PULLUP);
  pinMode(PIN_BUTTON_DOWN, INPUT_PULLUP);
  pinMode(LED_2, OUTPUT);
  digitalWrite(LED_2,HIGH);
}


void loop()
{
   Read_Data();
   delay(50);
   Send_Joystick(X, Y);
   delay(50);
   Send_Button();
   delay(50);
}

//---------------------------------------------------------------- FUNCTION Declare

//---------------------------------------------------------------- Read the analog and digital value that I want
void Read_Data()
{
  Y = analogRead(PIN_ANALOG_X);
  X = analogRead(PIN_ANALOG_Y);
}

//---------------------------------------------------------------- Send data to main board via Bluetooth
void Send_Joystick(int X, int Y)
{
       if(880 <= X && X < 1025 &&   0 <= Y && Y < 140){ BTSerial.write(10);}
  else if(740 <= X && X < 880  &&   0 <= Y && Y < 140){ BTSerial.write(11);}
  else if(600 <= X && X < 740  &&   0 <= Y && Y < 140){ BTSerial.write(12);}
  else if(440 <= X && X < 600  &&   0 <= Y && Y < 140){ BTSerial.write(13);}
  else if(300 <= X && X < 440  &&   0 <= Y && Y < 140){ BTSerial.write(14);}
  else if(160 <= X && X < 300  &&   0 <= Y && Y < 140){ BTSerial.write(15);}
  else if(  0 <= X && X < 160  &&   0 <= Y && Y < 140){ BTSerial.write(16);}


  else if(880 <= X && X < 1025 && 140 <= Y && Y < 280){ BTSerial.write(17);}
  else if(740 <= X && X < 880  && 140 <= Y && Y < 280){ BTSerial.write(18);}
  else if(600 <= X && X < 740  && 140 <= Y && Y < 280){ BTSerial.write(19);}
  else if(440 <= X && X < 600  && 140 <= Y && Y < 280){ BTSerial.write(20);}
  else if(300 <= X && X < 440  && 140 <= Y && Y < 280){ BTSerial.write(21);}
  else if(160 <= X && X < 300  && 140 <= Y && Y < 280){ BTSerial.write(22);}
  else if(  0 <= X && X < 160  && 140 <= Y && Y < 280){ BTSerial.write(23);}

  else if(880 <= X && X < 1025 && 280 <= Y && Y < 420){ BTSerial.write(24);}
  else if(740 <= X && X < 880  && 280 <= Y && Y < 420){ BTSerial.write(25);}
  else if(600 <= X && X < 740  && 280 <= Y && Y < 420){ BTSerial.write(26);}
  else if(440 <= X && X < 600  && 280 <= Y && Y < 420){ BTSerial.write(27);}
  else if(300 <= X && X < 440  && 280 <= Y && Y < 420){ BTSerial.write(28);}
  else if(160 <= X && X < 300  && 280 <= Y && Y < 420){ BTSerial.write(29);}
  else if(  0 <= X && X < 160  && 280 <= Y && Y < 420){ BTSerial.write(30);}

  else if(880 <= X && X < 1025 && 420 <= Y && Y < 605){ BTSerial.write(31);}
  else if(740 <= X && X < 880  && 420 <= Y && Y < 605){ BTSerial.write(32);}
  else if(600 <= X && X < 740  && 420 <= Y && Y < 605){ BTSerial.write(33);}
  else if(440 <= X && X < 600  && 420 <= Y && Y < 605){ BTSerial.write(34);}
  else if(300 <= X && X < 440  && 420 <= Y && Y < 605){ BTSerial.write(35);}
  else if(160 <= X && X < 300  && 420 <= Y && Y < 605){ BTSerial.write(36);}
  else if(  0 <= X && X < 160  && 420 <= Y && Y < 605){ BTSerial.write(37);}

  else if(880 <= X && X < 1025 && 605 <= Y && Y < 745){ BTSerial.write(38);}
  else if(740 <= X && X < 880  && 605 <= Y && Y < 745){ BTSerial.write(39);}
  else if(600 <= X && X < 740  && 605 <= Y && Y < 745){ BTSerial.write(40);}
  else if(440 <= X && X < 600  && 605 <= Y && Y < 745){ BTSerial.write(41);}
  else if(300 <= X && X < 440  && 605 <= Y && Y < 745){ BTSerial.write(42);}
  else if(160 <= X && X < 300  && 605 <= Y && Y < 745){ BTSerial.write(43);}
  else if(  0 <= X && X < 160  && 605 <= Y && Y < 745){ BTSerial.write(44);}

  else if(880 <= X && X < 1025 && 745 <= Y && Y < 890){ BTSerial.write(45);}
  else if(740 <= X && X < 880  && 745 <= Y && Y < 890){ BTSerial.write(46);}
  else if(600 <= X && X < 740  && 745 <= Y && Y < 890){ BTSerial.write(47);}
  else if(440 <= X && X < 600  && 745 <= Y && Y < 890){ BTSerial.write(48);}
  else if(300 <= X && X < 440  && 745 <= Y && Y < 890){ BTSerial.write(49);}
  else if(160 <= X && X < 300  && 745 <= Y && Y < 890){ BTSerial.write(50);}
  else if(  0 <= X && X < 160  && 745 <= Y && Y < 890){ BTSerial.write(51);}

  else if(880 <= X && X < 1025 && 885 <= Y && Y < 1025){BTSerial.write(52);}
  else if(740 <= X && X < 880  && 885 <= Y && Y < 1025){BTSerial.write(53);}
  else if(600 <= X && X < 740  && 885 <= Y && Y < 1025){BTSerial.write(54);}
  else if(440 <= X && X < 600  && 885 <= Y && Y < 1025){BTSerial.write(55);}
  else if(300 <= X && X < 440  && 885 <= Y && Y < 1025){BTSerial.write(56);}
  else if(160 <= X && X < 300  && 885 <= Y && Y < 1025){BTSerial.write(57);}
  else if(  0 <= X && X < 160  && 885 <= Y && Y < 1025){BTSerial.write(58);}
}

//---------------------------------------------------------------- Change STATE and light when click LEFT button
void Send_Button()
{
  old_STATE_D = STATE_D;
  old_STATE_L = STATE_L;
  LEFT = digitalRead(PIN_BUTTON_LEFT);
  DOWN = digitalRead(PIN_BUTTON_DOWN);

  if(LEFT == 0){STATE_L = !STATE_L;}                              // L → Choose parking and driving
  if(DOWN == 0){STATE_D = !STATE_D;}                              // R → Turn on/off laser

  if(old_STATE_L != STATE_L && STATE_L == true){  BTSerial.write(80);} // Driving mode
  if(old_STATE_L != STATE_L && STATE_L == false){ BTSerial.write(81);} // Parking mode
  if(old_STATE_D != STATE_D && STATE_D == true){  BTSerial.write(82);} // Turn on  LED
  if(old_STATE_D != STATE_D && STATE_D == false){ BTSerial.write(83);} // Turn off LED

       if(STATE_L == true) {digitalWrite(LED_2,HIGH);}
  else if(STATE_L == false){digitalWrite(LED_2,LOW);}
       if(STATE_D == true) {digitalWrite(LED_1,HIGH);}
  else if(STATE_D == false){digitalWrite(LED_1, LOW);}
}


//---------------------------------------------------------------- Show the value of Joystick analogvalue and etc
/*void write_Data()
{
  Serial.print("LEFT: ");
  Serial.print(LEFT);

  Serial.print(" X: ");
  Serial.print(X);

  Serial.print(" Y");
  Serial.print(Y);

  Serial.print(" STATE: ");
  Serial.print(STATE);
  Serial.println();
}

//---------------------------------------------------------------- Show what will be sent via Bluetooth (shows in Serial monitor)

void What_will_send(int X, int Y)
{
    if(800 <= X && X < 1023 && 700 <= Y && Y < 1025){Serial.println("FR30");}
    else if(600 <= X && X < 800 && 700 <= Y && Y < 1025){Serial.println("FR15");}
    else if(400 <= X && X < 600 && 700 <= Y && Y < 1025){Serial.println("FS00");}
    else if(200 <= X && X < 400 && 700 <= Y && Y < 1025){Serial.println("FL15");}
    else if(0 <= X && X < 200 && 700 <= Y && Y < 1025){  Serial.println("FL30");}

    else if(800 <= X && X < 1025 && 300 <= Y && Y < 700){Serial.println("HR30");}
    else if(600 <= X && X < 800 && 300 <= Y && Y < 700){Serial.println("HR15");}
    else if(400 <= X && X < 600 && 300 <= Y && Y < 700){Serial.println("HS00");}
    else if(200 <= X && X < 400 && 300 <= Y && Y < 700){Serial.println("HL15");}
    else if(0 <= X && X < 200 && 300 <= Y && Y < 700){  Serial.println("HL30");}

    else if(800 <= X && X < 1025 && 0 <= Y && Y < 300){Serial.println("BR30");}
    else if(600 <= X && X < 800 && 0 <= Y && Y < 300){Serial.println("BR15");}
    else if(400 <= X && X < 600 && 0 <= Y && Y < 300){Serial.println("BS00");}
    else if(200 <= X && X < 400 && 0 <= Y && Y < 300){Serial.println("BL15");}
    else if(0 <= X && X < 200 && 0 <= Y && Y < 300){  Serial.println("BL30");}
}
*/
