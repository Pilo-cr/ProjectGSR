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


  if (data > 615){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  else if (450=< data =<615){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }
  else if (data<450){
    digitalWrite(2,HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else{
    digitalWrite(2,LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);

  }
  delay(1000);

}

