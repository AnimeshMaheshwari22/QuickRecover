import sounddevice as sd

def print_device_info():
    devices = sd.query_devices()
    print("Available input devices:")
    for i, device in enumerate(devices):
        if device["max_input_channels"] > 0:
            print(f"Index {i}: {device['name']}")

if __name__ == "__main__":
    print_device_info()