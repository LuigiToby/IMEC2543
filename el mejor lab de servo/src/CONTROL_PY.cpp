#include <Arduino.h>
#include <ESP32Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

const int pinServo1 = 18;
const int pinServo2 = 19;
const int pinServo3 = 21;

String inputString = "";

void setup() {
  Serial.begin(115200);

  servo1.attach(pinServo1);
  servo2.attach(pinServo2);
  servo3.attach(pinServo3);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      int first = inputString.indexOf(',');
      int second = inputString.indexOf(',', first + 1);

      if (first > 0 && second > first) {
        int a1 = inputString.substring(0, first).toInt();
        int a2 = inputString.substring(first + 1, second).toInt();
        int a3 = inputString.substring(second + 1).toInt();

        a1 = constrain(a1, 0, 180);
        a2 = constrain(a2, 0, 180);
        a3 = constrain(a3, 0, 180);

        servo1.write(a1);
        servo2.write(a2);
        servo3.write(a3);
      }

      inputString = "";
    } else {
      inputString += c;
    }
  }
}