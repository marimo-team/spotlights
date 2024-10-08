# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy==2.1.2",
#     "pandas==2.2.3",
#     "matplotlib==3.9.2",
# ]
# ///

import marimo

__generated_with = "0.9.0"
app = marimo.App(width="full")


@app.cell
def __(mo):
    mo.md("""#Overview""")
    return


@app.cell
def __(mo):
    paper_link = 'https://www.nature.com/articles/s44221-024-00316-4'
    github_link = 'https://github.com/we3lab/valuing-flexibility-from-water'
    we3lab_link = 'https://we3lab.stanford.edu'
    nawi_link = 'https://www.nawihub.org/wp-content/uploads/sites/16/2024/03/3.24-Meagan-Mauter-Open-Source-Platform-for-Assessing-the-Cost-and-Carbon-Benefits-of-Flexible-Desalination.pdf'
    mo.md("This page contains interactive visualizations associated with the paper titled *Valuing Energy Flexibility from Water Systems* by Rao et al. (2024) ([paper]({}),[data]({})). The study is part of a broader research effort by the [Water Energy Efficiency & Environment Lab]({}) at Stanford University to understand the value of industrial flexibility for decarbonization. This work was funded by the [National Alliance for Water Innovation]({}).".format(paper_link, github_link, we3lab_link,nawi_link))
    return github_link, nawi_link, paper_link, we3lab_link


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import os, json
    from datetime import datetime, timedelta
    from glob import glob

    def system_line_color(system_type):
            """
            Returns the color associated with the given system type.
            """
            return {
                'AWT_nominal': "#74B29C",
                'AWT_curtailed': "#748D85",
                'WSD': "#8DA0CB",
                'WWT': "#fc8d62",
                }[system_type]

    def system_face_color(system_type):
            """
            Returns the color associated with the given system type.
            """
            return {
                'AWT_nominal': "#74B29C",
                'AWT_curtailed': "#748D85",
                'WSD': "#8DA0CB",
                'WWT': "#fc8d62",
                }[system_type]

    def full_system_label(system_type):
         """
         Returns the full system label associated with the given system type."""
         return{
                'AWT_nominal': 'Advanced Water Treatment: Nominal',
                'AWT_curtailed': 'Advanced Water Treatment: Curtailed',
                'WSD': 'Water Distribution',
                'WWT': 'Wastewater Treatment',
            }[system_type]

    def shortened_system_type(system_label):
        """
        Returns the system type associated with the full system label
        """
        return{
                'Advanced Water Treatment: Nominal': 'AWT_nominal',
                'Advanced Water Treatment: Curtailed':'AWT_curtailed',
                'Water Distribution' : 'WSD',
                'Wastewater Treatment':'WWT',
            }[system_label]

    def reformat_case_name(case_name):
         """
         Returns the full system label associated with the given system type."""
         return{
                'houston': 'Houston - Centerpoint',
                'newyork': 'New York - CONED',
                'sanjose': 'San Jose - PG&E',
                'santabarbara': 'Santa Barbara - SCE',
                'tampa': 'Tampa - TECO',
            }[case_name]

    def valid_repdays(case_name, system_type, plot_type):
        days = [""]
        if 'wastewater' in system_type.lower() or 'wwt' in system_type.lower() or case_name == 'sanjose':
            days.append('Winter')
            days.append('Spring')
            days.append('Summer')
        else:
            if case_name == 'houston':
                days.append('Annualized')
            elif case_name == 'newyork':
                days.append('SummerWeekday')
                days.append('SummerWeekend')
                days.append('WinterWeekday')
                days.append('WinterWeekend')
            elif case_name == 'santabarbara':
                days.append('SummerWeekday')
                days.append('SummerWeekend')
                days.append('Winter')
            elif case_name == 'tampa':
                days.append('SummerWeekday')
                days.append('WinterWeekday')
                days.append('Weekend')
        if plot_type == 'radar' and 'Annualized' not in days:
            days.append('Annualized')
        return days

    def plot_timeseries(sim_data,
                    case_name, 
                    system_type,
                    representative_day, 
                    ax=None, **kwargs):

        # get timing parameters
        t = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in sim_data['DateTime']]
        dT = (t[1] - t[0]).total_seconds()/3600          # time step in hours


        # get load data 
        baseline_power = sim_data['baseline_grid_to_plant_kW'].values / 1000    # convert from kW to MW
        flexible_power = sim_data['flexible_grid_to_plant_kW'].values / 1000    # convert from kW to MW

        # plot the timeseries on the same subplot
        plt.rcParams.update({'axes.labelsize': 12,
                            'xtick.labelsize': 12,
                            'xtick.major.width': 2,
                            'ytick.labelsize': 12,
                            'ytick.major.width': 2,
                            'legend.fontsize': 12,
                            'font.size': 12,
                            'axes.linewidth': 0.5,
                            'lines.linewidth': 2.,
                            'lines.markersize': 1.,
                            'font.size': 12})

        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))

        b_norm = baseline_power / np.mean(baseline_power)
        f_norm = flexible_power / np.mean(baseline_power)


        # plot flexible power in #01665e using a step function
        ax.step(t, f_norm, 
                color=system_line_color(system_type), 
                label='Flexible',
                where='post')

        # plot baseline power in black with dashed line
        ax.step(t, b_norm, 
                color='black', 
                label='Baseline',
                where='post')

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))

        ax.set_xlim([t[0], t[-1]])

        # set the ylim to 0 and 1.2 times the maximum power
        ax.set_ylim([0, 2])
        ax.set_xlabel('Time [hr]')
        ax.set_ylabel('Normalized Load')

        ax.set_title('{}\n{}\n{}'.format(full_system_label(system_type), reformat_case_name(case_name), representative_day), fontsize = 14)

        ax.legend()

        return ax

    def plot_radar(sim_data,
                   case_name,
                    system_type,
                    representative_day,
                    ax=None, **kwargs):
            """
            Plots the radar chart associated with the given case.
            """
            RTE = sim_data['rte']
            EnergyCapacity = sim_data['ed_normalized']
            PowerCapacity = sim_data['p_normalized']

            LABELS = ["Round-Trip\nEfficiency", 
                            "Energy\nCapacity\n(Normalized)", 
                            "Power\nCapacity\n(Normalized)"]
            METRICS = [RTE, EnergyCapacity, PowerCapacity]
            N = 3

            # Define colors
            BG_WHITE = "#FFFFFF"
            GREY70 = "#808080"
            GREY_LIGHT = "#f2efe8"

            # The angles at which the values of the numeric variables are placed
            ANGLES = [2 * np.pi * (n/3) for n in range(N)]
            ANGLES += ANGLES[:1]

            # Angle values going from 0 to 2*pi
            HANGLES = np.linspace(0, 2 * np.pi, 200)
            # Used for the equivalent of horizontal lines in cartesian coordinates plots 
            # The last one is also used to add a fill which acts a background color.
            H0 = np.zeros(len(HANGLES))
            H025 = np.ones(len(HANGLES)) * 0.25
            H050 = np.ones(len(HANGLES)) * 0.5
            H075 = np.ones(len(HANGLES)) * 0.75
            H2 = np.ones(len(HANGLES))


            plt.rcParams.update({'axes.labelsize': 12,
                                'xtick.labelsize': 12,
                                'xtick.major.width': 2,
                                'ytick.labelsize': 12,
                                'ytick.major.width': 2,
                                'legend.fontsize': 12,
                                'font.size': 12,
                                'axes.linewidth': 0.5,
                                'lines.linewidth': 1.,
                                'lines.markersize': 1.,
                                'legend.fontsize': 'medium',
                                'figure.titlesize': 'medium',
                                'font.size': 12})

                # Initialize layout ----------------------------------------------
            if ax == None:
                fig = plt.figure(dpi = 300, figsize=(8,6))
                ax = fig.add_subplot(111, polar=True)
                fig.patch.set_facecolor(BG_WHITE)
            ax.set_facecolor(BG_WHITE)

            # Rotate the "" 0 degrees on top. 
            # There it where the first variable, avg_bill_length, will go.
            ax.set_theta_offset(np.pi / 2)
            ax.set_theta_direction(-1)

            # Setting lower limit to negative value reduces overlap
            # for values that are 0 (the minimums)
            ax.set_ylim(-0.05, 1.15)


            # Remove lines for radial axis (y)
            ax.set_yticks([])
            ax.yaxis.grid(False)
            ax.xaxis.grid(False)

            # # Remove spines
            ax.spines["start"].set_color("none")
            ax.spines["polar"].set_color("none")

            # Add custom lines for radial axis (y) at 0, 0.5 and 1.
            ax.plot(HANGLES, H0, ls=(0, (6, 3)), c=GREY70)
            ax.plot(HANGLES, H025, ls=(0, (6, 3)), c=GREY70)
            ax.plot(HANGLES, H050, ls=(0, (6, 3)), c=GREY70)
            ax.plot(HANGLES, H075, ls=(0, (6, 3)), c=GREY70)
            ax.plot(HANGLES, H2, c=GREY70)

            ax.plot([0, 0], [0, 1], lw=1, c=GREY70)
            ax.plot([2*np.pi/3, 2*np.pi/3], [0,1], lw = 1, c=GREY70)
            ax.plot([4*np.pi/3, 4*np.pi/3], [0,1], lw = 1, c=GREY70)


            # Add levels -----------------------------------------------------
            # These labels indicate the values of the radial axis
            PAD = 0.12
            # ax.text(-np.pi/2, 0 + PAD, "0%", size=16)
            ax.text(-np.pi/2, 0.25 + PAD, "25%", va='center', rotation=90, size=8)
            ax.text(-np.pi/2, 0.5 + PAD, "50%", va='center', rotation=90, size=8)
            ax.text(-np.pi/2, 0.75 + PAD, "75%", va='center', rotation=90, size=8)
            ax.text(-np.pi/2, 1 + PAD, "100%", va='center', rotation=90, size=8)

            ax.plot([0, 2*np.pi/3, 4*np.pi/3, 0], 
                    METRICS + [METRICS[0]], 
                    c = system_line_color(system_type),
                    lw = 1)

            # fill area inside triangle 
            ax.fill([0, 2*np.pi/3, 4*np.pi/3, 0], 
                    METRICS + [METRICS[0]], 
                    system_face_color(system_type), 
                    alpha = 0.75)

            # Set values for the angular axis (x)
            ax.set_xticks(ANGLES[:-1])
            ax.set_xticklabels(LABELS, size=10)
            ax.yaxis.labelpad = 15
            ax.set_title('{}\n{}\n{}'.format(full_system_label(system_type), reformat_case_name(case_name), representative_day), fontsize = 12)


            return ax

    def plot_contour(sim_data,
                        case_name,
                        system_type,
                        financial_metric,
                        interest_rate,
                        om_cost_annum,
                        fig = None,
                        ax=None):
            # plot the timeseries on the same subplot
            plt.rcParams.update({'axes.labelsize': 12,
                                'xtick.labelsize': 12,
                                'xtick.major.width': 2,
                                'ytick.labelsize': 12,
                                'ytick.major.width': 2,
                                'legend.fontsize': 12,
                                'font.size': 21,
                                'axes.linewidth': 0.5,
                                'lines.linewidth': 1.,
                                'lines.markersize': 1.,
                                'legend.fontsize': 'medium',
                                'figure.titlesize': 'medium',
                                'font.size': 12})

            if ax is None or fig is None:
                fig, ax = plt.subplots(dpi = 300, figsize = (8,6))

            benefits = sim_data["annualized_benefit"] + 10000 - om_cost_annum
            discharge = sim_data["annualized_discharge_capacity"]

            lifetime = np.linspace(5, 30, 26).astype(int)

            if "curtailed" in system_type:
                capex_end = 10e6
            else:
                capex_end = 1e6
            capex = np.linspace(0, capex_end, 100)

            discount = np.zeros(len(lifetime))

            for i in range(len(lifetime)):
                discount[i] = sum([1/((1+interest_rate)**n) for n in range(1, lifetime[i])])

            lifetime_mesh, capex_mesh = np.meshgrid(lifetime, capex)
            discount_mesh, capex_mesh = np.meshgrid(discount, capex)

            lvof = 1000 * (benefits * discount_mesh - capex_mesh) / (discharge * lifetime_mesh)
            npv = benefits * discount_mesh - capex_mesh
            roi = 100 * npv / (capex_mesh + 1e-8)

            # options=['Value of Flexibility', 'Return on Investment', 'Net Present Value'],
            if financial_metric == 'Value of Flexibility':
                range_bar = [-200, 200]
                contour = ax.contourf(capex_mesh * 1e-6, lifetime_mesh, lvof,
                                levels = np.linspace(range_bar[0], range_bar[1], 51, endpoint=True),
                                cmap = 'RdYlBu',
                                extend = 'both')
            elif financial_metric == 'Return on Investment':
                range_bar = [-500, 500]
                contour = ax.contourf(capex_mesh * 1e-6, lifetime_mesh, roi,
                                    levels = np.linspace(range_bar[0], range_bar[1], 51, endpoint=True),
                                    cmap = 'RdYlGn',
                                    extend = 'both')
            elif financial_metric == 'Net Present Value':
                range_bar = [-10*capex_end, 10*capex_end]
                contour = ax.contourf(capex_mesh * 1e-6, lifetime_mesh, npv,
                            levels = np.linspace(range_bar[0], range_bar[1], 51, endpoint=True),
                            cmap = 'RdGy_r',
                            extend = 'both')
            else:
                pass

            contour_breakeven = ax.contour(contour, levels = [0], colors = ['black'], linestyles = ['-'], alpha = 1)

            cbar = fig.colorbar(contour, ax=ax)
            cbar.add_lines(contour_breakeven)
            cbar.set_ticks(np.linspace(range_bar[0], range_bar[1], 9, endpoint=True))

            if "curtailed" in system_type:
                ax.set_xticks(np.linspace(0,10,11))
            else:
                ax.set_xticks(np.linspace(0,1,5))
            ax.set_yticks(np.linspace(5,30,6))
            ax.set_xlabel('Net Capital Upgrade Cost [$M]')
            ax.set_ylabel('Facility Lifetime after Upgrade [Years]')
            units = {"Value of Flexibility" : ' [$/MWh]',
                     "Return on Investment" : ' [%]',
                     "Net Present Value" : ' [$]'}

            ax.set_title(financial_metric + units[financial_metric] +
                        '\n{}\n{}'.format(reformat_case_name(case_name), full_system_label(system_type)), fontsize = 11)
            fig.tight_layout() 

            return fig, ax

    def get_ts_data(case_name,
                   system_type, 
                   representative_day):
            """
            Parses the file hierarchy to find the data for the given case.
            """
            filepath = "timeseries/{}/{}/{}.csv".format(system_type,case_name,representative_day)
            return pd.read_csv(filepath), filepath

    def get_radar_data(case_name,
                      system_type,
                      representative_day):
            filepath = "casestudies/{}/{}/{}/radar.json".format(case_name,
                                                                               system_type,
                                                                               representative_day.split('/')[0])
            return json.load(open(filepath)), filepath


    def get_costing_data(case_name, 
                        system_type):

            filepath = "costing/{}/{}.json".format(case_name, system_type)
            return json.load(open(filepath)), filepath
    return (
        datetime,
        full_system_label,
        get_costing_data,
        get_radar_data,
        get_ts_data,
        glob,
        json,
        mdates,
        mo,
        mpl,
        np,
        os,
        pd,
        plot_contour,
        plot_radar,
        plot_timeseries,
        plt,
        reformat_case_name,
        shortened_system_type,
        system_face_color,
        system_line_color,
        timedelta,
        valid_repdays,
    )


