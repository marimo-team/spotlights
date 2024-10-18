# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "statsmodels==0.14.4",
#     "pandas==2.2.3",
#     "scipy==1.14.1",
#     "marimo",
#     "altair==5.4.1",
# ]
# ///
import marimo

__generated_with = "0.9.7-dev1"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("<h1><center> Monitoring Flow of GHG Emissions </h1> </center> <br>").style({'background-color':'green'})
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    from scipy.stats import f_oneway
    from statsmodels.tsa.stattools import adfuller
    return adfuller, f_oneway, mo, pd


@app.cell
async def __():
    import micropip
    await micropip.install("altair")
    import altair as alt
    return alt, micropip


@app.cell
def __(
    Canada_Pesticide_Stack,
    Canada_Pharmaceutical_Stack,
    Canada_Transportation_Stack,
    mo,
):
    mo.md(
        rf""""
    {mo.hstack([Canada_Pharmaceutical_Stack,Canada_Pesticide_Stack,Canada_Transportation_Stack])}
    """
    ).center()
    return


@app.cell
def __(
    Ontario_Pesticide_Stack,
    Ontario_Pharmaceutical_Stack,
    Ontario_Transportation_Stack,
    mo,
):
    mo.md(
        rf""""
    {mo.hstack([Ontario_Pharmaceutical_Stack,Ontario_Pesticide_Stack,Ontario_Transportation_Stack])}
    """
    ).center()
    return


@app.cell
def __(pd):
    Start_Date = '2009'
    End_Date = '2022'

    Date_Range = pd.date_range(start=Start_Date, end=End_Date, freq='Y')
    return Date_Range, End_Date, Start_Date


@app.cell
def __(Date_Range, pd):
    Canada_Pharmaceutical = pd.DataFrame(
        {
            'REF_DATE': Date_Range,
            'VALUE':[
                250, 
                247, 
                221, 
                235, 
                190, 
                258, 
                263, 
                426, 
                297, 
                277, 
                274, 
                271, 
                264
            ]
        }
    )

    Canada_Pesticide = pd.DataFrame(
        {
            'REF_DATE':Date_Range,
            'VALUE':[
                5539,
                5869,
                6168,
                6168,
                6758,
                6342,
                6722,
                6987,
                6216,
                5881,
                6115,
                6050,
                6071
            ]
        }
    )

    Canada_Transportation = pd.DataFrame(
        {
            'REF_DATE':Date_Range,
            'VALUE':[
                1357,
                1381,
                1310,
                1295,
                1199,
                933,
                1276,
                1388,
                1635,
                1617,
                1440,
                1188,
                1228
            ]
        }
    )

    Ontario_Pharmaceutical = pd.DataFrame(
        {
            'REF_DATE':Date_Range,
            'VALUE':[
                154,
                153,
                137,
                151,
                121,
                176,
                163,
                326,
                176,
                166,
                177,
                184,
                185
            ]
        }
    )

    Ontario_Pesticide = pd.DataFrame(
        {
           'REF_DATE':Date_Range,
           'VALUE':[
            754,
            575,
            671,
            768,
            1120,
            1140,
            950,
            1179,
            1112,
            387,
            399,
            387,
            389
            ]
        }
    )

    Ontario_Transportation = pd.DataFrame(
        {
            'REF_DATE':Date_Range,
            'VALUE':[
                526,
                516,
                445,
                461,
                519,
                410,
                636,
                618,
                769,
                712,
                642,
                488,
                485,
            ]
        }
    )
    return (
        Canada_Pesticide,
        Canada_Pharmaceutical,
        Canada_Transportation,
        Ontario_Pesticide,
        Ontario_Pharmaceutical,
        Ontario_Transportation,
    )


@app.cell
def __(
    Canada_Pesticide,
    Canada_Pharmaceutical,
    Canada_Transportation,
    Ontario_Pesticide,
    Ontario_Pharmaceutical,
    Ontario_Transportation,
    adfuller,
):
    Canada_ADF_Pharmaceutical = adfuller(Canada_Pharmaceutical['VALUE'])
    Canada_ADF_Pesticide = adfuller(Canada_Pesticide['VALUE'])
    Canada_ADF_Transportation = adfuller(Canada_Transportation['VALUE']) 

    Ontario_ADF_Pharmaceutical = adfuller(Ontario_Pharmaceutical['VALUE'])
    Ontario_ADF_Pesticide = adfuller(Ontario_Pesticide['VALUE'])
    Ontario_ADF_Transportation = adfuller(Ontario_Transportation['VALUE'])
    return (
        Canada_ADF_Pesticide,
        Canada_ADF_Pharmaceutical,
        Canada_ADF_Transportation,
        Ontario_ADF_Pesticide,
        Ontario_ADF_Pharmaceutical,
        Ontario_ADF_Transportation,
    )


