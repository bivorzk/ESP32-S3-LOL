#include <Arduino.h>
#include <USB.h>
#include <USBHIDKeyboard.h>
#include "USBHID.h"
USBHIDKeyboard Keyboard;
USBHID HID;

// put function declarations here:
int myFunction(int, int);


int ledPin = 2;

const uint8_t *descriptors[5] = {
  NULL,  // Language
  (const uint8_t[]){'L', 0, 'o', 0, 'g', 0, 'i', 0, 't', 0, 'e', 0, 'c', 0, 'h', 0},  // Manufacturer: "Logitech"
  (const uint8_t[]){'G', 0, '5', 0, '1', 0, '3', 0, ' ', 0, 'R', 0, 'G', 0, 'B', 0},  // Product: "G513 RGB"
  (const uint8_t[]){'1', 0, '2', 0, '3', 0, '4', 0, '5', 0, '6', 0},  // Serial: "123456"
  NULL   // No extra
};

// Standard HID report descriptor for boot keyboard (8-byte report: modifiers, reserved, 6 keycodes)
const uint8_t hidReportDescriptor[] = {
  0x05, 0x01,  // Usage Page (Generic Desktop)
  0x09, 0x06,  // Usage (Keyboard)
  0xA1, 0x01,  // Collection (Application)
  0x85, 0x01,  //   Report ID (1)
  0x05, 0x07,  //   Usage Page (Key Codes)
  0x19, 0xe0,  //   Usage Minimum (224)
  0x29, 0xe7,  //   Usage Maximum (231)
  0x15, 0x00,  //   Logical Minimum (0)
  0x25, 0x01,  //   Logical Maximum (1)
  0x75, 0x01,  //   Report Size (1)
  0x95, 0x08,  //   Report Count (8)
  0x81, 0x02,  //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
  0x95, 0x01,  //   Report Count (1)
  0x75, 0x08,  //   Report Size (8)
  0x81, 0x01,  //   Input (Const,Ary,Abs,No Wrap,Wrap,Linear,Preferred State,No Null Position)
  0x95, 0x05,  //   Report Count (5)
  0x75, 0x01,  //   Report Size (1)
  0x05, 0x08,  //   Usage Page (LEDs)
  0x19, 0x01,  //   Usage Minimum (Num Lock)
  0x29, 0x05,  //   Usage Maximum (Kana)
  0x91, 0x02,  //   Output (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
  0x95, 0x01,  //   Report Count (1)
  0x75, 0x03,  //   Report Size (3)
  0x91, 0x01,  //   Output (Const,Ary,Abs,No Wrap,Wrap,Linear,Preferred State,No Null Position,Non-volatile)
  0x95, 0x06,  //   Report Count (6)
  0x75, 0x08,  //   Report Size (8)
  0x15, 0x00,  //   Logical Minimum (0)
  0x25, 0x65,  //   Logical Maximum (101)
  0x05, 0x07,  //   Usage Page (Key Codes)
  0x19, 0x00,  //   Usage Minimum (0)
  0x29, 0x65,  //   Usage Maximum (101)
  0x81, 0x00,  //   Input (Data,Ary,Abs,No Wrap,Wrap,Linear,Preferred State,No Null Position)
  0xC0         // End Collection
};

void setup() {


  USB.VID(0x046D);            // Vendor ID: Logitech
  USB.PID(0xC548);            // Product ID: G513
  USB.manufacturerName("Logitech");
  USB.productName("G513 RGB Mechanical Gaming Keyboard");
  USB.serialNumber("123456");       // Or generate dynamically
  // HID.begin(hidReportDescriptor, sizeof(hidReportDescriptor));  // Custom HID report
  HID.begin(); 

  Serial.begin(123456);
  while (!Serial) {;}
  
  USB.begin();
  Keyboard.begin();
  // Keyboard.print("Hello, world!");
  Serial.println("Hello world.");
  
  int result = myFunction(2, 3);
}

void loop() {
  
  if (Serial.available()) {
    char c = Serial.read();
    Keyboard.write(c);

    Serial.print("Sent key: ");
    Serial.println(c);
  }


}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}