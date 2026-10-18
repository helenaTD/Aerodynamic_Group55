import matplotlib.pyplot as plt
import numpy as np
import os


inputs = [
    "cp_1611_a10_inv.txt",
    "cp_1622_a10_inv.txt"
]

path = r"C:\Users\david\Desktop\Uni\Aircraft Aereodynamics\Aerodynamic_Group55\Inviscid_flows"
figures_dir = r"C:\Users\david\Desktop\Uni\Aircraft Aereodynamics\Aerodynamic_Group55\figures"

# Ensure the figures directory exists
os.makedirs(figures_dir, exist_ok=True)

# Combine directory and filename for saving
save_path = os.path.join(figures_dir, "3.1.3.png")

labels_to_use = ["NACA 1611", "NACA1622", "AoA: 10"]

def read_cp(file_path):
    """Split XFOIL data at the leading edge (minimum x) to avoid gaps."""
    data = np.loadtxt(file_path, skiprows=3)
    x, cp = data[:, 0], data[:, 2]
    i_le = np.argmin(x)
    return x[: i_le + 1], cp[: i_le + 1], x[i_le:], cp[i_le:]

for i, files in enumerate(inputs):
    file_path = os.path.join(path, files)
    xu, cpu, xl, cpl = read_cp(file_path)
    
    plt.plot(xu, cpu, linestyle='-', color=f'C{i}', label=labels_to_use[i])
    plt.plot(xl, cpl, linestyle='--', color=f'C{i}')

plt.gca().invert_yaxis()

plt.xlabel("x")
plt.ylabel("Cp")
plt.legend()
plt.gca().axhline(0, color='black', linewidth=0.8, linestyle='--')

# Save using the complete file path with high resolution and no cropped borders
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()