@app.cell
def __(mo):
    mo.md("""#Operating Schema Comparison""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""This section compares the operating schema of two different configurations.""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Select the configuration options for the operating schema A.""")
    return


@app.cell
def __(mo):
    ts_A_case_name = mo.ui.dropdown(
            label="Select Case City:",
            options=["houston", "newyork", "sanjose", "santabarbara", "tampa"],
            value = "santabarbara")
    ts_A_case_name
    return (ts_A_case_name,)


@app.cell
def __(mo):
    ts_A_sys_name = mo.ui.dropdown(
            label="Select System Type:",
            options= ['Advanced Water Treatment: Nominal','Advanced Water Treatment: Curtailed','Water Distribution','Wastewater Treatment'],
            value = 'Advanced Water Treatment: Curtailed')
    ts_A_sys_name
    return (ts_A_sys_name,)


@app.cell
def __(
    mo,
    shortened_system_type,
    ts_A_case_name,
    ts_A_sys_name,
    valid_repdays,
):
    valid_day_ts_a = valid_repdays(case_name=ts_A_case_name.value,
                                  system_type= shortened_system_type(ts_A_sys_name.value),
                                  plot_type='timeseries')
    ts_A_day = mo.ui.dropdown(
            label="Select Representative Day:",
            options= valid_day_ts_a,
            value = valid_day_ts_a[1])
    ts_A_day
    return ts_A_day, valid_day_ts_a


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Select the configuration options for the operating schema B.""")
    return


@app.cell(hide_code=True)
def __(mo):
    ts_B_case_name = mo.ui.dropdown(
            label="Select Case City:",
            options=["houston", "newyork", "sanjose", "santabarbara", "tampa"],
            value = "santabarbara")
    ts_B_case_name
    return (ts_B_case_name,)


@app.cell
def __(mo):
    ts_B_sys_name = mo.ui.dropdown(
            label="Select System Type:",
            options= ['Advanced Water Treatment: Nominal','Advanced Water Treatment: Curtailed','Water Distribution','Wastewater Treatment'],
            value = 'Wastewater Treatment')
    ts_B_sys_name
    return (ts_B_sys_name,)


@app.cell
def __(
    mo,
    shortened_system_type,
    ts_B_case_name,
    ts_B_sys_name,
    valid_repdays,
):
    valid_day_ts_b = valid_repdays(case_name=ts_B_case_name.value,
                                  system_type= shortened_system_type(ts_B_sys_name.value),
                                  plot_type='timeseries')
    ts_B_day = mo.ui.dropdown(
            label="Select Representative Day",
            options= valid_day_ts_b,
            value = "")
    ts_B_day
    return ts_B_day, valid_day_ts_b


@app.cell
def __(
    full_system_label,
    get_ts_data,
    plot_timeseries,
    plt,
    reformat_case_name,
    shortened_system_type,
    ts_A_case_name,
    ts_A_day,
    ts_A_sys_name,
    ts_B_case_name,
    ts_B_day,
    ts_B_sys_name,
):
    fig_ts, ax_ts = plt.subplots(1,2,figsize=(10, 6))

    try:
        if ts_A_day.value == "":
            ax_ts[0].set_title('{}\n{}\n{}'.format(full_system_label(ts_A_sys_name.value), 
                                               reformat_case_name(ts_A_case_name.value), 
                                               ts_A_day.value), 
                                               fontsize = 12)
            ax_ts[0].text(0.5, 0.5, 'Select a representative day', 
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_ts[0].transAxes)
        sim_dataA = get_ts_data(ts_A_case_name.value, 
                                shortened_system_type(ts_A_sys_name.value), 
                                ts_A_day.value)
        ax_ts[0] = plot_timeseries(sim_dataA[0], 
                        case_name=ts_A_case_name.value,
                        system_type=shortened_system_type(ts_A_sys_name.value),
                        representative_day=ts_A_day.value,
                                ax = ax_ts[0])
    except:
        # ax_ts[0].set_title('{}\n{}\n{}'.format(full_system_label(ts_A_case_name.value), 
        #                                        reformat_case_name(ts_A_sys_name.value), 
        #                                        ts_A_day.value), 
        #                                        fontsize = 12)
        if ts_A_day.value == "":
            ax_ts[0].text(0.5, 0.5, 'Select a representative day', 
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_ts[0].transAxes)
        else:
            ax_ts[0].text(0.5, 0.5, "Data not available", 
                        horizontalalignment='center',
                        verticalalignment='center', 
                        transform=ax_ts[0].transAxes)

    try:
        if ts_B_day.value == "":
            ax_ts[1].set_title('{}\n{}\n{}'.format(full_system_label(ts_B_case_name.value), 
                                               reformat_case_name(ts_B_sys_name.value), 
                                               ts_B_day.value), 
                                               fontsize = 12)
            ax_ts[1].text(0.5, 0.5, 'Select a representative day', 
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_ts[0].transAxes)
        sim_dataB = get_ts_data(ts_B_case_name.value, 
                                shortened_system_type(ts_B_sys_name.value), 
                                ts_B_day.value)
        ax_ts[1] = plot_timeseries(sim_dataB[0], 
                       case_name=ts_B_case_name.value,
                       system_type=shortened_system_type(ts_B_sys_name.value),
                       representative_day=ts_B_day.value,
                               ax = ax_ts[1])

    except:

        if ts_B_day.value == "":
            ax_ts[1].text(0.5, 0.5, 'Select a representative day', 
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_ts[1].transAxes)
        else:
            ax_ts[1].text(0.5, 0.5, "Data not available", 
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_ts[1].transAxes)

    fig_ts.tight_layout()
    fig_ts
    return ax_ts, fig_ts, sim_dataA, sim_dataB


@app.cell
def __(mo):
    mo.md("""#Energy Performance Metrics Comparison""")
    return


