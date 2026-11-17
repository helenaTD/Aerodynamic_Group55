import matplotlib.pyplot as plt
import numpy as np
import os

base = r"C:\Users\helen\Downloads\TU_DELFT\MSc_FPP\Q1\AircraftAerodynamics\aa_repo\Aerodynamic_Group55"

inputs = [os.path.join(base, "NACA1611.dat"),
          os.path.join(base, "Viscous_flows", "Redesign", "1611_opt.dat")]
labels_to_use = ["NACA 1611 (original)", "Optimised (MDES)"]
styles = ["-", "--"]

figures_dir = os.path.join(base, "figures")
os.makedirs(figures_dir, exist_ok=True)
save_path = os.path.join(figures_dir, "3.2.7_shape.png")

plt.figure(figsize=(9, 3))

for i, file_path in enumerate(inputs):
    data = np.loadtxt(file_path, skiprows=1)   # first line is the airfoil name
    plt.plot(data[:, 0], data[:, 1], linestyle=styles[i], color=f'C{i}', label=labels_to_use[i])

plt.gca().set_aspect('equal')   # true shape, no vertical stretching
plt.xlabel("x/c")
plt.ylabel("y/c")
plt.legend()
plt.grid(True, linewidth=0.4, alpha=0.6)

plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()