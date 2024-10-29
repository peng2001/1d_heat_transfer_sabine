import numpy as np
from sympy import symbols, Eq, solve
from cell import Cell

def model_setup(dx, thickness):
    L = thickness/2
    cell_positions = np.arange(-L,L+dx/2,dx) # positions of discretised cells in model
    cell_list = []
    cell_unknown_T_list = []
    for cell_position in cell_positions:
        symbolT_name = "T_"+str(cell_position)
        cell_list.append(Cell(x=cell_position, T=None, q=None, symbolT = symbols(symbolT_name)))
        cell_unknown_T_list.append
    return cell_list

def run_model(cell_list, k, dx, T_amb):
    for i, cell in enumerate(cell_list):
        if i == 0:
            cellL = None
            cellR = cell_list[i+1]
        elif i == len(cell_list)-1:
            cellL = cell_list[i-1]
            cellR = None
        else:
            cellL = cell_list[i-1]
            cellR = cell_list[i+1]
        cell_heat_calc(cell=cell, cell_index=i, cellL=cellL, cellR=cellR, k=k, dx=dx, cell_list_length=len(cell_list), T_amb=T_amb)

def cell_heat_calc(cell, cell_index, cellL, cellR, k, dx, cell_list_length, T_amb):
    const = k/dx
    if cell_index == 0:
        qL = 10*T_amb - 10*cell.symbolT
        qR = const*cell.symbolT - const*cellR.symbolT
    elif cell_index == cell_list_length-1:
        qL = const*cellL.symbolT - const*cell.symbolT
        qR = 10*cell.symbolT - 10*T_amb
    else:
        qL = const*cellL.symbolT - const*cell.symbolT
        qR = const*cell.symbolT - const*cellR.symbolT
    cell.q = qL + qR