import asyncio
from bleak import BleakClient

GYRO_ADDRESS = "FFE8C585-20A3-4DCA-7C74-A584DC16EAE7"

async def main():
    print(f"Attempting to connect to {GYRO_ADDRESS}...")
    async with BleakClient(GYRO_ADDRESS) as client:
        if client.is_connected:
            print("🎉 Successfully connected to Gyroscope!")
            print("Available services and characteristics:")
            for service in client.services:
                print(f"[Service] {service.uuid}")
                for char in service.characteristics:
                    print(f" ↳ [Characteristic] {char.uuid}, Properties: {char.properties}")
        else:
            print("Failed to connect.")

asyncio.run(main())
