import os

import matplotlib.pyplot as plt
import numpy as np

# Folders are found relative to this script, so it runs from anywhere
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INV_DIR = os.path.join(BASE_DIR, "Inviscid_flows")
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def read_cp(path):
    """Read an XFOIL CPWR file (3 header lines, columns x, y, Cp).

    XFOIL lists points from the trailing edge over the upper surface to the
    leading edge, then back along the lower surface. Split at minimum x.
    Returns (x_upper, cp_upper, x_lower, cp_lower).
    """
    data = np.loadtxt(path, skiprows=3)
    x, cp = data[:, 0], data[:, 2]
    i_le = np.argmin(x)
    return x[: i_le + 1], cp[: i_le + 1], x[i_le:], cp[i_le:]


def plot_cp(cases, title, filename):
    """cases: list of (file path, legend label)."""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    for (path, label), color in zip(cases, colors):
        xu, cpu, xl, cpl = read_cp(path)
        ax.plot(xu, cpu, color=color, linestyle="-", label=f"{label}, upper")
        ax.plot(xl, cpl, color=color, linestyle="--", label=f"{label}, lower")

    ax.invert_yaxis()  # suction (negative Cp) upward
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_xlim(0, 1)
    ax.set_xlabel("x/c [-]")
    ax.set_ylabel(r"Cp [-]")
    ax.set_title(title)
    ax.grid(True, linewidth=0.4, alpha=0.6)
    ax.legend(fontsize=9, ncol=2)
    fig.tight_layout()

    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG_DIR, f"{filename}.{ext}"), dpi=300)
    plt.show()


if __name__ == "__main__":
    # 3.1.2 - inviscid Cp of NACA 1611 at 0, 5 and 10 deg
    cases_312 = [
        (os.path.join(INV_DIR, f"cp_1611_a{a}_inv.txt"), rf"$\alpha$ = {a}°")
        for a in (0, 5, 10)
    ]
    plot_cp(cases_312, "NACA 1611, inviscid", "cp_1611_inviscid_a0_5_10")
