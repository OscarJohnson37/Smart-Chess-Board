#include "serial.h"

String readSerialLine() {
  static String input = "";

  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      input.trim();             // Remove trailing newline or carriage return
      String result = input;
      input = "";               // Clear buffer
      return result;
    } else {
      input += c;
    }
  }

  return "";  // No complete line yet
}


void sendBitmapString(String board[]) {
  String bitmap = getBitmapString(board);
  Serial.print('<');
  Serial.print(bitmap);
  Serial.print('>');
  Serial.print('\n');
}


void initSerial() {
  Serial.begin(BAUD_RATE);
}