@app.cell
def __(mo):
    mo.md("""This section compares the energy performance metrics of two different configurations.""")
    return


@app.cell
def __(mo):
    mo.md("""Select the configuration options for the case A.""")
    return


@app.cell
def __(mo):
    radar_A_case_name = mo.ui.dropdown(
            label="Select Case City:",
            options=["houston", "newyork", "sanjose", "santabarbara", "tampa"],
            value = "santabarbara")
    radar_A_case_name
    return (radar_A_case_name,)


@app.cell
def __(mo):
    radar_A_sys_name = mo.ui.dropdown(
            label="Select System Type:",
            options= ['Advanced Water Treatment: Nominal','Advanced Water Treatment: Curtailed','Water Distribution','Wastewater Treatment'],
            value = 'Advanced Water Treatment: Curtailed')
    radar_A_sys_name
    return (radar_A_sys_name,)


@app.cell
def __(mo, radar_A_case_name, radar_A_sys_name, valid_repdays):
    valid_day_r_a = valid_repdays(case_name=radar_A_case_name.value,
                                  system_type= radar_A_sys_name.value,
                                  plot_type='radar')
    r_day_A = mo.ui.dropdown(
        label="Select Representative Day:",
        options= valid_day_r_a,
        value = valid_day_r_a[1])
    r_day_A
    return r_day_A, valid_day_r_a


