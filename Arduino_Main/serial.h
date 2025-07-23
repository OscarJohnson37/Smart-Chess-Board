#ifndef SERIAL_H
#define SERIAL_H

#include <Arduino.h>

#define BAUD_RATE 9600

// Reads a line from Serial (terminated by '\n')
// Returns an empty String if no complete line is available
String readSerialLine();


//Sends a 64 bit bitmap which has been flattened to a 64 bit string, with < and > to begin and end the message
void sendBitmapString(String board[]);

// Initialises serial
void initSerial();

#endif
