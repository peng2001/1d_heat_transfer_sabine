import numpy as np
from import_config import *

def model_setup():
    time_record = np.arange(0, total_time+dt, dt)
    L = Thickness/2
    cells_list = np.arange(-L,L+dx/2,dx) # positions of discretised cells in model
    print(cells_list)
    cells_temperatures_init = np.zeros(len(cells_list))+Temperature_initial # initial list of cell temperatures
    return time_record, cells_list, cells_temperatures_init

def run_model(time_record, cells_list, cells_temperatures_init):
    temperatures = [[] for _ in time_record]
    temperatures[0] = cells_temperatures_init; temperatures[0][0] = Temperature_side_minusL; temperatures[0][-1] = Temperature_side_plusL # set end boundaries to defined temperatures
    for time_index, time in enumerate(time_record):
        if time_index == 0:
            continue # do nothing at zeroth time step
        temperatures[time_index] = time_step_calc(cells_list = cells_list, prev_temperatures_list = temperatures[time_index-1])
    return temperatures

def calculate_heat_in_peltier():
    print("yo")

def time_step_calc(cells_list, prev_temperatures_list):
    # Equation: dT/dt = alpha * (d2T/dx2 + egen/k)
    k = Conductivity*1000 # convert conductivity to W/(mm*K) to use mm in calculations, because using m in calculations was causing errors
    dTdt_list = np.zeros(len(cells_list)) # initialise as zeros first
    new_temperature_list = np.zeros(len(cells_list))
    dTdx_list = np.zeros(len(cells_list))
    d2Tdx2_list = np.zeros(len(cells_list))
    alpha = k/(Density*Specific_heat) # thermal diffusivity
    # First, calculate all dT/dx
    # forward difference for discretising derivative at left bounds
    dTdx_list[0] = (prev_temperatures_list[1] - prev_temperatures_list[0])/dx
    # backward difference for discretising derivative at right bounds
    dTdx_list[-1] = (prev_temperatures_list[-1] - prev_temperatures_list[-2])/dx
    for cell_index, cell_location in enumerate(cells_list):
        if cell_index == 0 or cell_index == range(len(cells_list))[-1]:
            continue
        # central difference for discretising derivative
        dTdx_list[cell_index] = ((prev_temperatures_list[cell_index+1]-prev_temperatures_list[cell_index])/dx + (prev_temperatures_list[cell_index]-prev_temperatures_list[cell_index-1])/dx)/2
    # Next, calculate all d2T/dx2
    # Using calculated dT/dx values, calculate d2T/dx2 at previous time step for all points.
    # forward difference for discretising derivative at left bounds
    d2Tdx2_list[0] = (dTdx_list[1] - dTdx_list[0])/dx
    # backward difference for discretising derivative at right bounds
    d2Tdx2_list[-1] = (dTdx_list[-1] - dTdx_list[-2])/dx
    for cell_index, cell_location in enumerate(cells_list):
        if cell_index == 0 or cell_index == range(len(cells_list))[-1]:
            continue
        # central difference for discretising derivative
        d2Tdx2_list[cell_index] = ((dTdx_list[cell_index+1]-dTdx_list[cell_index])/dx + (dTdx_list[cell_index]-dTdx_list[cell_index-1])/dx)/2
    # Finally, calculate dT/dt and the new temperatures
    for cell_index, cell_location in enumerate(cells_list):
        dTdt_list[cell_index] = alpha*(d2Tdx2_list[cell_index]+Heat_gen/k)
        dTdt_list[0] = 0; dTdt_list[-1] = 0
        new_temperature_list[cell_index] = prev_temperatures_list[cell_index] + dTdt_list[cell_index]*dt
    return new_temperature_list

        
        

