import matplotlib.pyplot as plt
import numpy as np
import os


#inputs = ["pol_1611_inv.txt", "pol_1622_inv.txt"]
#inputs = ["pol_1611_N10_inv.txt", "pol_1611_N50_inv.txt", "pol_1611_N250_inv.txt"]
inputs = ["pol_1611_inv.txt", "pol_0011_inv.txt"]

#labels_to_use = ["NACA1611", "NACA1622"]
#labels_to_use = ["N = 10", "N = 50", "N = 250"]
labels_to_use = ["NACA1611", "NACA0011"]

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inviscid_flows")
figures_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figures_dir, exist_ok=True)

save_path = os.path.join(figures_dir, "3.1.5_polars.png")

def read_polar(file_path):
    # skip the XFOIL header, columns: alpha, CL, CD, CDp, CM, Top_Xtr, Bot_Xtr
    data = np.loadtxt(file_path, skiprows=12)
    return data[:, 0], data[:, 1], data[:, 4]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

for i, files in enumerate(inputs):
    file_path = os.path.join(path, files)
    alpha, cl, cm = read_polar(file_path)

    ax1.plot(alpha, cl, markersize=3, color=f'C{i}', label=labels_to_use[i])
    ax2.plot(alpha, cm, markersize=3, color=f'C{i}', label=labels_to_use[i])

ax1.set_xlabel("alpha [deg]")
ax1.set_ylabel("Cl")
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax1.legend()

ax2.set_xlabel("alpha [deg]")
ax2.set_ylabel("Cm c/4")
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax2.legend()

plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()