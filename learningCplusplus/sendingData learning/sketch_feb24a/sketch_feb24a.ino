const int sensorpin = A2;
int data;
int time=0;
void setup(){
  Serial.begin(9600);
}

void loop(){
  char message[10];

  data=analogRead(sensorpin);
  sprintf(message, "%d;%d", data, time);

  Serial.println(message);

  delay(1000);
  
  time++;

  Serial.flush();
}
