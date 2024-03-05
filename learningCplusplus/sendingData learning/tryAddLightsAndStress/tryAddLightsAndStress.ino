const int sensorpin = A2;
const int ledA = 2;
const int ledB = 3;
const int ledC = 4;


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

  if (615 < data < 700){
    digitalWrite(ledA, HIGH);
    digitalWrite(ledB, HIGH);
    digitalWrite(ledC, HIGH);
  }
  else if (450=< data =<615){
    digitalWrite(ledA, HIGH);
    digitalWrite(ledB, HIGH);
    digitalWrite(ledC, LOW);
  }
  else if (0=< data <450){
    digitalWrite(ledA,HIGH);
    digitalWrite(ledB, LOW);
    digitalWrite(ledC, LOW);
  }
  else{
    digitalWrite(ledA,LOW);
    digitalWrite(ledB, LOW);
    digitalWrite(ledC, LOW);

  }
  delay(1000);

}

