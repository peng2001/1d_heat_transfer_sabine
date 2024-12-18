import model
import matplotlib.pyplot as plt
from setup import *

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
    ax.set_ylabel('Steady State Temperature (Degres C)')
    ax.set_title('1D Temperature')
    plt.show()

def graphing_transient(temperatures_list, time_record, cells_list):
    x = np.array(cells_list)
    t = np.array(time_record)
    temperature_data = np.array(temperatures_list)
    x, t = np.meshgrid(x, t)
    # Flatten the data for plotting
    # Plotting the data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, t, temperature_data, cmap='viridis')
    # Adding axis labels
    ax.set_xlabel('x (m)')
    ax.set_ylabel('Time (s)')
    ax.set_zlabel('Temperature (Degrees C)')
    ax.set_title('1D Temperature')
    plt.show()

def graphing_transient_2D(temperatures_list, time_record, cells_list): # graphs temperature over time of one x=-L surface
    x = np.array(cells_list)
    t = np.array(time_record)
    temperature_data = np.array(temperatures_list)
    left_surface_temperature = [sublist[0] for sublist in temperature_data]
    # Plotting the data
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(t, left_surface_temperature)
    # Adding axis labels
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (Degrees C)')
    ax.set_title('Temperature of Left Surface of Cell')
    plt.show()

def calculate_max_dTdt(temperatures_list):
    # calculates dT/dt at centre of model to make sure that steady state is reached
    dTdt_list = []
    for index, cell in enumerate(temperatures_list[0]):
        dTdt = (temperatures_list[-1][index] - temperatures_list[-2][index])/dt
        dTdt_list.append(dTdt)
    return max(dTdt_list)
        
if __name__ == "__main__":
    time_record, cells_list, cells_temperatures_init = model.model_setup()
    temperatures = model.run_model(time_record=time_record, cells_list=cells_list, cells_temperatures_init=cells_temperatures_init)
    temperatures_C = [[value - 273.15 for value in sublist] for sublist in temperatures] # subtract 273.15 from all points to convert to deg C
    print("Avg final temperature: "+str(round(np.mean(temperatures_C[-1]), 4))+" Degrees C")
    print("Max final temperature: "+str(round(max(temperatures_C[-1]), 4))+" Degrees C")
    print("Min final temperature: "+str(round(min(temperatures_C[-1]), 4))+" Degrees C")
    max_dTdt = calculate_max_dTdt(temperatures_list=temperatures_C)
    print("Max final dT/dt (should be very small to reach steady state): "+str(max_dTdt)) # should be very small; otherwise increase simulation time
    if max_dTdt > 0.00001:
        print("Steady state not reached, try increasing simulation time")
    graphing_steady_state(temperatures_C, time_record, cells_list)
    # graphing_transient(temperatures_C, time_record, cells_list)
    graphing_transient_2D(temperatures_C, time_record, cells_list)