@app.cell
def __(mo):
    mo.md("""Select the configuration options for the case B.""")
    return


@app.cell
def __(mo):
    radar_B_case_name = mo.ui.dropdown(
            label="Select Case City:",
            options=["houston", "newyork", "sanjose", "santabarbara", "tampa"],
            value = "santabarbara")
    radar_B_case_name
    return (radar_B_case_name,)


@app.cell
def __(mo):
    radar_B_sys_name = mo.ui.dropdown(
            label="Select System Type:",
            options= ['Advanced Water Treatment: Nominal','Advanced Water Treatment: Curtailed','Water Distribution','Wastewater Treatment'],
            value = 'Advanced Water Treatment: Nominal')
    radar_B_sys_name
    return (radar_B_sys_name,)


@app.cell
def __(mo, radar_B_case_name, radar_B_sys_name, valid_repdays):
    valid_day_r_b = valid_repdays(case_name=radar_B_case_name.value,
                                  system_type= radar_B_sys_name.value,
                                  plot_type='radar')
    r_day_B = mo.ui.dropdown(
        label="Select Representative Day:",
        options= valid_day_r_b,
        value = "")
    r_day_B
    return r_day_B, valid_day_r_b


@app.cell
def __(radar_B_sys_name):
    print(radar_B_sys_name.value)
    return


