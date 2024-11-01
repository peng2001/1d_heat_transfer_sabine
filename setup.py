import toml

config_file = "config.toml"
with open(config_file, 'r') as f:
    inputs = toml.load(f)

dt = inputs["dt"]
total_time = inputs["total_time"]
dx = inputs["dx"]
Thickness = inputs["Thickness"]
Specific_heat = inputs["Specific_heat"]
Conductivity = inputs["Conductivity"]
Density = inputs["Density"]
Temperature_initial = inputs["Temperature_initial"]+273.15
Heat_flux_left = inputs["Heat_flux_left"]
Heat_flux_right = inputs["Heat_flux_right"]
Heat_gen = inputs["Heat_gen"]
Total_heat_loss = inputs["Total_heat_loss"]
Temperature_ambient = inputs["Temperature_ambient"]+273.15