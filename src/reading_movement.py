# send_payload.py
import serial
import serial.tools.list_ports
import time
import sys

def find_esp32_s3():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "ESP32" in p.description or "USB Serial" in p.description or "COM" in p.device:
            print(f"Found possible ESP32-S3 port: {p.device} - {p.description}")
            return p.device
    return None

def load_lines(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        sys.exit(1)

def main():
    port = find_esp32_s3()
    if not port:
        print("ESP32-S3 not found! Plug it in and try again.")
        sys.exit(1)

    print(f"Connecting to {port} @ 115200...")
    ser = serial.Serial(port, 115200, timeout=1)
    time.sleep(1.5)
    ser.flushInput()

    print("Connected!")

    # LOAD BOTH FILES
    key_lines = load_lines("keyboard.txt")
    mouse_lines = load_lines("mouse.txt")

    print(f"Loaded {len(key_lines)} keyboard lines and {len(mouse_lines)} mouse lines.")

    i = 0
    j = 0

    # SEND BOTH STREAMS IN PARALLEL
    try:
        while i < len(key_lines) or j < len(mouse_lines):

            if i < len(key_lines):
                msg = f"KEY:{key_lines[i]}"
                print("SEND", msg)
                ser.write((msg + "\n").encode())
                i += 1
                time.sleep(0.05)

            if j < len(mouse_lines):
                msg = f"MOUSE:{mouse_lines[j]}"
                print("SEND", msg)
                ser.write((msg + "\n").encode())
                j += 1
                time.sleep(0.05)

    except KeyboardInterrupt:
        pass
    finally:
        ser.close()
        print("\nDisconnected.")

if __name__ == "__main__":
    main()