@app.cell
def __(
    get_radar_data,
    plot_radar,
    plt,
    r_day_A,
    r_day_B,
    radar_A_case_name,
    radar_A_sys_name,
    radar_B_case_name,
    radar_B_sys_name,
    reformat_case_name,
    shortened_system_type,
):
    fig_r = plt.figure(figsize = (10, 4))
    ax_rA = plt.subplot(121, projection = 'polar')
    ax_rB = plt.subplot(122, projection='polar')

    try:
        sim_dataA_r = get_radar_data(radar_A_case_name.value, 
                                     shortened_system_type(radar_A_sys_name.value), 
                                     r_day_A.value)
        ax_rA = plot_radar(sim_dataA_r[0], 
                       case_name=radar_A_case_name.value,
                       system_type=shortened_system_type(radar_A_sys_name.value),
                       representative_day=r_day_A.value,
                       ax = ax_rA)
    except:
        ax_rA.set_yticklabels([])
        ax_rA.set_xticklabels([])
        ax_rA.yaxis.grid(False)
        ax_rA.xaxis.grid(False)
        if r_day_A.value == "":
            ax_rA.text(0, 0, 'Select a representative day',                   
                   horizontalalignment='center',
                   verticalalignment='center',
                  fontsize = 8)
        else:
            ax_rA.text(0, 0, 'Data not available',                   
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize = 8)

        ax_rA.set_title('{}\n{}\n{}'.format(radar_A_sys_name.value, 
                                            reformat_case_name(radar_A_case_name.value), 
                                            r_day_A.value), fontsize = 10, pad=26.1)

    try:

        sim_dataB_r = get_radar_data(radar_B_case_name.value, 
                                     shortened_system_type(radar_B_sys_name.value), 
                                     r_day_B.value)
        ax_rB = plot_radar(sim_dataB_r[0],
                       case_name=radar_B_case_name.value,
                       system_type=shortened_system_type(radar_B_sys_name.value),
                       representative_day=r_day_B.value, 
                       ax = ax_rB)
    except:
        ax_rB.set_yticklabels([])
        ax_rB.set_xticklabels([])
        ax_rB.yaxis.grid(False)
        ax_rB.xaxis.grid(False)
        if r_day_B.value == "":
            ax_rB.text(0, 0, 'Select a representative day',                   
                   horizontalalignment='center',
                   verticalalignment='center',
                  fontsize = 8)
        else:
            ax_rB.text(0, 0, "Data not available",             # show filepath on plot      
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize = 8)
        ax_rB.set_title('{}\n{}\n{}'.format(radar_B_sys_name.value, 
                                            reformat_case_name(radar_B_case_name.value), 
                                            r_day_B.value), fontsize = 10, pad=26.1)

    if 'curtailed' in radar_A_sys_name.value or 'curtailed' in radar_B_sys_name.value:
        plt.figtext(0.5, 0.02, "*Round-trip efficiency is not defined for cases with supply curtailment", ha="center", fontsize=8)

    fig_r.tight_layout()
    fig_r
    return ax_rA, ax_rB, fig_r, sim_dataA_r, sim_dataB_r


