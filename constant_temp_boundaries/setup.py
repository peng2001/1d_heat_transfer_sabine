import toml
import numpy as np

config_file = "constant_temp_boundaries/config.toml"
with open(config_file, 'r') as f:
    inputs = toml.load(f)

dt = np.float64(inputs["dt"])
total_time = np.float64(inputs["total_time"])
n = inputs["n"]
Thickness = np.float64(inputs["Thickness"])
dx = np.float64(Thickness/n)
Specific_heat = np.float64(inputs["Specific_heat"])
Conductivity = np.float64(inputs["Conductivity"])
Density = np.float64(inputs["Density"])
Thickness_interface = np.float64(inputs["Thermal_Interface_Thickness"])
Conductivity_interface = np.float64(inputs["Thermal_Interface_Conductivity"])
Density_interface = np.float64(inputs["Thermal_Interface_Density"])
Specific_heat_interface = np.float64(inputs["Thermal_Interface_Specific_heat"])
Temperature_initial = np.float64(inputs["Temperature_initial"]+273.15)
Temperature_left = np.float64(inputs["Temperature_left"]+273.15)
Temperature_right = np.float64(inputs["Temperature_right"]+273.15)
Total_heat_gen = np.float64(inputs["Total_heat_gen"])
Heat_loss_heat_transfer_coefficient = np.float64(inputs["Heat_loss_heat_transfer_coefficient"])
Temperature_ambient = np.float64(inputs["Temperature_ambient"]+273.15)