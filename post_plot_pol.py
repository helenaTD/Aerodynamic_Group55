import os

import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INV_DIR = os.path.join(BASE_DIR, "Inviscid_flows")
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def read_polar(path):
    """Read an XFOIL polar file (PACC). Data starts after the '-----' line.
    Sorted by alpha, duplicate alphas removed (e.g. two sweeps from 0 deg)."""
    with open(path) as f:
        lines = f.readlines()
    start = next(i for i, line in enumerate(lines) if line.strip().startswith("---")) + 1
    data = np.loadtxt(lines[start:])
    data = data[np.argsort(data[:, 0])]
    _, keep = np.unique(data[:, 0], return_index=True)
    data = data[keep]
    names = ["alpha", "CL", "CD", "CDp", "CM", "Top_Xtr", "Bot_Xtr"]
    return {name: data[:, i] for i, name in enumerate(names)}


def plot_cl_cm(cases, title, filename):
    """Cl-alpha and Cm-alpha side by side. cases: list of (file path, label)."""
    fig, (ax_cl, ax_cm) = plt.subplots(1, 2, figsize=(10, 4.2))

    for path, label in cases:
        pol = read_polar(path)
        ax_cl.plot(pol["alpha"], pol["CL"], marker="o", markersize=3, label=label)
        ax_cm.plot(pol["alpha"], pol["CM"], marker="o", markersize=3, label=label)

    ax_cl.set_ylabel(r"$Cl$ [-]")
    ax_cm.set_ylabel(r"$C_{m,c/4}$ [-]")
    for ax in (ax_cl, ax_cm):
        ax.set_xlabel(r"$\alpha$ [deg]")
        ax.axhline(0, color="black", linewidth=0.6)
        ax.axvline(0, color="black", linewidth=0.6)
        ax.grid(True, linewidth=0.4, alpha=0.6)
        ax.legend(fontsize=9)
    fig.suptitle(title)
    fig.tight_layout()

    
    fig.savefig(os.path.join(FIG_DIR, f"{filename}.png"), dpi=300)


if __name__ == "__main__":
    cases = [
        (os.path.join(INV_DIR, "pol_1611_inv.txt"), "NACA 1611"),
        (os.path.join(INV_DIR, "pol_0011_inv.txt"), "NACA 0011"),
    ]
    plot_cl_cm(cases, "Inviscid polars", "polar_inviscid_1611_0011")
    plt.show()