@app.cell
def __(mo):
    mo.md("""#Levelized Value of Flexibility Comparison""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""This section compares the levelized value of flexibility for two different configurations.""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Select the configuration options for the case A.""")
    return


@app.cell(hide_code=True)
def __(mo):
    contour_A_case_name = mo.ui.dropdown(
            label="Select Case City:",
            options=["houston", "newyork", "sanjose", "santabarbara", "tampa"],
            value = "santabarbara")
    contour_A_case_name
    return (contour_A_case_name,)


@app.cell
def __(mo):
    contour_A_sys_name = mo.ui.dropdown(
            label="Select System Type:",
            options= ['Advanced Water Treatment: Nominal','Advanced Water Treatment: Curtailed','Water Distribution','Wastewater Treatment'],
            value = 'Advanced Water Treatment: Curtailed')
    contour_A_sys_name
    return (contour_A_sys_name,)


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Select the configuration options for the case B.""")
    return


@app.cell(hide_code=True)
def __(mo):
    contour_B_case_name = mo.ui.dropdown(
            label="Select Case City:",
            options=["houston", "newyork", "sanjose", "santabarbara", "tampa"],
            value = "santabarbara")
    contour_B_case_name
    return (contour_B_case_name,)


@app.cell
def __(mo):
    contour_B_sys_name = mo.ui.dropdown(
            label="Select System Type:",
            options= ['Advanced Water Treatment: Nominal','Advanced Water Treatment: Curtailed','Water Distribution','Wastewater Treatment'],
            value = 'Water Distribution')
    contour_B_sys_name
    return (contour_B_sys_name,)


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Select comparison parameters.""")
    return


