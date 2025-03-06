import numpy as np
import scipy.io
import pandas as pd
import os

# Ensure output directory exists
os.makedirs("Data", exist_ok=True)

df = pd.read_csv("Data1/demographics_data.csv")  # Use forward slashes for compatibility
file_names = df.iloc[:, 0].tolist()
npz_data = np.load("Data1/X.npz")  # Ensure file exists

key_list = list(npz_data.files)

for i, file_name in enumerate(file_names):
    # Define the required directories
    dir_wmLR = f"Data/Timecourses/b'{file_name}'"
    dir_wmRL = f"Data/Timecourses/b'{file_name}'"
    dir_wmLR1 = f"Data/Timecourses/{file_name}"
    dir_wmRL1 = f"Data/Timecourses/{file_name}"

    # Create directories if they don't exist
    os.makedirs(dir_wmLR, exist_ok=True)
    os.makedirs(dir_wmRL, exist_ok=True)
    os.makedirs(dir_wmLR1, exist_ok=True)
    os.makedirs(dir_wmRL1, exist_ok=True)

    # Save the .mat files
    time_series = npz_data[key_list[i]]
    scipy.io.savemat(f"{dir_wmLR}/power_264_tfMRI_WM_LR.mat", {"wmLR": time_series[:, :140].T})
    scipy.io.savemat(f"{dir_wmRL}/power_264_tfMRI_WM_RL.mat", {"wmRL": time_series[:, :140].T})
    scipy.io.savemat(f"{dir_wmLR1}/power_264_tfMRI_WM_LR.mat", {"wmLR": time_series[:, :140].T})
    scipy.io.savemat(f"{dir_wmRL1}/power_264_tfMRI_WM_RL.mat", {"wmRL": time_series[:, :140].T})

print("Done")
