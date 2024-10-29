import toml
import model_steady_state
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve

def config_import(): 
    config_file = "config.toml"
    with open(config_file, 'r') as f:
        inputs = toml.load(f)
    return inputs

# def graphing_3d(temperatures_list, time_record, cells_list):
#     x = np.array(cells_list)
#     t = np.array(time_record)
#     temperature_data = np.array(temperatures_list)
#     x, t = np.meshgrid(x, t)
#     # Flatten the data for plotting
#     # Plotting the data
#     fig, ax = plt.subplots()
#     ax.plot(x[-1], temperature_data[-1])
#     # Adding axis labels
#     ax.set_xlabel('x (m)')
#     ax.set_ylabel('Temperature (Degrees C)')
#     ax.set_title('1D Temperature')
#     plt.show()


# if __name__ == "__main__":
#     inputs = config_import()
#     time_record, cells_list, cells_temperatures_init = model.model_setup(dx = inputs["dx"], dt = 5, total_time = 100000, temperature_initial = inputs["Temperature_initial"]+273.15, thickness = inputs["Thickness"])
#     temperatures = model.run_model(time_record=time_record, cells_list=cells_list, cells_temperatures_init=cells_temperatures_init,
#                                     Temperature_side_minusL=inputs["Temperature_side_minusL"]+273.15, Temperature_side_plusL=inputs["Temperature_side_plusL"]+273.15, 
#                                     dt=inputs["dt"], dx=inputs["dx"], Heat_gen=inputs["Heat_gen"], k=inputs["Conductivity"], rho=inputs["Density"], cp=inputs["Specific_heat"])
#     temperatures_C = [[value - 273.15 for value in sublist] for sublist in temperatures] # subtract 273.15 from all points to convert to deg C
#     print("Avg final temperature: "+str(round(np.mean(temperatures_C[-1]), 4))+" Degrees C")
#     print("Max final temperature: "+str(round(max(temperatures_C[-1]), 4))+" Degrees C")
#     print("Min final temperature: "+str(round(min(temperatures_C[-1]), 4))+" Degrees C")
#     graphing_3d(temperatures_C, time_record, cells_list)

if __name__ == "__main__":
    inputs = config_import()
    cell_list = model_steady_state.model_setup(dx=inputs["dx"], thickness=inputs["Thickness"])
    model_steady_state.setup_equations(cell_list=cell_list, k=inputs["Conductivity"], dx=inputs["dx"], T_amb=inputs["Temperature_ambient"]+273.15)
    solution = model_steady_state.solve_equations(cell_list)
    print(solution)
    # for key in solution:
    #     if key == "T_0.1":
    #         print("AAAAAAAAA")
    #     print(key)
    # for cell in cell_list:
    #     print(cell.x)