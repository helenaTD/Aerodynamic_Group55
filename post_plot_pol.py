import matplotlib.pyplot as plt
import numpy as np
import os


#inputs = ["pol_1611_inv.txt", "pol_1622_inv.txt"]
#inputs = ["pol_1611_N10_inv.txt", "pol_1611_N50_inv.txt", "pol_1611_N250_inv.txt"]
#inputs = ["pol_1611_inv.txt", "pol_0011_inv.txt"]
inputs = ["pol_1611_Re1.5e6.txt", "pol_1611_inv.txt"]

#labels_to_use = ["NACA1611", "NACA1622"]
#labels_to_use = ["N = 10", "N = 50", "N = 250"]
#labels_to_use = ["NACA1611", "NACA0011"]
labels_to_use = ["NACA 1611 Visc", "NACA 1611 Invisc"]

path_i = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inviscid_flows")
path_v = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Viscous_flows")
figures_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figures_dir, exist_ok=True)

save_path = os.path.join(figures_dir, "3.2.3_polars.png")         
save_path_drag = os.path.join(figures_dir, "3.2.3_drag_polar.png")  

def read_polar(file_path):
    # skip the XFOIL header, columns: alpha, CL, CD, CDp, CM, Top_Xtr, Bot_Xtr
    data = np.loadtxt(file_path, skiprows=12)
    data= data[np.argsort(data[:,0])]
    return data[:, 0], data[:, 1], data[:, 2], data[:, 4]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
fig2, ax3 = plt.subplots(figsize=(5, 4))  

for i, files in enumerate(inputs):
    if files.endswith("inv.txt"):
        file_path = os.path.join(path_i, files)
    else:
        file_path = os.path.join(path_v, files)
    alpha, cl, cd, cm = read_polar(file_path)

    ax1.plot(alpha, cl, markersize=3, color=f'C{i}', label=labels_to_use[i])
    ax2.plot(alpha, cm, markersize=3, color=f'C{i}', label=labels_to_use[i])
    ax3.plot(cd, cl, color=f'C{i}', label=labels_to_use[i])

ax1.set_xlabel("alpha [deg]")
ax1.set_ylabel("Cl")
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax1.legend()

ax2.set_xlabel("alpha [deg]")
ax2.set_ylabel("Cm c/4")
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax2.legend()

ax3.set_xlabel("Cd")                                       
ax3.set_ylabel("Cl")                                        
ax3.axhline(0, color='black', linewidth=0.8, linestyle='--')  
ax3.legend()                                                

fig.savefig(save_path, dpi=300, bbox_inches='tight')        
fig2.savefig(save_path_drag, dpi=300, bbox_inches='tight')  
plt.show()