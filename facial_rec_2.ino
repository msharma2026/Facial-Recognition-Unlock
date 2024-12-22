#include <BluetoothSerial.h>

BluetoothSerial SerialBT;
#define led 2;
#define lock 3;


void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32");
  pinMode(led, OUTPUT);
  pinMode(lock, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    String command = SerialBT.readString();
    if (command == "BLINK") {
      digitalWrite(led, HIGH);
      delay(2500);
      digitalWrite(led, LOW);
    }
    else if (command == "RAPID") {
      int i = 10;
      while(i != 0) {
        digitalWrite(led, HIGH);
        delay(100);
        digitalWrite(led, LOW);
        delay(100);
        i--;
      }
    }
    else if (command == "ON") {
      digitalWrite(led, HIGH);
    }
    else if (command == "OFF") {
      digitalWrite(led, LOW);
    }
    else if (command == "UNLOCK") {
      digitalWrite(lock, HIGH);
    }
    else if (command == "LOCK") {
      digitalWrite(lock, LOW);
    }
  }
}