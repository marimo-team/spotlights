# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy==2.1.2",
#     "pandas==2.2.3",
#     "plotly==5.24.1",
# ]
# ///
import marimo

__generated_with = "0.9.7-dev1"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("<h1> Action Potential Simulator </h1>").center()
    return


@app.cell
def __():
    #Import required libraries
    import marimo as mo
    import numpy as np
    import pandas as pd
    import micropip
    return micropip, mo, np, pd


@app.cell
async def __(micropip):
    #Account for using WASM which doesn't natively have plotly so use micropip.install
    await micropip.install("plotly")
    import plotly.express as px
    return (px,)


@app.cell
def __(mo):
    #Create an interactive space where user can select action potential constants, timing, and variables on their own

    #Constants
    Membrane_Capacitance = mo.ui.number(0.5,2,0.1,0.5)
    Sodium_Conductance = mo.ui.number(50,200,1,50)
    Potassium_Conductance = mo.ui.number(10,50,1,10)
    Leak_Conductance = mo.ui.number(0.1,1,0.1,0.1)
    Sodium_Reverse_Potential = mo.ui.number(40,70,1,40)
    Potassium_Reverse_Potential = mo.ui.number(-90,-60,1,-90)
    Leak_Reverse_Potential = mo.ui.number(-70,-50,1,-70) 

    #Action potential timing
    Duration_Time = mo.ui.number(0.01,0.05,0.01,0.01)
    Stimulation_End = mo.ui.number(12,25,1,12)
    Total_Time = mo.ui.number(100,200,1,100)
    return (
        Duration_Time,
        Leak_Conductance,
        Leak_Reverse_Potential,
        Membrane_Capacitance,
        Potassium_Conductance,
        Potassium_Reverse_Potential,
        Sodium_Conductance,
        Sodium_Reverse_Potential,
        Stimulation_End,
        Total_Time,
    )


@app.cell
def __(
    Duration_Time,
    Leak_Conductance,
    Leak_Reverse_Potential,
    Membrane_Capacitance,
    Potassium_Conductance,
    Potassium_Reverse_Potential,
    Sodium_Conductance,
    Sodium_Reverse_Potential,
    Stimulation_End,
    Total_Time,
    mo,
):
    #Vertically stack the interactive elements so there's structure to them
    Action_Potential_Constants = mo.hstack([
            Membrane_Capacitance,
            Sodium_Conductance,
            Potassium_Conductance,
            Leak_Conductance,
            Sodium_Reverse_Potential,
            Potassium_Reverse_Potential,
            Leak_Reverse_Potential
    ]) 

    Time = mo.hstack([
        Duration_Time,
        Stimulation_End,
        Total_Time
    ])
    return Action_Potential_Constants, Time


@app.cell
def __(mo):
    mo.md("""<h2> Action Potential Constants </h2>""")
    return


@app.cell
def __(Action_Potential_Constants):
    Action_Potential_Constants
    return


@app.cell
def __(mo):
    mo.md("""<h2> Time </h2>""")
    return


@app.cell
def __(Time):
    Time
    return


@app.cell
def __(
    Duration_Time,
    Leak_Conductance,
    Leak_Reverse_Potential,
    Membrane_Capacitance,
    Potassium_Conductance,
    Potassium_Reverse_Potential,
    Sodium_Conductance,
    Sodium_Reverse_Potential,
    Stimulation_End,
    Total_Time,
    np,
):
    # Process user selected values so an action potential plot can be generated
    C_m = Membrane_Capacitance.value   
    g_Na = Sodium_Conductance.value  
    g_K = Potassium_Conductance.value
    g_L = Leak_Conductance.value
    E_Na = Sodium_Reverse_Potential.value  
    E_K = Potassium_Reverse_Potential.value
    E_L = Leak_Reverse_Potential.value

    dt = Duration_Time.value  
    T = Total_Time.value 
    t = np.arange(0, T, dt) 


    V = -65  
    m = 0.05 
    h = 0.6   
    n = 0.32  

    # Stimulus
    I = np.zeros(len(t)) 
    I[int(10 / dt):int(Stimulation_End.value / dt)] = 10  

    def alpha_m(V):
        return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))

    def beta_m(V):
        return 4 * np.exp(-(V + 65) / 18)

    def alpha_h(V):
        return 0.07 * np.exp(-(V + 65) / 20)

    def beta_h(V):
        return 1 / (1 + np.exp(-(V + 35) / 10))

    def alpha_n(V):
        return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))

    def beta_n(V):
        return 0.125 * np.exp(-(V + 65) / 80)

    Vm = np.zeros(len(t))  
    m_values = np.zeros(len(t))  
    h_values = np.zeros(len(t))  
    n_values = np.zeros(len(t)) 


    for i in range(len(t)):
        m += dt * (alpha_m(V) * (1 - m) - beta_m(V) * m)
        h += dt * (alpha_h(V) * (1 - h) - beta_h(V) * h)
        n += dt * (alpha_n(V) * (1 - n) - beta_n(V) * n)

        g_Na_t = g_Na * (m ** 3) * h
        g_K_t = g_K * (n ** 4)
        g_L_t = g_L

        V += dt * (I[i] - g_Na_t * (V - E_Na) - g_K_t * (V - E_K) - g_L_t * (V - E_L)) / C_m

        Vm[i] = V
        m_values[i] = m
        h_values[i] = h
        n_values[i] = n
    return (
        C_m,
        E_K,
        E_L,
        E_Na,
        I,
        T,
        V,
        Vm,
        alpha_h,
        alpha_m,
        alpha_n,
        beta_h,
        beta_m,
        beta_n,
        dt,
        g_K,
        g_K_t,
        g_L,
        g_L_t,
        g_Na,
        g_Na_t,
        h,
        h_values,
        i,
        m,
        m_values,
        n,
        n_values,
        t,
    )


@app.cell
def __(Vm, pd, t):
    Potential_Data = pd.DataFrame({'Time (ms)': t, 'Membrane Potential (mV)': Vm})
    return (Potential_Data,)


@app.cell
def __(Potential_Data, px):
    px.line(Potential_Data, x='Time (ms)', y='Membrane Potential (mV)', title='Action Potential Simulation')
    return


@app.cell
def __(Potential_Data, mo, pd):
    Statistics_Table = pd.DataFrame(
        {
            'Statistic':[
                'Global Max Potential',
                'Global Min Potential',
                'Mean Potential'
            ],
            'Value':[
                Potential_Data['Membrane Potential (mV)'].max(),
                Potential_Data['Membrane Potential (mV)'].min(),
                Potential_Data['Membrane Potential (mV)'].mean()
            ]
        }
    )
    mo.ui.dataframe(Statistics_Table)
    return (Statistics_Table,)


if __name__ == "__main__":
    app.run()
