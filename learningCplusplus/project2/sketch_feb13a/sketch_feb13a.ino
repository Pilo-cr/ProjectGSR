int switchState = 0;
void setup() {
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(2, INPUT);
}
void loop() {
  switchState = digitalRead(2);

  if (switchState == LOW) {
    // the button is not pressed
    digitalWrite(3, HIGH); //green LED
    digitalWrite(4, LOW); // red LED
    digitalWrite(5, LOW); //red LED
  }
  else{ //switch isnt pressed
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);

    delay(500);//waits half a second
    digitalWrite(4, LOW);//turns it off
    delay(500);
  }
}//goes back to beggining of loop
