#include <Arduino.h>
#include "serial.h"

String board[64] = {
  // Row 1 (A1 to H1)
  "1", "1", "1", "1", "1", "1", "1", "1",
  // Row 2
  "1", "1", "1", "1", "1", "1", "1", "1",
  // Row 3
  "0", "0", "0", "0", "0", "0", "0", "0",
  // Row 4
  "0", "0", "0", "0", "0", "0", "0", "0",
  // Row 5
  "0", "0", "0", "0", "0", "0", "0", "0",
  // Row 6
  "0", "0", "0", "0", "0", "0", "0", "0",
  // Row 7
  "1", "1", "1", "1", "1", "1", "1", "1",
  // Row 8
  "1", "1", "1", "1", "1", "1", "1", "1"
};

String getBitmapString(String board[]) {
  String result = "";
  for (int i = 0; i < 64; i++) {
    result += board[i];
  }
  return result;
}

int squareToIndex(String square) {
  int file = square.charAt(0) - 'a'; // use lowercase: 'a' to 'h'
  int rank = square.charAt(1) - '1'; // '1' to '8'
  return rank * 8 + file;
}

void pickUpPiece(String square, String board[]) {
  int index = squareToIndex(square);
  board[index] = "0";
}

void placePiece(String square, String board[]) {
  int index = squareToIndex(square);
  board[index] = "1";
}


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
