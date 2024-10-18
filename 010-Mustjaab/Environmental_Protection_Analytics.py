# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "duckdb==1.1.2",
#     "pandas==2.2.3",
#     "plotly==5.24.1",
#     "scipy==1.14.1",
#     "stats-can==2.9.4",
#     "statsmodels==0.14.4",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""<h1> Oil and Gas Expenditure Analytics </h1>""")
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd 
    import plotly.express as px
    import stats_can as sc
    import duckdb
    from scipy.stats import pearsonr
    return duckdb, mo, pd, pearsonr, px, sc


@app.cell
def __(sc):
    # Bring in data of interest from Statistics Canada (copy/paste the 10-digit ID next to 'Table:')
    DF = sc.table_to_df('25-10-0064-01')
    return (DF,)


@app.cell
def __(DF, mo, pd):
    #Prepare table so it can be queried using SQL by replacing any columns that have spaces with underscores 
    Energy = DF.rename(columns={	
    'Capital expenditures and operating expenses':'Capital_expenditures_and_operating_expenses'}) 
    Energy_Table = pd.DataFrame(Energy)
    Energy_Data = mo.ui.table(Energy_Table)
    return Energy, Energy_Data, Energy_Table


@app.cell
def __(Energy_Table, duckdb):
    #Pull out the values for total capital from extraction and oil sands expenditures
    Total_Expenditures = duckdb.sql("SELECT Capital_expenditures_and_operating_expenses,VALUE AS Total_Capital FROM Energy_Table WHERE Capital_expenditures_and_operating_expenses = 'Total capital expenditures'").df()
    return (Total_Expenditures,)


@app.cell
def __(Energy_Table, duckdb):
    #Pull out the values for expenditures on extraction
    Extraction_Expenditures = duckdb.sql("SELECT Capital_expenditures_and_operating_expenses, VALUE AS Extraction_Expenditures FROM Energy_Table WHERE Capital_expenditures_and_operating_expenses = 'Oil and gas extraction expenditures'").df()
    return (Extraction_Expenditures,)


@app.cell
def __(Energy_Table, duckdb):
    #Pull out the values for expenditures on the oil sands
    Sands_Expenditures = duckdb.sql("SELECT Capital_expenditures_and_operating_expenses, VALUE AS Sands_Expenditures FROM Energy_Table WHERE Capital_expenditures_and_operating_expenses = 'Oil sands expenditures'").df()
    return (Sands_Expenditures,)


@app.cell
def __(Sands_Expenditures, Total_Expenditures, pd):
    #Create a dataframe for the total capital and oil sand expenditures
    C_and_S = {
        "Total Capital":Total_Expenditures['Total_Capital'],
        "Expenditures":Sands_Expenditures['Sands_Expenditures']
    }
    Capital_and_Sands = pd.DataFrame(C_and_S)
    return C_and_S, Capital_and_Sands


@app.cell
def __(Extraction_Expenditures, Total_Expenditures, pd):
    #Also create a dataframe for total capital and extraction expenditures
    C_and_E = {
    "Total Capital":Total_Expenditures['Total_Capital'],
     "Expenditures":Extraction_Expenditures['Extraction_Expenditures']
    }
    Capital_and_Extraction = pd.DataFrame(C_and_E)
    return C_and_E, Capital_and_Extraction


@app.cell
def __(Capital_and_Extraction, Capital_and_Sands, mo):
    #Prepare options for the drop down so either of the two dataframes can be selected
    Expenditure_Options = {
        'Capital and Extraction':Capital_and_Extraction, 
        'Capital and Sands': Capital_and_Sands
    } 

    Expenditure_Choices = mo.ui.dropdown(
        options=[
            'Capital and Extraction',
            'Capital and Sands'
        ], value='Capital and Extraction'
    ) 
    Expenditure_Choices 
    mo.md(
        rf"""This is a summary of **{Expenditure_Choices}**
        """
    )
    return Expenditure_Choices, Expenditure_Options


@app.cell
def __(Expenditure_Choices, Expenditure_Options):
    Expenditure_Visualization = Expenditure_Options[Expenditure_Choices.value]
    return (Expenditure_Visualization,)


@app.cell
def __(Expenditure_Visualization, pearsonr):
    Pearson_Test = pearsonr(Expenditure_Visualization['Total Capital'],Expenditure_Visualization['Expenditures'])
    return (Pearson_Test,)


@app.cell
def __(Expenditure_Visualization, Pearson_Test, mo, pd):
    #A skeleton statistics summary table that returns exploratory data analytics for whatever option is chosen from the drowndown list. 
    Summary_Table = {
        "Variable": [
            'Mean Total Capital',
            'Mean Expenditure',
            'Median Total Capital',
            'Median Expenditure', 
            'Total Capital Skewness',
            'Expenditure Skewness',
            "Correlation pvalue"
        ],
        "Value": [
            Expenditure_Visualization['Total Capital'].mean(),
            Expenditure_Visualization['Expenditures'].mean(),
            Expenditure_Visualization['Total Capital'].median(),
            Expenditure_Visualization['Expenditures'].median(),
            Expenditure_Visualization['Total Capital'].skew(),
            Expenditure_Visualization['Expenditures'].skew(),
            Pearson_Test.pvalue
        ]

    }
    Summary_Statistics = pd.DataFrame(Summary_Table)
    mo.ui.table(Summary_Statistics)
    return Summary_Statistics, Summary_Table


@app.cell
def __(Expenditure_Visualization, px):
    #Displays the scatter plot for whatever option is chosen 
    px.scatter(Expenditure_Visualization,y='Total Capital', x ='Expenditures',trendline='ols')
    return


@app.cell
def __(Expenditure_Visualization, px):
    #Displays the boxplot for whatever option is chosen
    px.box(Expenditure_Visualization)
    return


if __name__ == "__main__":
    app.run()
