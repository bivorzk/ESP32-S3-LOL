import serial
import time







def test_esp32_keyboard():
    try:
        # Connect to ESP32
        ser = serial.Serial('COM3', 115200, timeout=2)
        time.sleep(4)  # Give ESP32 time to start
        
        print("Connected to ESP32-S3")
        
        # Clear any existing data
        ser.flushInput()
        
        # Send test message
        print("Sending test message...")
        ser.write(b'hello\n')
        time.sleep(0.5)
        
        # Read response
        response = ser.read(100)
        if response:
            print(f"ESP32 Response: {response.decode().strip()}")
        
        # Activate keyboard mode
        print("Activating keyboard mode...")
        ser.write(b'start\n')
        time.sleep(1)
        
        # Read response
        response = ser.read(200)
        if response:
            print(f"Keyboard Mode Response: {response.decode().strip()}")
            
        # Test keyboard input
        print("Sending test text to type...")
        ser.write(b'Hello World!\n')
        time.sleep(1)
        
        # Read final response
        response = ser.read(100)
        if response:
            print(f"Final Response: {response.decode().strip()}")
        
        ser.close()
        print("Test completed!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_esp32_keyboard()