#include <Arduino.h>
#include <ESP32Servo.h>

Servo miServo;

const int pinServo = 4;

void moverConSpline(Servo &motor, float theta_i, float theta_f, float tiempoTotal) {

  float a0 = theta_i;
  float a1 = 0.0;
  float a2 = 3.0 * (theta_f - theta_i) / pow(tiempoTotal, 2);
  float a3 = -2.0 * (theta_f - theta_i) / pow(tiempoTotal, 3);

  int pasos = tiempoTotal * 50;
  float dt = tiempoTotal / pasos;

  for (int i = 0; i <= pasos; i++) {

    float t = i * dt;

    float theta_t =
      a0 +
      a1 * t +
      a2 * pow(t, 2) +
      a3 * pow(t, 3);

    motor.write(theta_t);

    delay(dt * 1000);   // en milisegundos
  }
}

void setup() {

  Serial.begin(115200);

  ESP32PWM::allocateTimer(0);

  miServo.setPeriodHertz(50);

  miServo.attach(pinServo, 500, 2400);
}

void loop() {

  moverConSpline(miServo, 0, 90, 2.0);  // 0 → 90 en 2 segundos
  delay(500);

  moverConSpline(miServo, 90, 0, 2.0);  // 90 → 0 en 2 segundos
  delay(500);
}