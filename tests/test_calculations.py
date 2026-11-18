import pytest

from compressor_sim.calculations import calculate_stage
from compressor_sim.models import StageInputs


def baseline_inputs() -> StageInputs:
    return StageInputs(
        inlet_temperature_k=288.15,
        inlet_pressure_pa=101325.0,
        mass_flow_kg_s=10.0,
        rotational_speed_rpm=12000.0,
        target_pressure_ratio=1.2,
        mean_radius_m=0.25,
        axial_velocity_m_s=150.0,
        stage_efficiency=0.85,
    )


def test_calculate_stage_returns_positive_values():
    result = calculate_stage(baseline_inputs())

    assert result.blade_speed_m_s > 0
    assert result.outlet_temperature_k > 288.15
    assert result.specific_work_j_kg > 0
    assert result.outlet_tangential_velocity_m_s > 0


def test_pressure_ratio_must_be_greater_than_one():
    inputs = baseline_inputs()
    inputs.target_pressure_ratio = 1.0

    with pytest.raises(ValueError, match="pressure ratio"):
        calculate_stage(inputs)
