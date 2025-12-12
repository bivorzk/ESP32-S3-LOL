  #include <Arduino.h>
  #include <USB.h>
  #include <USBHIDKeyboard.h>
  #include "USBHIDMouse.h"
  #include "USBHID.h"
  USBHIDKeyboard Keyboard;
  USBHID HID;
  USBHIDMouse Mouse;

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
    Serial.begin(115200);
    delay(2000);  // Give time to connect serial monitor

    Serial.println("ESP32-S3 Starting...");
    Serial.println("Type 'start' to enable keyboard mode");
    Serial.println("Or send any other text to test serial communication");

    // Don't start USB HID immediately
  }

  bool keyboardEnabled = false;

  void loop() {
    if (Serial.available()) {
      String line = Serial.readStringUntil('\n');  // Read full line from Python
      line.trim();                                 // Remove \r\n

      if (line.length() > 0) {
        if (line == "start" && !keyboardEnabled) {
          // Initialize USB HID keyboard
          Serial.println("Initializing USB HID keyboard...");
          USB.VID(0x046D);                             // Logitech
          USB.PID(0xC548);                             // G513 exact PID
          USB.manufacturerName("Logitech");
          USB.productName("G513 RGB Mechanical Gaming Keyboard");
          USB.serialNumber("133713371337");

          USB.begin();        // Starts TinyUSB + CDC + HID
          Keyboard.begin();   // Register keyboard
          keyboardEnabled = true;
          Serial.println("Keyboard mode enabled! Send text to type it out.");
        } else if (keyboardEnabled) {
          if (line == "space") {
            Keyboard.press(HID_KEY_SPACE); 
          } else if (line == "d") {
            Keyboard.press(HID_KEY_D); 
          } else if (line == "y"){
            Keyboard.press(HID_KEY_Y);
          }else if (line == "a"){
            Keyboard.press(HID_KEY_A);
          }else if (line == "tab"){
            Keyboard.press(HID_KEY_TAB);
          }
          Keyboard.println();       // Press Enter at the end (optional, remove if unwanted)
          Serial.println("[Typed] " + line);  // Debug echo
        } else {
          Serial.println("[Echo] " + line);  // Just echo back for testing
        }
      }
    }
  }

  // put function definitions here:
  int myFunction(int x, int y) {
    return x + y;
  }