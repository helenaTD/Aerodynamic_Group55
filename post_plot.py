import os
from itertools import cycle

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

    for (path, label), color in zip(cases, cycle(colors)):
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

    fig.savefig(os.path.join(FIG_DIR, f"{filename}.png"), dpi=300)
    plt.show()


def make_cases(filenames):
    """Build plot cases from filenames in the inviscid data directory."""
    return [
        (os.path.join(INV_DIR, name), os.path.splitext(name)[0])
        for name in filenames
    ]


if __name__ == "__main__":
    # Add or remove filenames here to choose which cases are plotted together.
    files_to_plot = [
        "cp_1622_a10_inv.txt",
        "cp_1611_a10_inv.txt"
    ]

    plot_cp(
        make_cases(files_to_plot),
        "Inviscid pressure coefficient",
        "cp_inviscid_comparison",
    )
