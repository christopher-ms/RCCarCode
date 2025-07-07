import numpy as np
import pandas as pd

# Force exactly 3 trials of each movement
movements = ['forward', 'backward', 'left', 'right', 'resting']
data = []

# 15 trials, 3 of each
trial = 1
for movement in movements:
    for _ in range(3):
        timestamps = np.round(np.arange(0, 2.6, 0.1), 2)
        for t in timestamps:
            # (same per-movement logic as before)
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

            angle_x = np.random.normal(0, 10)
            angle_y = np.random.normal(0, 10)
            angle_z = np.random.normal(0, 10)
            mag_x   = np.random.normal(0, 50)
            mag_y   = np.random.normal(0, 50)
            mag_z   = np.random.normal(0, 50)

            data.append({
                'timestamp': t,
                'movement': movement,
                'ACC_X': acc_x, 'ACC_Y': acc_y, 'ACC_Z': acc_z,
                'GYRO_X': gyro_x, 'GYRO_Y': gyro_y, 'GYRO_Z': gyro_z,
                'ANGLE_X': angle_x, 'ANGLE_Y': angle_y, 'ANGLE_Z': angle_z,
                'MAG_X': mag_x, 'MAG_Y': mag_y, 'MAG_Z': mag_z,
                'trial': trial
            })
        trial += 1

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\chris\Downloads\CapstoneData\Data\synthetic_gesture_data.csv", index=False)
print("Re-generated CSV with forward data included.")