@app.cell
def __(mo):
    om_cost_annum = mo.ui.slider(
        start = -10000.,
        stop = 100000,
        step = 5000,
        value = 10000,
        label = 'Annual change in labor/maintainance costs due to flexibility [$]')
    om_cost_annum
    return (om_cost_annum,)


@app.cell
def __(mo):
    interest_rate = mo.ui.slider(
        start = 0.,
        stop = 0.10,
        step = 0.01,
        value = 0.03,
        label = 'Interest rate [-]')
    interest_rate
    return (interest_rate,)


@app.cell(hide_code=True)
def __(mo):
    financial_metric = mo.ui.dropdown(
            label="Financial Metric:",
            options=['Value of Flexibility', 'Return on Investment'],
            value = "Value of Flexibility")
    financial_metric
    return (financial_metric,)


@app.cell
def __(
    contour_A_case_name,
    contour_A_sys_name,
    contour_B_case_name,
    contour_B_sys_name,
    financial_metric,
    get_costing_data,
    interest_rate,
    om_cost_annum,
    plot_contour,
    plt,
    reformat_case_name,
    shortened_system_type,
):
    fig_c, ax_c = plt.subplots(1,2, figsize = (10,4))

    try:
        sim_dataA_c = get_costing_data(contour_A_case_name.value, shortened_system_type(contour_A_sys_name.value))
        fig_c, ax_c[0] = plot_contour(sim_dataA_c[0], 
                                      case_name=contour_A_case_name.value,
                                      system_type=shortened_system_type(contour_A_sys_name.value),
                                      om_cost_annum=om_cost_annum.value,
                                      fig = fig_c,
                                      ax = ax_c[0],
                                      financial_metric=financial_metric.value,
                                      interest_rate = interest_rate.value)

    except:
        ax_c[0].set_title('{}\n{}'.format(contour_A_sys_name.value, 
                                               reformat_case_name(contour_A_case_name.value)),
                                               fontsize = 12)
        ax_c[0].text(0.5, 0.5, "Data not available", # show filepath on plot
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_c[0].transAxes)

    try:
        sim_dataB_c = get_costing_data(case_name = contour_B_case_name.value, 
                                   system_type = shortened_system_type(contour_B_sys_name.value))
        fig_c, ax_c = plot_contour(sim_data = sim_dataB_c[0], 
                                   case_name = contour_B_case_name.value,
                                   system_type = shortened_system_type(contour_B_sys_name.value),
                                   om_cost_annum=om_cost_annum.value,
                                   fig = fig_c,
                                   ax = ax_c[1],
                                   financial_metric=financial_metric.value,
                                   interest_rate = interest_rate.value)
    except:
        ax_c[1].set_title('{}\n{}'.format(contour_B_sys_name.value, 
                                               reformat_case_name(contour_B_case_name.value)),
                                               fontsize = 12)
        ax_c[1].text(0.5, 0.5, "Data not available", # show filepath on plot
                      horizontalalignment='center',
                      verticalalignment='center', 
                      transform=ax_c[1].transAxes)

    fig_c.tight_layout()
    fig_c
    return ax_c, fig_c, sim_dataA_c, sim_dataB_c


if __name__ == "__main__":
    app.run()
