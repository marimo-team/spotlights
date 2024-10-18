# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy==1.26.4",
#     "plotly==5.24.1",
#     "pandas==2.2.3",
#     "duckdb==1.1.2",
#     "statsmodels==0.14.4",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""<h1> Risk Management Analytics </h1>""")
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    import duckdb as db 
    from statsmodels.stats.proportion import proportions_ztest
    import numpy as np
    return db, mo, np, pd, proportions_ztest, px


@app.cell
def __(pd):
    Risk_Arrangement = pd.read_csv('assets/Risk_Arrangement.csv')
    return (Risk_Arrangement,)


@app.cell
def __():
    Risk_query_2019 = """
    SELECT REF_DATE, Risk_management_arrangements, NAICS, VALUE
    FROM Risk_Arrangement
    WHERE Risk_management_arrangements IN (
        'A Business Continuity Plan (BCP)',
        'Frequent updating of operating systems',
        'No risk management arrangements'
    )
    AND REF_DATE='2019';
    """

    Risk_query_2021 = """
    SELECT REF_DATE, Risk_management_arrangements, NAICS, VALUE
    FROM Risk_Arrangement
    WHERE Risk_management_arrangements IN (
        'A Business Continuity Plan (BCP)',
        'Frequent updating of operating systems',
        'No risk management arrangements'
    )
    AND REF_DATE='2021';
    """
    return Risk_query_2019, Risk_query_2021


@app.cell
def __(Risk_query_2019, Risk_query_2021, db):
    Canada_Risk_Landscape_2019 = db.execute(Risk_query_2019).df()
    Canada_Risk_Landscape_2021 = db.execute(Risk_query_2021).df()
    return Canada_Risk_Landscape_2019, Canada_Risk_Landscape_2021


