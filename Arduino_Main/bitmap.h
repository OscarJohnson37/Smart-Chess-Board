#ifndef BITMAP_H
#define BITMAP_H

#include <Arduino.h>


// Turns a list of 64 bits into a string with <> on either end of the message
String getBitmapString(String board[]);


// Turns a square in chess notation, ie e1, into its index in the bitmap list
int squareToIndex(String square);


// Simulates picking up a piece by taking a chess notation square, which is turned to a 0 in the bitmap
void pickUpPiece(String square, String board[]);


// Simulates placing a piece by taking a chess notation square, which is turned to a 1 in the bitmap
void placePiece(String square, String board[]);

#endif