@app.cell
def __(
    Canada_ADF_Pesticide,
    Canada_ADF_Pharmaceutical,
    Canada_ADF_Transportation,
    Canada_Pesticide,
    Canada_Pharmaceutical,
    Canada_Transportation,
    Ontario_ADF_Pesticide,
    Ontario_ADF_Pharmaceutical,
    Ontario_ADF_Transportation,
    Ontario_Pesticide,
    Ontario_Pharmaceutical,
    Ontario_Transportation,
    pd,
):
    Canada_Pharmaceutical_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Canada_Pharmaceutical['VALUE'].mean(),
                Canada_Pharmaceutical['VALUE'].median(),
                Canada_Pharmaceutical['VALUE'].skew(),
                Canada_ADF_Pharmaceutical[1]
            ]
        }
    )

    Canada_Pesticide_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Canada_Pesticide['VALUE'].mean(),
                Canada_Pesticide['VALUE'].median(),
                Canada_Pesticide['VALUE'].skew(),
                Canada_ADF_Pesticide[1]
            ]
        }
    )


    Canada_Transportation_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Canada_Transportation['VALUE'].mean(),
                Canada_Transportation['VALUE'].median(),
                Canada_Transportation['VALUE'].skew(),
                Canada_ADF_Transportation[1]
            ]
        }
    )

    Ontario_Pharmaceutical_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Ontario_Pharmaceutical['VALUE'].mean(),
                Ontario_Pharmaceutical['VALUE'].median(),
                Ontario_Pharmaceutical['VALUE'].skew(),
                Ontario_ADF_Pharmaceutical[1]
            ]
        }
    )


    Ontario_Pharmaceutical_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Ontario_Pharmaceutical['VALUE'].mean(),
                Ontario_Pharmaceutical['VALUE'].median(),
                Ontario_Pharmaceutical['VALUE'].skew(),
                Ontario_ADF_Pharmaceutical[1]
            ]
        }
    )

    Ontario_Pesticide_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Ontario_Pesticide['VALUE'].mean(),
                Ontario_Pesticide['VALUE'].median(),
                Ontario_Pesticide['VALUE'].skew(),
                Ontario_ADF_Pesticide[1]
            ]
        }
    )

    Ontario_Transportation_Summary = pd.DataFrame(
        {
            'Statistic':[
                'Mean',
                'Median',
                'Skewness',
                'ADF pvalue'
            ],
            'Value':[
                Ontario_Transportation['VALUE'].mean(),
                Ontario_Transportation['VALUE'].median(),
                Ontario_Transportation['VALUE'].skew(),
                Ontario_ADF_Transportation[1]
            ]
        }
    )
    return (
        Canada_Pesticide_Summary,
        Canada_Pharmaceutical_Summary,
        Canada_Transportation_Summary,
        Ontario_Pesticide_Summary,
        Ontario_Pharmaceutical_Summary,
        Ontario_Transportation_Summary,
    )


