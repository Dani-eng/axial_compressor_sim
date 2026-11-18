import math

from .models import StageInputs, StageResults


# Approximate properties of air near room temperature.
CP_AIR_J_KG_K = 1005.0
GAMMA_AIR = 1.4


def calculate_stage(inputs: StageInputs) -> StageResults:
    """Estimate one idealized stage; this is an educational model."""
    if inputs.inlet_temperature_k <= 0:
        raise ValueError("Inlet temperature must be positive.")
    if inputs.inlet_pressure_pa <= 0:
        raise ValueError("Inlet pressure must be positive.")
    if inputs.mass_flow_kg_s <= 0:
        raise ValueError("Mass flow must be positive.")
    if inputs.rotational_speed_rpm <= 0 or inputs.mean_radius_m <= 0:
        raise ValueError("Rotational speed and mean radius must be positive.")
    if inputs.axial_velocity_m_s <= 0:
        raise ValueError("Axial velocity must be positive.")
    if inputs.target_pressure_ratio <= 1:
        raise ValueError("Target pressure ratio must be greater than 1.")
    if not 0 < inputs.stage_efficiency <= 1:
        raise ValueError("Stage efficiency must be in the range (0, 1].")

    # Total-to-total temperature estimate from pressure ratio and efficiency.
    exponent = (GAMMA_AIR - 1.0) / GAMMA_AIR
    ideal_temperature_rise = inputs.inlet_temperature_k * (
        inputs.target_pressure_ratio**exponent - 1.0
    )
    actual_temperature_rise = ideal_temperature_rise / inputs.stage_efficiency
    outlet_temperature = inputs.inlet_temperature_k + actual_temperature_rise

    # Euler work, assuming zero inlet swirl: work = U * (Ctheta2 - Ctheta1).
    blade_speed = 2.0 * math.pi * inputs.mean_radius_m * inputs.rotational_speed_rpm / 60.0
    specific_work = CP_AIR_J_KG_K * actual_temperature_rise
    outlet_tangential_velocity = specific_work / blade_speed

    inlet_angle = 0.0  # Inlet flow is assumed purely axial.
    outlet_angle = math.degrees(
        math.atan2(outlet_tangential_velocity, inputs.axial_velocity_m_s)
    )

    return StageResults(
        blade_speed_m_s=blade_speed,
        outlet_temperature_k=outlet_temperature,
        specific_work_j_kg=specific_work,
        outlet_tangential_velocity_m_s=outlet_tangential_velocity,
        inlet_flow_angle_deg=inlet_angle,
        outlet_flow_angle_deg=outlet_angle,
    )
