from scipy.io import loadmat
import pandas as pd
import scipy.io
import numpy as np
import os


df = pd.read_csv("Data1/demographics_data.csv")  # Use forward slashes for compatibility
file_names = df.iloc[:, 0].tolist()
npz_data = np.load("Data1/X.npz")  # Ensure file exists
key_list = list(npz_data.files)
mini=0
for i, file_name in enumerate(file_names):
    # Define the required directories
    dir_wmLR = f"Data/Timecourses/{file_name}"
    data = loadmat(f"{dir_wmLR}"+"/power_264_tfMRI_WM_LR.mat")
    if "wmLR" in data.keys():
        mini=max(mini,data['wmLR'].shape[1])
    else:
        mini=max(mini,data['wmRL'].shape[1]) 
print(mini)