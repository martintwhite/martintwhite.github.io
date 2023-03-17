from js import document
from pyodide.ffi import create_proxy 
import thermo_props
import orc_simulator
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# heat exchanger discretisation (not user defined):
n_hxc = [2,2,2,5,2,2,2,2]

# initialise figures:
fig, ax = plt.subplots()
fig.set_size_inches(4, 4)
ax.set_position([0.175,0.125,0.80,0.85])
display(fig,target="test_plt")
plt.close(fig)

def setup_fluid(fluid_name):
    
    if fluid_name == "n-pentane":
        tc = 438
        pc = 2480000
        om = 0.441774
        cp = [ 10.4923, 0.6569, -4.13e-4 ]
        wm = 72.1488
        
    return thermo_props.pr_fluid(fluid_name,tc,pc,om,cp,300,0.01,wm)

def _single_cycle(*args, **kwargs):

    # setup fluid:
    name  = document.getElementById("working-fluid-select").value
    fluid = setup_fluid(name)
    
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

    # simulate cycle:
    [props,cycle_out,UA,pp,th,tc] = orc_simulator.simulate_ORC(fluid,x,eta,hot,cld,n_hxc,0)

    # print cycle outputs:
    document.getElementById("power-output").innerHTML = "{:.3f}".format(cycle_out[0])
    document.getElementById("thermal-efficiency").innerHTML = "{:.3f}".format(cycle_out[1])
    document.getElementById("second-law").innerHTML = "{:.3f}".format(cycle_out[2])
    document.getElementById("pump-work").innerHTML = "{:.3f}".format(cycle_out[3])
    document.getElementById("turbine-work").innerHTML = "{:.3f}".format(cycle_out[4])
    document.getElementById("heat-input").innerHTML = "{:.3f}".format(cycle_out[5])
    document.getElementById("heat-output").innerHTML = "{:.3f}".format(cycle_out[6])
    document.getElementById("heat-recuperated").innerHTML = "{:.3f}".format(cycle_out[7])
    document.getElementById("mass-flow-rate").innerHTML = "{:.3f}".format(cycle_out[8])

    # print heat exchanger outputs:
    document.getElementById("ua-hot").innerHTML = "{:.3f}".format(sum(UA[0])/1000)
    document.getElementById("ua-cold").innerHTML = "{:.3f}".format(sum(UA[1])/1000)
    document.getElementById("ua-recup").innerHTML = "{:.3f}".format(UA[2]/1000)
    document.getElementById("pp-hot").innerHTML = "{:.3f}".format(min(pp[0]))
    document.getElementById("pp-cold").innerHTML = "{:.3f}".format(min(pp[1]))
    document.getElementById("pp-recup").innerHTML = "{:.3f}".format(pp[2])
    
    # update T-s plot:   
    document.getElementById("test_plt").innerHTML = ""
    df = pd.read_csv(r'./pentane.csv')
    fig, ax = orc_simulator.plot_cycle_ts(fluid,props,th,tc,df)
    ax.set_position([0.175,0.125,0.80,0.85])
    fig.set_size_inches(4, 4)
    display(fig,target="test_plt")
    plt.close(fig)
    
def _param_cycle(*args, **kwargs):
    
    # setup fluid:
    name  = document.getElementById("working-fluid-select").value
    fluid = setup_fluid(name)
    
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
    
    # extract parametric study:
    param_var = document.getElementById("param-study-select").value
    param_min = float(document.getElementById("param-min").value)
    param_max = float(document.getElementById("param-max").value)
    x_param   = np.linspace(param_min,param_max,10)
    
    # set index of parametric variable:
    if param_var == "condensation-temp":
        param_indx = 0
    elif param_var == "subcool":
        param_indx = 1
    elif param_var == "pressure-ratio":
        param_indx = 2
    elif param_var == "expander-inlet":
        param_indx = 3
    elif param_var == "recuperator":
        param_indx = 4
    elif param_var == "heat-source-outlet":
        param_indx = 5
        
    # run parametric study:
    for i in range(len(x_param)):
        
        # run for current set of inputs:
        x[param_indx] = x_param[i]
        [props,cycle_out,UA,pp,th,tc] = orc_simulator.simulate_ORC(fluid,x,eta,hot,cld,n_hxc,0)

        # print cycle outputs:
        document.getElementById("var-"+str(i+1)).innerHTML = "{:.3f}".format(x_param[i])
        document.getElementById("Wn-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[0])
        document.getElementById("eta1-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[1])
        document.getElementById("eta2-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[2])
        document.getElementById("Wp-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[3])
        document.getElementById("Wt-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[4])
        document.getElementById("Qh-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[5])
        document.getElementById("Qc-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[6])
        document.getElementById("Qr-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[7])
        document.getElementById("mdot-"+str(i+1)).innerHTML = "{:.3f}".format(cycle_out[8])
        document.getElementById("uah-"+str(i+1)).innerHTML = "{:.3f}".format(sum(UA[0])/1000)
        document.getElementById("uac-"+str(i+1)).innerHTML = "{:.3f}".format(sum(UA[1])/1000)
        document.getElementById("uar-"+str(i+1)).innerHTML = "{:.3f}".format(UA[2]/1000)
        document.getElementById("pph-"+str(i+1)).innerHTML = "{:.3f}".format(min(pp[0]))
        document.getElementById("ppc-"+str(i+1)).innerHTML = "{:.3f}".format(min(pp[1]))
        document.getElementById("ppr-"+str(i+1)).innerHTML = "{:.3f}".format(pp[2])

# run function on click:    
single_cycle = create_proxy(_single_cycle)
document.getElementById("single-cycle").addEventListener("click", single_cycle)

# run function on click:    
param_cycle = create_proxy(_param_cycle)
document.getElementById("param-cycle").addEventListener("click", param_cycle)

