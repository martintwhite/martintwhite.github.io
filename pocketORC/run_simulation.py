from js import document
from pyodide import create_proxy 
import thermo_props
import orc_simulator
import matplotlib.pyplot as plt
import numpy as np
 
def _simulate_cycle(*args, **kwargs):

    # setup fluid:
    currentFluid = document.getElementById("working-fluid-select").value
    if currentFluid == "n-pentane":
        tc = 438
        pc = 2480000
        om = 0.441774
        cp = [ 10.4923, 0.6569, -4.13e-4 ]
        wm = 72.1488
    fluid = thermo_props.pr_fluid(currentFluid,tc,pc,om,cp,300,0.01,wm)
    
    # get heat-source conditions:
    hot = [0,0,0]
    hot[0] = float(document.getElementById("heat-source-temperature").value)
    hot[1] = float(document.getElementById("heat-source-mass-flow").value)
    hot[2] = float(document.getElementById("heat-source-heat-capacity").value)
    
    # get heat-sink conditions:
    cld = [0,0,0]
    cld[0] = float(document.getElementById("heat-sink-temperature").value)
    cld[1] = float(document.getElementById("heat-sink-mass-flow").value)
    cld[2] = float(document.getElementById("heat-sink-heat-capacity").value)

    # get component efficiencies:
    eta = [0,0]
    eta[0] = float(document.getElementById("pump-efficiency").value)/100
    eta[1] = float(document.getElementById("turbine-efficiency").value)/100

    # get cycle variables:
    x = [0,0,0,0,0,0]
    x[0] = float(document.getElementById("condensation-temperature").value)
    x[1] = float(document.getElementById("pump-subcooling").value)
    x[2] = float(document.getElementById("pressure-ratio").value)
    x[3] = float(document.getElementById("expander-inlet").value)
    x[4] = float(document.getElementById("recuperator-effectiveness").value)/100
    x[5] = float(document.getElementById("heat-source-outlet").value)

    # heat exchanger discretisation (not user defined):
    n_hxc = [2,2,2,5,2,2,2,2]

    # simulate cycle:
    [props,cycle_out,UA,pp] = orc_simulator.simulate_ORC(fluid,x,eta,hot,cld,n_hxc,0)
    
    # print cycle outputs:
    document.getElementById("power-output").value = cycle_out[0]
    document.getElementById("thermal-efficiency").value = cycle_out[1]
    document.getElementById("second-law").value = cycle_out[2]
    document.getElementById("pump-work").value = cycle_out[3]
    document.getElementById("turbine-work").value = cycle_out[4]
    document.getElementById("heat-input").value = cycle_out[5]
    document.getElementById("heat-output").value = cycle_out[6]
    document.getElementById("heat-recuperated").value = cycle_out[7]
    document.getElementById("mass-flow-rate").value = cycle_out[8]

    # print heat exchanger outputs:
    document.getElementById("ua-hot").value = sum(UA[0])/1000
    document.getElementById("ua-cold").value = sum(UA[1])/1000
    document.getElementById("ua-recup").value = UA[2]/1000
    document.getElementById("pp-hot").value = min(pp[0])
    document.getElementById("pp-cold").value = min(pp[1])
    document.getElementById("pp-recup").value = pp[2]

    
# run function on click:    
simulate_cycle = create_proxy(_simulate_cycle)
document.getElementById("simulate-cycle").addEventListener("click", simulate_cycle)

