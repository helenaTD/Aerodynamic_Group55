import matplotlib.pyplot as plt
import numpy as np
import os


inputs = "pol_1611_Re1.5e6.txt"

path = r"C:\Users\david\Desktop\Uni\Aircraft Aereodynamics\Aerodynamic_Group55\Viscous_flows"
figures_dir = r"C:\Users\david\Desktop\Uni\Aircraft Aereodynamics\Aerodynamic_Group55\figures"

# Ensure the figures directory exists
os.makedirs(figures_dir, exist_ok=True)

# Combine directory and filename for saving
save_path = os.path.join(figures_dir, "3.2.3.png")


file_path = os.path.join(path, inputs)
data = np.loadtxt(file_path, skiprows=12)
x, cp = data[:, 0], data[:, 2]
alpha, Top_Xtr = data[:, 0], data[:, 5]

plt.plot(alpha, Top_Xtr, label = "NACA1611")

plt.xlabel("AoA")
plt.ylabel("x/c transition")
plt.legend()

# Save using the complete file path with high resolution and no cropped borders
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()