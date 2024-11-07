import numpy as np
from setup import *

def model_setup():
    time_record = np.arange(0, total_time+dt, dt)
    L = Thickness/2
    cells_list = np.arange(-L,L+dx/2,dx) # positions of discretised cells in model
    cells_temperatures_init = np.zeros(len(cells_list))+Temperature_initial # initial list of cell temperatures
    return time_record, cells_list, cells_temperatures_init

def calculate_heat_loss(cell_temperature):
    heat_loss = (cell_temperature - Temperature_ambient)*Heat_loss_heat_transfer_coefficient
    return(heat_loss)

def time_step_calc(cells_list, prev_temperatures_list):
    system_total_q = 0
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
        #### EGEN FUNCTION HERE
        # calculating heat input: add heat gen, heat from peltier (for border cells), and subtract heat loss
        heat_loss = calculate_heat_loss(prev_temperatures_list[cell_index])
        if cell_index == 0:
            egen = ((Total_heat_gen)/Thickness - heat_loss)*dx + Heat_flux_left # heat gen minus heat loss multiplied by dx to get discretised value, plus heat flux in
            system_total_q + egen
        elif cell_index == range(len(cells_list))[-1]:
            egen = ((Total_heat_gen)/Thickness - heat_loss)*dx + Heat_flux_right
            system_total_q + egen
        else:
            egen = ((Total_heat_gen)/Thickness - heat_loss)*dx
            system_total_q + egen
        dTdt_list[cell_index] = alpha*(d2Tdx2_list[cell_index]+egen/k)
        # dTdt_list[0] = 0; dTdt_list[-1] = 0 # commented out because this is only used for setting constant surface temperature
        new_temperature_list[cell_index] = prev_temperatures_list[cell_index] + dTdt_list[cell_index]*dt
    # print("Time step total system q: "+str(system_total_q))
    return new_temperature_list

def run_model(time_record, cells_list, cells_temperatures_init):
    temperatures = [[] for _ in time_record]
    temperatures[0] = cells_temperatures_init; # temperatures[0][0] = Temperature_side_minusL; temperatures[0][-1] = Temperature_side_plusL # set end boundaries to defined temperatures
    for time_index, time in enumerate(time_record):
        if time_index == 0:
            continue # do nothing at zeroth time step
        temperatures[time_index] = time_step_calc(cells_list = cells_list, prev_temperatures_list = temperatures[time_index-1])
    return temperatures
        

