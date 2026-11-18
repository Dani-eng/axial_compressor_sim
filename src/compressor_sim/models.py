from dataclasses import dataclass


@dataclass
class StageInputs:
    inlet_temperature_k: float
    inlet_pressure_pa: float
    mass_flow_kg_s: float
    rotational_speed_rpm: float
    target_pressure_ratio: float
    mean_radius_m: float
    axial_velocity_m_s: float
    stage_efficiency: float = 0.85


@dataclass
class StageResults:
    blade_speed_m_s: float
    outlet_temperature_k: float
    specific_work_j_kg: float
    outlet_tangential_velocity_m_s: float
    inlet_flow_angle_deg: float
    outlet_flow_angle_deg: float
