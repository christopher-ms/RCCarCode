#!/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
import time
from bleak import BleakClient, BleakScanner

# Replace with your device's address
DEVICE_ADDRESS = "FFE8C585-20A3-4DCA-7C74-A584DC16EAE7"
# Replace with the correct characteristic UUID that sends sensor data
CHAR_UUID = "0000ffe4-0000-1000-8000-00805f9a34fb"

class TestGyro:
    def __init__(self):
        # Initialize all sensor value variables
        self.latest_acc_x = None
        self.latest_acc_y = None
        self.latest_acc_z = None
        self.latest_as_x = None
        self.latest_as_y = None
        self.latest_as_z = None
        self.latest_ang_x = None
        self.latest_ang_y = None
        self.latest_ang_z = None
        self.latest_hx = None
        self.latest_hy = None
        self.latest_hz = None

    def notification_handler(self, sender, data):
        """
        This function is called every time a new BLE notification is received.
        Here, we update our sensor values.
        
        Note: Replace the dummy conversion below with your actual data parsing logic.
        """
        # Dummy conversion: simply use the first byte for all values for demonstration.
        # In practice, you would decode "data" according to your device's protocol.
        if len(data) > 0:
            val = data[0]
            self.latest_acc_x = val
            self.latest_acc_y = val + 1
            self.latest_acc_z = val + 2
            self.latest_as_x  = val + 3
            self.latest_as_y  = val + 4
            self.latest_as_z  = val + 5
            self.latest_ang_x = val + 6
            self.latest_ang_y = val + 7
            self.latest_ang_z = val + 8
            self.latest_hx    = val + 9
            self.latest_hy    = val + 10
            self.latest_hz    = val + 11

        # (Optional) Immediately print a debug line every notification:
        # print(f"Notification: AsX={self.latest_as_x}, AsY={self.latest_as_y}, ...")

    async def run(self):
        print("Scanning for device...")
        device = await BleakScanner.find_device_by_address(DEVICE_ADDRESS, timeout=15)
        if not device:
            print("Device not found.")
            return

        print(f"Found device: {device.address}")
        async with BleakClient(device) as client:
            if client.is_connected:
                print("Connected. Subscribing to notifications...")
                await client.start_notify(CHAR_UUID, self.notification_handler)
                print("Now printing sensor values every 5 seconds...")
                try:
                    while True:
                        await asyncio.sleep(5)  # Wait 5 seconds before printing
                        print("---- Gyro Sensor Values ----")
                        print(f"AccX: {self.latest_acc_x}")
                        print(f"AccY: {self.latest_acc_y}")
                        print(f"AccZ: {self.latest_acc_z}")
                        print(f"AsX:  {self.latest_as_x}")
                        print(f"AsY:  {self.latest_as_y}")
                        print(f"AsZ:  {self.latest_as_z}")
                        print(f"AngX: {self.latest_ang_x}")
                        print(f"AngY: {self.latest_ang_y}")
                        print(f"AngZ: {self.latest_ang_z}")
                        print(f"Hx:   {self.latest_hx}")
                        print(f"Hy:   {self.latest_hy}")
                        print(f"HZ:   {self.latest_hz}")
                        print("----------------------------")
                except KeyboardInterrupt:
                    print("Stopping notifications...")
                    await client.stop_notify(CHAR_UUID)
            else:
                print("Connection failed.")

if __name__ == "__main__":
    test_gyro = TestGyro()
    asyncio.run(test_gyro.run())
