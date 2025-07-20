#include <Arduino.h>

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

void sendBitmapString(String board[]) {
  String bitmap = getBitmapString(board);
  Serial.print('<');
  Serial.print(bitmap);
  Serial.print('>');
  Serial.print('\n');
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
  sendBitmapString(board);
  delay(2000);
  pickUpPiece("e2", board);
  sendBitmapString(board);
  delay(2000);
  placePiece("e4", board);
  sendBitmapString(board);
  delay(2000);
  pickUpPiece("e4", board);
  sendBitmapString(board);
  delay(2000);
  placePiece("e2", board);
  sendBitmapString(board);
  delay(2000);
}
