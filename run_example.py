import json
from pathlib import Path

from compressor_sim.calculations import calculate_stage
from compressor_sim.models import StageInputs


def main():
    project_root = Path(__file__).parent
    input_path = project_root / "examples" / "baseline.json"

    data = json.loads(input_path.read_text(encoding="utf-8"))
    inputs = StageInputs(**data)
    results = calculate_stage(inputs)

    print("Educational single-stage estimate")
    print(f"Blade speed:                {results.blade_speed_m_s:.1f} m/s")
    print(f"Outlet temperature:         {results.outlet_temperature_k:.1f} K")
    print(f"Specific work:              {results.specific_work_j_kg:.1f} J/kg")
    print(
        "Outlet tangential velocity: "
        f"{results.outlet_tangential_velocity_m_s:.1f} m/s"
    )
    print(f"Inlet flow angle:           {results.inlet_flow_angle_deg:.1f} degrees")
    print(f"Outlet flow angle:          {results.outlet_flow_angle_deg:.1f} degrees")
    print("\nApproximate educational estimate—not validated design data.")


if __name__ == "__main__":
    main()
