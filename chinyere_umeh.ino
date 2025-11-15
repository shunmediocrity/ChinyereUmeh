#define LED_R 9
#define LED_G 10
#define LED_B 11
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_R, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_B, HIGH);  // turn the LED on (HIGH is the voltage level)
  digitalWrite(LED_R, HIGH); 

  delay(1000);                      // wait for a second
  digitalWrite(LED_B, LOW);   // turn the LED off by making the voltage LOW
  digitalWrite(LED_R, LOW); 
  delay(1000);                      // wait for a second
}