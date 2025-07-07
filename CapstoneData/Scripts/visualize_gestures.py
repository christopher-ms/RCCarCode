import os
import pandas as pd
import matplotlib.pyplot as plt

# --- Paths (adjust if needed) ---
data_path = r"C:\Users\chris\Downloads\CapstoneData\Data\synthetic_gesture_data.csv"
output_dir = r"C:\Users\chris\Downloads\CapstoneData\Outputs"

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# --- Load data ---
df = pd.read_csv(data_path)

# --- Plot 1: ACC_Z time series by gesture ---
plt.figure()
for movement, group in df.groupby('movement'):
    plt.plot(group['timestamp'], group['ACC_Z'], label=movement)
plt.xlabel('Timestamp (s)')
plt.ylabel('ACC_Z')
plt.title('ACC_Z over Time by Movement')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'acc_z_time_series.png'))
plt.close()

# --- Plot 2: ACC_Y vs GYRO_Z scatter by gesture ---
plt.figure()
for movement, group in df.groupby('movement'):
    plt.scatter(group['ACC_Y'], group['GYRO_Z'], label=movement, alpha=0.7)
plt.xlabel('ACC_Y')
plt.ylabel('GYRO_Z')
plt.title('ACC_Y vs GYRO_Z by Movement')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'acc_y_vs_gyro_z_scatter.png'))
plt.close()

# --- Plot 3: Boxplot of GYRO_Z by movement ---
plt.figure()
df.boxplot(column='GYRO_Z', by='movement', grid=False)
plt.title('Boxplot of GYRO_Z by Movement')
plt.suptitle('')  # remove automatic subtitle
plt.xlabel('Movement')
plt.ylabel('GYRO_Z')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'gyro_z_boxplot.png'))
plt.close()

print(f"Plots saved to {output_dir}")
