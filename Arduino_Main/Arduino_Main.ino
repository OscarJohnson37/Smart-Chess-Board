#include <Arduino.h>
#include "serial.h"
#include "bitmap.h"


void setup() {
  // put your setup code here, to run once:
  initSerial();
}

void loop() {

  // example code for reading a line from serial
  String line = readSerialLine();
  if (line.length() > 0) {
    Serial.print("Got line: ");
    Serial.println(line);
  }

}