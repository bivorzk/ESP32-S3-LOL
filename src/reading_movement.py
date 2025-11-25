# send_payload.py
import serial
import serial.tools.list_ports
import time
import sys

def find_esp32_s3():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "ESP32" in p.description or "USB Serial" in p.description or "COM" in p.device:
            # Extra check: look for Logitech keyboard in description (optional)
            print(f"Found possible ESP32-S3 port: {p.device} - {p.description}")
            return p.device
    return None

def main():
    port = find_esp32_s3()
    if not port:
        print("ESP32-S3 not found! Plug it in and try again.")
        sys.exit(1)

    print(f"Connecting to {port} @ 115200...")
    ser = serial.Serial(port, 115200, timeout=1)
    time.sleep(1.5)  # Wait for ESP32 reset message
    ser.flushInput()

    print("Connected! Send your lines (empty line + Enter = quit)")

    try:
        while True:
            line = input("> ")
            if line == "":
                break
            ser.write((line + "\n").encode('utf-8'))
            time.sleep(0.05)  # Tiny delay for reliability
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()
        print("\nDisconnected.")

if __name__ == "__main__":
    main()