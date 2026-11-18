import matplotlib.pyplot as plt

from .models import StageInputs, StageResults


def plot_velocity_triangles(inputs: StageInputs, results: StageResults) -> None:
    """Plot simplified inlet and outlet absolute-velocity vectors."""
    axial = inputs.axial_velocity_m_s
    inlet_swirl = 0.0  # Assumed axial-only inlet flow.
    outlet_swirl = results.outlet_tangential_velocity_m_s

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    for ax, title, swirl in (
        (axes[0], "Inlet velocity", inlet_swirl),
        (axes[1], "Outlet velocity", outlet_swirl),
    ):
        ax.quiver(
            0, 0, axial, swirl,
            angles="xy", scale_units="xy", scale=1,
            color="tab:blue",
        )
        ax.set_title(title)
        ax.set_xlabel("Axial velocity (m/s)")
        ax.set_ylabel("Tangential velocity (m/s)")
        ax.set_xlim(0, max(axial, outlet_swirl) * 1.2)
        ax.set_ylim(-10, max(outlet_swirl, 10) * 1.2)
        ax.grid(True)
        ax.set_aspect("equal", adjustable="box")

    fig.suptitle("Simplified velocity vectors—not validated design data")
    fig.tight_layout()
    plt.show()
    
def plot_stage_changes(inputs: StageInputs, results: StageResults) -> None:
    """Plot inlet and estimated outlet pressure and temperature."""
    pressures = [
        inputs.inlet_pressure_pa / 1000,
        inputs.inlet_pressure_pa * inputs.target_pressure_ratio / 1000,
    ]
    temperatures = [
        inputs.inlet_temperature_k,
        results.outlet_temperature_k,
    ]
    positions = [0, 1]
    labels = ["Inlet", "Outlet"]

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))

    axes[0].bar(positions, pressures, color="tab:blue")
    axes[0].set_title("Pressure")
    axes[0].set_ylabel("Pressure (kPa)")
    axes[0].set_xticks(positions, labels)
    axes[0].grid(axis="y", alpha=0.3)

    axes[1].bar(positions, temperatures, color="tab:orange")
    axes[1].set_title("Temperature")
    axes[1].set_ylabel("Temperature (K)")
    axes[1].set_xticks(positions, labels)
    axes[1].grid(axis="y", alpha=0.3)

    fig.suptitle("Estimated single-stage changes—not validated design data")
    fig.tight_layout()
    plt.show()