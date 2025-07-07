import numpy as np
import pandas as pd

# Define your gesture labels
movements = ['forward', 'backward', 'left', 'right', 'resting']
data = []

# Generate data for 15 trials
for trial in range(1, 16):
    # pick a random movement for this trial
    movement = np.random.choice(movements)
    # timestamps from 0.0 to 2.5 in 0.1s steps
    timestamps = np.round(np.arange(0, 2.6, 0.1), 2)

    for t in timestamps:
        # Create synthetic sensor values with different means per movement
        if movement == 'forward':
            acc_x = np.random.normal(0.2, 0.05)
            acc_y = np.random.normal(-0.1, 0.05)
            acc_z = np.random.normal(-0.5, 0.1)
            gyro_x = np.random.normal(0, 5)
            gyro_y = np.random.normal(5, 5)
            gyro_z = np.random.normal(10, 5)
        elif movement == 'backward':
            acc_x = np.random.normal(-0.2, 0.05)
            acc_y = np.random.normal(0.1, 0.05)
            acc_z = np.random.normal(-0.5, 0.1)
            gyro_x = np.random.normal(0, 5)
            gyro_y = np.random.normal(-5, 5)
            gyro_z = np.random.normal(-10, 5)
        elif movement == 'left':
            acc_x = np.random.normal(0, 0.05)
            acc_y = np.random.normal(-0.5, 0.1)
            acc_z = np.random.normal(0.1, 0.05)
            gyro_x = np.random.normal(5, 5)
            gyro_y = np.random.normal(10, 5)
            gyro_z = np.random.normal(0, 5)
        elif movement == 'right':
            acc_x = np.random.normal(0, 0.05)
            acc_y = np.random.normal(0.5, 0.1)
            acc_z = np.random.normal(0.1, 0.05)
            gyro_x = np.random.normal(-5, 5)
            gyro_y = np.random.normal(-10, 5)
            gyro_z = np.random.normal(0, 5)
        else:  # resting
            acc_x = np.random.normal(0, 0.02)
            acc_y = np.random.normal(0, 0.02)
            acc_z = np.random.normal(0, 0.02)
            gyro_x = np.random.normal(0, 1)
            gyro_y = np.random.normal(0, 1)
            gyro_z = np.random.normal(0, 1)

        # random magnetometer & angle readings
        angle_x = np.random.normal(0, 10)
        angle_y = np.random.normal(0, 10)
        angle_z = np.random.normal(0, 10)
        mag_x   = np.random.normal(0, 50)
        mag_y   = np.random.normal(0, 50)
        mag_z   = np.random.normal(0, 50)

        data.append({
            'timestamp': t,
            'movement': movement,
            'ACC_X': acc_x,
            'ACC_Y': acc_y,
            'ACC_Z': acc_z,
            'GYRO_X': gyro_x,
            'GYRO_Y': gyro_y,
            'GYRO_Z': gyro_z,
            'ANGLE_X': angle_x,
            'ANGLE_Y': angle_y,
            'ANGLE_Z': angle_z,
            'MAG_X': mag_x,
            'MAG_Y': mag_y,
            'MAG_Z': mag_z,
            'trial': trial
        })

# Build DataFrame and write CSV
df = pd.DataFrame(data)

# Adjusted output path:
csv_path = r"C:\Users\chris\Downloads\CapstoneData\Data\synthetic_gesture_data.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file created at {csv_path}")
