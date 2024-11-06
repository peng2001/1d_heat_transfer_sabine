from model import *
        
def thermal_interface_model_setup():
    time_record = np.arange(0, total_time+dt, dt)
    L = Thickness/2
    thermal_interface_cells_list_L = np.arange(-L-Thickness_interface,-L,dx) # positions of discretised cells in model
    thermal_interface_cells_list_R = np.arange(L, L+Thickness_interface,dx)
    print(thermal_interface_cells_list_L)
    print(thermal_interface_cells_list_R)
    thermal_interface_cells_temperatures_init_L = np.zeros(len(thermal_interface_cells_list_L))+Temperature_initial # initial list of cell temperatures
    thermal_interface_cells_temperatures_init_R = np.zeros(len(thermal_interface_cells_list_R))+Temperature_initial
    return time_record, thermal_interface_cells_list_L, thermal_interface_cells_temperatures_init_L, thermal_interface_cells_list_R, thermal_interface_cells_temperatures_init_R

thermal_interface_model_setup()