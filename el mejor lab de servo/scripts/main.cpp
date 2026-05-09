#include <Arduino.h>
#include <ESP32Servo.h>

#include <Arduino.h>

const int LED_PIN = 2;   // LED integrado del ESP32 (generalmente GPIO 2)

void setup() {
  pinMode(LED_PIN, OUTPUT);  // Configurar el pin como salida
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // Encender LED
  delay(1000);                  // Esperar 1 segundo

  digitalWrite(LED_PIN, LOW);   // Apagar LED
  delay(1000);                  // Esperar 1 segundo
}

