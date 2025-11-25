#include <Arduino.h>
#include <USB.h>
#include <USBHIDKeyboard.h>


USBHIDKeyboard Keyboard;

// put function declarations here:
int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  USB.begin();
  Keyboard.begin();


  // Keyboard.print("Hello, world!");
  Serial.println("Hello world.");
  
  int result = myFunction(2, 3);
}

void loop() {
  
  delay(10);
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}