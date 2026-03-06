#include <Arduino.h>
#include <ESP32Servo.h>

Servo miServo;
Servo miServo2;

const int pinServo = 4;
const int pinServo2 = 2;


void setup() {
  miServo.attach(pinServo);
  miServo2.attach(pinServo2);
}

void loop() {
  miServo.write(0);
  miServo2.write(0);
  delay(1000);

  miServo.write(90);
  miServo2.write(90);
  delay(1000);
}