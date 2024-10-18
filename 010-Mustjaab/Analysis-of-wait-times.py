# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas==2.2.3",
#     "plotly==5.24.1",
#     "marimo",
# ]
# ///
import marimo

__generated_with = "0.9.7-dev1"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    return mo, pd, px


@app.cell
def __(mo):
    mo.md(r"""<h1> Analysis of Wait Times for Priority Procedures </h1>""").style(
        {"background-color": "crimson"}
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Sections
        <ul>
            <li> General Overview</li>
            <li> 50th Percentiles </li>
            <li> Comparing 90th Percentiles </li>
        </ul>
        """
    )
    return


@app.cell
def __(pd):
    Wait_Times = pd.read_csv("Wait_Times_Data.csv")
    return (Wait_Times,)


@app.cell
def __(mo):
    mo.md(
        r"""
        ## General Overview
        <p> This notebook will compare the percentile of wait days (50th, and 90th) for various critical procedures in hospitals across Canada. Data was obtained from the <a href = "https://www.cihi.ca/en/access-data-and-reports/data-tables?sort_by=field_published_date_value&sort_order=DESC&page=1"> Canadian Institute for Health Information </a> (CIHI). Percentiles help us get a better understanding where a value in a dataset stands in comparison to others - is it on the lower end of the set? Is it on the higher end? Or is it smack in the middle? You can learn more about percentiles <a href = "https://statisticsbyjim.com/basics/percentiles/"> here. </a> </p>
        """
    )
    return


@app.cell
def __(mo):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM "Wait_Times"
        WHERE Indicator_result !='n/a'
        LIMIT 50
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"""<h2 id='Bladder'> 50th Percentiles </h2>""")
    return


@app.cell
def __(Bladder_Cancer_df, CABG_df, Lung_Cancer_df, mo):
    Operation_Options = {
        "Bladder Cancer Surgery": Bladder_Cancer_df,
        "CABG": CABG_df,
        "Lung Cancer Surgery": Lung_Cancer_df,
    }

    Operation_Choice = mo.ui.dropdown(
        options=["Bladder Cancer Surgery", "CABG", "Lung Cancer Surgery"],
        value="Bladder Cancer Surgery",
    )
    return Operation_Choice, Operation_Options


@app.cell
def __(Operation_Choice, Operation_Options):
    Operation_Bar = Operation_Options[Operation_Choice.value]
    return (Operation_Bar,)


@app.cell
def __(mo):
    Bladder_Cancer_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory !='Canada'
        AND Indicator = 'Bladder Cancer Surgery'
        AND Metric = '50th Percentile'
        AND Data_year IN ('2013', '2023')
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (Bladder_Cancer_df,)


@app.cell
def __(mo):
    CABG_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory !='Canada'
        AND Indicator = 'CABG'
        AND Metric = '50th Percentile'
        AND Data_year IN ('2013', '2023')
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (CABG_df,)


@app.cell
def __(mo):
    Lung_Cancer_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory !='Canada'
        AND Indicator = 'Lung Cancer Surgery'
        AND Metric = '50th Percentile'
        AND Data_year IN ('2013', '2023')
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (Lung_Cancer_df,)


@app.cell
def __(Operation_Choice):
    Operation_Choice
    return


@app.cell
def __(Operation_Bar, px):
    Bladder_Bar = px.bar(Operation_Bar,x='Province_territory',y='Indicator_result', color='Data_year', barmode='group')
    Bladder_Bar
    return (Bladder_Bar,)


@app.cell
def __(mo):
    mo.md(r"""<caption> Bar chart comparing 50th percentiles of wait times between 2013 and 2023 across provinces.</caption>""").style({'background-color':'brown','color':'white'})
    return


@app.cell
def __(mo):
    mo.md(r"""## Comparing 90th Percentiles""")
    return


@app.cell
def __(mo):
    Bladder_Cancer_90th_Percentile_2013_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory !='Canada'
        AND Indicator = 'Bladder Cancer Surgery'
        AND Metric = '90th Percentile'
        AND Data_year = '2013'
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (Bladder_Cancer_90th_Percentile_2013_df,)


@app.cell
def __(mo):
    Bladder_Cancer_90th_Percentile_2023_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory != 'Canada'
        AND Indicator = 'Bladder Cancer Surgery'
        AND Metric = '90th Percentile'
        AND Data_year IN ('2023')
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (Bladder_Cancer_90th_Percentile_2023_df,)


@app.cell
def __(mo):
    Lung_Cancer_90th_Percentile_2013_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory != 'Canada'
        AND Indicator = 'Lung Cancer Surgery'
        AND Metric = '90th Percentile'
        AND Data_year IN ('2013')
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (Lung_Cancer_90th_Percentile_2013_df,)


@app.cell
def __(mo):
    Lung_Cancer_90th_Percentile_2023_df = mo.sql(
        f"""
        SELECT Province_territory,Indicator,Metric,Data_year,Unit_of_measurement,Indicator_result
        FROM "Wait_Times"
        WHERE Province_territory != 'Canada'
        AND Indicator = 'Bladder Cancer Surgery'
        AND Metric = '90th Percentile'
        AND Data_year IN ('2023')
        And Unit_of_measurement = 'Days'
        AND Indicator_result !='n/a'
        ORDER BY Indicator_result ASC
        """, output=False
    )
    return (Lung_Cancer_90th_Percentile_2023_df,)


@app.cell
def __(
    Bladder_Cancer_90th_Percentile_2013_df,
    Bladder_Cancer_90th_Percentile_2023_df,
    Lung_Cancer_90th_Percentile_2013_df,
    Lung_Cancer_90th_Percentile_2023_df,
    px,
):
    Bladder_Cancer_2013 = px.pie(Bladder_Cancer_90th_Percentile_2013_df,values='Indicator_result', names='Province_territory')

    Bladder_Cancer_2023 = px.pie(Bladder_Cancer_90th_Percentile_2023_df,values='Indicator_result', names='Province_territory')

    Lung_Cancer_2013 = px.pie(Lung_Cancer_90th_Percentile_2013_df,values='Indicator_result', names='Province_territory')

    Lung_Cancer_2023 = px.pie(Lung_Cancer_90th_Percentile_2023_df,values='Indicator_result', names='Province_territory')
    return (
        Bladder_Cancer_2013,
        Bladder_Cancer_2023,
        Lung_Cancer_2013,
        Lung_Cancer_2023,
    )


@app.cell
def __(mo):
    Ten_Year_Journey = mo.ui.slider(2013,2023,10,value=2023, label = 'Ten Year Slider:')
    Ten_Year_Journey
    return (Ten_Year_Journey,)


@app.cell
def __(Ten_Year_Journey):
    Time_Parameter = Ten_Year_Journey.value
    return (Time_Parameter,)


@app.cell
def __(Bladder_Cancer_2013, Bladder_Cancer_2023):
    def Percentile_Time_Machine(Time_Parameter):
        if Time_Parameter == 2013:
            return Bladder_Cancer_2013
        if Time_Parameter == 2023:
            return Bladder_Cancer_2023
    return (Percentile_Time_Machine,)


@app.cell
def __(Percentile_Time_Machine, Time_Parameter):
    Percentile_Time_Machine(Time_Parameter)
    return


@app.cell
def __(mo):
    mo.md(r"""<caption> Pie charts of 90th percentile values for each province over a span of 10 years.</caption>""").style({'background-color':'indigo'})
    return


if __name__ == "__main__":
    app.run()
