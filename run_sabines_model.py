import toml
import model
import matplotlib.pyplot as plt
import numpy as np

def config_import(): 
    config_file = "config.toml"
    with open(config_file, 'r') as f:
        inputs = toml.load(f)
    return inputs

def graphing_steady_state(temperatures_list, time_record, cells_list):
    x = np.array(cells_list)
    t = np.array(time_record)
    temperature_data = np.array(temperatures_list)
    x, t = np.meshgrid(x, t)
    # Flatten the data for plotting
    # Plotting the data
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x[-1], temperature_data[-1])
    # Adding axis labels
    ax.set_xlabel('x (mm)')
    ax.set_ylabel('Temperature (Degres C)')
    ax.set_title('1D Temperature')
    plt.show()


if __name__ == "__main__":
    inputs = config_import()
    dx_precise = np.float64(inputs["dx"])
    k_mm = inputs["Conductivity"]*1000 # convert conductivity to W/(mm*K) to use mm in calculations, because using m in calculations was causing errors
    time_record, cells_list, cells_temperatures_init = model.model_setup(dx = dx_precise, dt = inputs["dt"], total_time = inputs["total_time"], temperature_initial = inputs["Temperature_initial"]+273.15, thickness = inputs["Thickness"])
    temperatures = model.run_model(time_record=time_record, cells_list=cells_list, cells_temperatures_init=cells_temperatures_init,
                                    Temperature_side_minusL=inputs["Temperature_side_minusL"]+273.15, Temperature_side_plusL=inputs["Temperature_side_plusL"]+273.15, 
                                    dt=inputs["dt"], dx=dx_precise, Heat_flux=inputs["Heat_flux"], k=k_mm, rho=inputs["Density"], cp=inputs["Specific_heat"])
    temperatures_C = [[value - 273.15 for value in sublist] for sublist in temperatures] # subtract 273.15 from all points to convert to deg C
    print("Avg final temperature: "+str(round(np.mean(temperatures_C[-1]), 4))+" Degrees C")
    print("Max final temperature: "+str(round(max(temperatures_C[-1]), 4))+" Degrees C")
    print("Min final temperature: "+str(round(min(temperatures_C[-1]), 4))+" Degrees C")
    graphing_steady_state(temperatures_C, time_record, cells_list)
