const int sensorpin = A2;
int data;
unsigned long time;
void setup(){
  Serial.begin(9600);
}

void loop(){
  char message[40];

  data=analogRead(sensorpin);
  time=millis();

  sprintf(message, "%d,%lu", data, time);
  Serial.println(message);
  Serial.flush();

  delay(1000);
}