@app.cell
def __(np, proportions_ztest):
    #Risk arrangements
    Agricultural_BCP=proportions_ztest(
        count=np.array([2.2,1.8]),
        nobs=np.array([100,100]),
        alternative='smaller'
    ) 

    Schools_BCP=proportions_ztest(
        count=np.array([6.5,12.7]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )

    Hospitals_BCP=proportions_ztest(
        count=np.array([20,18.8]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )

    Agricultural_OS=proportions_ztest(
        count=np.array([13.4,13.0]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )

    Schools_OS=proportions_ztest(
        count=np.array([45.2,39.2]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )

    Hospitals_OS=proportions_ztest(
        count=np.array([43.6,38.1]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )

    Agricultural_No_RM=proportions_ztest(
        count=np.array([42.3,37.2]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )

    Schools_No_RM=proportions_ztest(
        count=np.array([8.9,10.1]),
        nobs=np.array([100,100]),
        alternative='larger'
    )

    Hospitals_No_RM=proportions_ztest(
        count=np.array([15.9,8.1]),
        nobs=np.array([100,100]),
        alternative='smaller'
    )
    return (
        Agricultural_BCP,
        Agricultural_No_RM,
        Agricultural_OS,
        Hospitals_BCP,
        Hospitals_No_RM,
        Hospitals_OS,
        Schools_BCP,
        Schools_No_RM,
        Schools_OS,
    )


@app.cell
def __(np, proportions_ztest):
    #Incidents 
    Agricultural_No_Impact = proportions_ztest(
        count = np.array([83.3,92.2]),
        nobs = np.array([100,100]),
        alternative='larger'
    ) 

    Agricultural_Stolen_Money = proportions_ztest(
        count = np.array([5.9,2.7]),
        nobs = np.array([100,100]),
        alternative='smaller'
    )

    Agricultural_Stolen_Personal = proportions_ztest(
        count = np.array([5.5,2.7]),
        nobs = np.array([100,100]),
        alternative='smaller'
    )

    Hospitals_No_Impact = proportions_ztest(
        count = np.array([63.3,89.1]),
        nobs = np.array([100,100]),
        alternative='larger'
    )

    Hospitals_Stolen_Money = proportions_ztest(
        count = np.array([27.5,4.0]),
        nobs = np.array([100,100]),
        alternative='smaller'
    )

    Hospitals_Stolen_Personal = proportions_ztest(
        count = np.array([16.9,4.1]),
        nobs = np.array([100,100]),
        alternative='smaller'
    )

    Schools_No_Impact = proportions_ztest(
        count = np.array([71.2,78.2]),
        nobs = np.array([100,100]),
        alternative='larger'
    )

    Schools_Stolen_Money = proportions_ztest(
        count = np.array([13.3,8.8]),
        nobs = np.array([100,100]),
        alternative='smaller'
    )

    Schools_Stolen_Personal = proportions_ztest(
        count = np.array([5.9,10.8]),
        nobs = np.array([100,100]),
        alternative='larger'
    )
    return (
        Agricultural_No_Impact,
        Agricultural_Stolen_Money,
        Agricultural_Stolen_Personal,
        Hospitals_No_Impact,
        Hospitals_Stolen_Money,
        Hospitals_Stolen_Personal,
        Schools_No_Impact,
        Schools_Stolen_Money,
        Schools_Stolen_Personal,
    )


@app.cell
def __(
    Agricultural_BCP,
    Agricultural_No_RM,
    Agricultural_OS,
    Hospitals_BCP,
    Hospitals_No_RM,
    Hospitals_OS,
    Schools_BCP,
    Schools_No_RM,
    Schools_OS,
    pd,
):
    Risk_Proportions_Table = pd.DataFrame(
        {
            'Risk Arrangement':[
                'Business Continuity Plan',
                'Frequent Updating of operating systems',
                'No risk management plan in place'
            ],
            'Hospitals':[Hospitals_BCP[1],
                         Hospitals_OS[1],
                         Hospitals_No_RM[1]
            ],
            'Schools':[Schools_BCP[1],
                       Schools_OS[1],
                       Schools_No_RM[1]
            ],
            'Agricultural':[Agricultural_BCP[1],
                               Agricultural_OS[1],
                               Agricultural_No_RM[1]
            ]
        }
    )
    return (Risk_Proportions_Table,)


@app.cell
def __(
    Agricultural_No_Impact,
    Agricultural_Stolen_Money,
    Agricultural_Stolen_Personal,
    Hospitals_No_Impact,
    Hospitals_Stolen_Money,
    Hospitals_Stolen_Personal,
    Schools_No_Impact,
    Schools_Stolen_Money,
    Schools_Stolen_Personal,
    pd,
):
    Incident_Proportions_Table = pd.DataFrame(
        {
            'Incident':[
                'No Impact on business',
                'Stolen money or demand ransom',
                'Stolen personal or financial information',
            ],
            'Hospitals':[Hospitals_No_Impact[1],
                         Hospitals_Stolen_Money[1],
                         Hospitals_Stolen_Personal[1]
            ],
            'Schools':[Schools_No_Impact[1],
                       Schools_Stolen_Money[1],
                       Schools_Stolen_Personal[1]
            ],
            'Agricultural':[Agricultural_No_Impact[1],
                               Agricultural_Stolen_Money[1],
                               Agricultural_Stolen_Personal[1]
            ]
        }
    )
    return (Incident_Proportions_Table,)


@app.cell
def __(mo):
    Ref_Date = mo.ui.slider(2019,2021,2)
    mo.md(rf"Year: {Ref_Date}").style({'border-width':'4px','border-color':'gray'})
    return (Ref_Date,)


@app.cell
def __(Ref_Date):
    Year = Ref_Date.value
    return (Year,)


@app.cell
def __(
    Canada_Incident_Landscape_2019,
    Canada_Incident_Landscape_2021,
    Canada_Risk_Landscape_2019,
    Canada_Risk_Landscape_2021,
    px,
):
    Grouped_Risks_2021 = px.histogram(
        Canada_Risk_Landscape_2021,
        x='Risk_management_arrangements',
        y='VALUE',
        color='NAICS',
        barmode='group'
    )

    Grouped_Risks_2019 = px.histogram(
        Canada_Risk_Landscape_2019,
        x='Risk_management_arrangements',
        y='VALUE',
        color='NAICS',
        barmode='group'
    ) 

    Grouped_Incidents_2019 = px.histogram(
        Canada_Incident_Landscape_2019,
        x='Cyber_security_incidents',
        y='VALUE',
        color='NAICS',
        barmode='group'
    )

    Grouped_Incidents_2021 = px.histogram(
        Canada_Incident_Landscape_2021,
        x='Cyber_security_incidents',
        y='VALUE',
        color='NAICS',
        barmode='group'
    )
    return (
        Grouped_Incidents_2019,
        Grouped_Incidents_2021,
        Grouped_Risks_2019,
        Grouped_Risks_2021,
    )


@app.cell
def __(
    Grouped_Incidents_2019,
    Grouped_Incidents_2021,
    Grouped_Risks_2019,
    Grouped_Risks_2021,
):
    def Grouped_Risks(Year):
        if Year == 2019:
            return Grouped_Risks_2019
        else:
            return Grouped_Risks_2021

    def Grouped_Incidents(Year):
        if Year == 2019:
            return Grouped_Incidents_2019
        else:
            return Grouped_Incidents_2021
    return Grouped_Incidents, Grouped_Risks


@app.cell
def __(Grouped_Incidents, Grouped_Risks, Year):
    Risks = Grouped_Risks(Year)
    Incidents = Grouped_Incidents(Year)
    return Incidents, Risks


@app.cell
def __(Incidents, Risks, mo):
    mo.md(f"""
    {mo.hstack([Risks,Incidents])}
    """
    ).center()
    return


@app.cell
def __(Incident_Proportions_Table, Risk_Proportions_Table, mo):
    Risk_Proportions_Explorer = mo.ui.data_explorer(Risk_Proportions_Table)
    Incident_Proportions_Explorer = mo.ui.data_explorer(Incident_Proportions_Table)
    return Incident_Proportions_Explorer, Risk_Proportions_Explorer


@app.cell
def __(Incident_Proportions_Explorer, Risk_Proportions_Explorer, mo):
    mo.md(
        f"""

        {mo.hstack([Risk_Proportions_Explorer,Incident_Proportions_Explorer])}

        """
    ).center()
    return


@app.cell
def __(mo):
    mo.md("<caption> Exploratory panel of pvalues from proportionality tests: left - risk arrangements, and right incidents.</caption>").style({'font-size':'16px'})
    return


@app.cell
def __(pd):
    Cyber_Incidents = pd.read_csv('assets\Incidents.csv')
    return (Cyber_Incidents,)


@app.cell
def __():
    Incident_query_2019 = """
    SELECT REF_DATE,Cyber_security_incidents, NAICS, VALUE
    FROM Cyber_Incidents
    WHERE NAICS IN (
        'Agriculture, forestry, fishing and hunting',
        'Hospitals',
        'Elementary and secondary schools'
        )
    AND REF_DATE='2019';
    """

    Incident_query_2021 = """
    SELECT REF_DATE,Cyber_security_incidents, NAICS, VALUE
    FROM Cyber_Incidents
    WHERE NAICS IN (
        'Agriculture, forestry, fishing and hunting',
        'Hospitals',
        'Elementary and secondary schools'
    )
    AND REF_DATE='2021';
    """
    return Incident_query_2019, Incident_query_2021


@app.cell
def __(Incident_query_2019, Incident_query_2021, db):
    Canada_Incident_Landscape_2019 = db.execute(Incident_query_2019).df()
    Canada_Incident_Landscape_2021 = db.execute(Incident_query_2021).df()
    return Canada_Incident_Landscape_2019, Canada_Incident_Landscape_2021


if __name__ == "__main__":
    app.run()