@app.cell
def __(
    Canada_Pesticide,
    Canada_Pharmaceutical,
    Canada_Transportation,
    Ontario_Pesticide,
    Ontario_Pharmaceutical,
    Ontario_Transportation,
    alt,
    mo,
):
    Pharmaceutical_Time_Series = mo.ui.altair_chart(alt.Chart(Canada_Pharmaceutical).mark_point().encode(
        x='REF_DATE',
        y='VALUE'
    ))

    Pesticide_Time_Series = mo.ui.altair_chart(alt.Chart(Canada_Pesticide).mark_point().encode(
        x='REF_DATE',
        y='VALUE'
    ))

    Transportation_Time_Series = mo.ui.altair_chart(alt.Chart(Canada_Transportation).mark_point().encode(
        x='REF_DATE',
        y='VALUE'
    ))


    Ontario_Pharmaceutical_Time_Series = mo.ui.altair_chart(
        alt.Chart(Ontario_Pharmaceutical).mark_point().encode(
            x='REF_DATE',
            y='VALUE'
    ))

    Ontario_Pesticide_Time_Series = mo.ui.altair_chart(
        alt.Chart(Ontario_Pesticide).mark_point().encode(
            x='REF_DATE',
            y='VALUE'
        )
    )

    Ontario_Transportation_Time_Series = mo.ui.altair_chart(
        alt.Chart(Ontario_Transportation).mark_point().encode(
            x='REF_DATE',
            y='VALUE'
        )
    )
    return (
        Ontario_Pesticide_Time_Series,
        Ontario_Pharmaceutical_Time_Series,
        Ontario_Transportation_Time_Series,
        Pesticide_Time_Series,
        Pharmaceutical_Time_Series,
        Transportation_Time_Series,
    )


@app.cell
def __(
    Canada_Pesticide_Summary,
    Canada_Pharmaceutical_Summary,
    Canada_Transportation_Summary,
    Ontario_Pesticide_Summary,
    Ontario_Pesticide_Time_Series,
    Ontario_Pharmaceutical_Summary,
    Ontario_Pharmaceutical_Time_Series,
    Ontario_Transportation_Summary,
    Ontario_Transportation_Time_Series,
    Pesticide_Time_Series,
    Pharmaceutical_Time_Series,
    Transportation_Time_Series,
    mo,
):
    Canada_Pharmaceutical_Stack = mo.vstack(
    [
    mo.md("<h2> Canada Pharmaceuticals </h2>").style({'background-color':'crimson','float':'left'}),
    Pharmaceutical_Time_Series,
     mo.ui.table(Pharmaceutical_Time_Series.value),
     mo.ui.table(Canada_Pharmaceutical_Summary)
    ])

    Canada_Pesticide_Stack = mo.vstack(
    [
    mo.md("<h2> Canada Pesticide Manufacturing </h2>").style({'background-color':'crimson','float':'left'}),
    Pesticide_Time_Series,
     mo.ui.table(Pesticide_Time_Series.value),
     mo.ui.table(Canada_Pesticide_Summary)
    ])

    Canada_Transportation_Stack = mo.vstack(
    [
    mo.md("<h2> Canada Transportation Engineering </h2>").style({'background-color':'crimson','float':'left'}),    
    Transportation_Time_Series,
     mo.ui.table(Transportation_Time_Series.value),
     mo.ui.table(Canada_Transportation_Summary)
    ])


    Ontario_Pharmaceutical_Stack = mo.vstack(
        [
            mo.md("<h2> Ontario Pharmaceuticals </h2>").style({'background-color':'navy','float':'left'}),
            Ontario_Pharmaceutical_Time_Series,
            mo.ui.table(Ontario_Pharmaceutical_Time_Series.value),
            mo.ui.table(Ontario_Pharmaceutical_Summary)
        ]
    )

    Ontario_Pesticide_Stack = mo.vstack(
        [
            mo.md("<h2> Ontario Pesticide Manufacturing </h2>").style({'background-color':'navy','float':'left'}),
            Ontario_Pesticide_Time_Series,
            mo.ui.table(Ontario_Pesticide_Time_Series.value),
            mo.ui.table(Ontario_Pesticide_Summary)
        ]
    )

    Ontario_Transportation_Stack = mo.vstack(
        [
            mo.md("<h2> Ontario Transportation Engineering </h2>").style({'background-color':'navy','float':'left'}),
            Ontario_Transportation_Time_Series,
            mo.ui.table(Ontario_Transportation_Time_Series.value),
            mo.ui.table(Ontario_Transportation_Summary)
        ]
    )
    return (
        Canada_Pesticide_Stack,
        Canada_Pharmaceutical_Stack,
        Canada_Transportation_Stack,
        Ontario_Pesticide_Stack,
        Ontario_Pharmaceutical_Stack,
        Ontario_Transportation_Stack,
    )


@app.cell
def __(mo):
    mo.md("""<footer> Data obtained from <a href="https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810009701&cubeTimeFrame.startYear=2009&cubeTimeFrame.endYear=2021&referencePeriods=20090101%2C20210101"> Statistics Canada  </a> </footer>""")
    return


if __name__ == "__main__":
    app.run()
