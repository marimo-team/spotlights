# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.2.3",
#     "duckdb==1.1.2",
#     "plotly==5.24.1",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App(width="full")


@app.cell
def __(mo):
    mo.md("#Punnett Square App &ndash; <strong> Genotype </strong>").center()
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def __(pd):
    #Use index to reflect rownames of punnett squares
    Aa_Aa = pd.DataFrame(
        {
            'A': [1/4,2/4],
            'a': [2/4,1/4]
        }, 
            index=['A', 'a']
    )

    aa_aa = pd.DataFrame(
        {
            'a': [4/4, 4/4],
            'a': [4/4, 4/4]
        },
        index=['a', 'a']
    )

    AA_AA = pd.DataFrame(
        {
            'A': [4/4,4/4],
            'A': [4/4,4/4]
        }, 
            index = ['A','A']
    )  

    Aa_Bb = pd.DataFrame(
        {
            'AB': [1/16,2/16,2/16,4/16],
            'Ab': [2/16,1/16,4/16,2/16],
            'aB': [2/16,4/16,1/16,2/16],
            'ab': [4/16,2/16,2/16,1/16]
        }, 
            index = ['AB','Ab','aB','ab']
    )

    AA_BB = pd.DataFrame(
        {
            'AB': [8/16,8/16,8/16,8/16],
            'AB': [8/16,8/16,8/16,8/16],
            'AB': [8/16,8/16,8/16,8/16],
            'AB': [8/16,8/16,8/16,8/16]
        },
            index = ['aB','ab','aB','ab']
    ) 

    Ab_Ba = pd.DataFrame(
        {
            'Ab':[4/16,4/16,4/16,4/16],
            'Ab':[4/16,4/16,4/16,4/16],
            'bb':[4/16,4/16,4/16,4/16],
            'bb':[4/16,4/16,4/16,4/16]
        },
            index = ['BA','BA','aA','aA']
    )

    Ab_Bb = pd.DataFrame(
        {
            'AB':[1/16,2/16,2/16,4/16],
            'ab':[2/16,1/16,4/16,2/16],
            'bB':[2/16,4/16,1/16,2/16],
            'bb':[4/16,2/16,2/16,1/16]
        },
            index = ['AB','Ab','bB','bb']
    )
    return AA_AA, AA_BB, Aa_Aa, Aa_Bb, Ab_Ba, Ab_Bb, aa_aa


@app.cell
def __(AA_AA, AA_BB, Aa_Aa, Aa_Bb, Ab_Ba, Ab_Bb, aa_aa):
    Punnett_Options = {
        'AaxAa':Aa_Aa,
        'AAxAA':AA_AA,
        'aaxaa':aa_aa,
        'AaBbxAaBb':Aa_Bb,
        'AABBxaaBb':AA_BB,
        'AbbbxBaAA':Ab_Ba,
        'AbBbxAbBb':Ab_Bb
    }
    return (Punnett_Options,)


@app.cell
def __(mo):
    Punnett_Square_Chooser = mo.ui.dropdown(
        options = [
            'AaxAa',
            'AAxAA',
            'aaxaa',
            'AaBbxAaBb',
            'AABBxaaBb',
            'AbbbxBaAA',
            'AbBbxAbBb'
        ],value='AaxAa'
    )
    Punnett_Square_Chooser.style({'border-width':'10px','border-color':'crimson','background-color':'navy'}).center()
    return (Punnett_Square_Chooser,)


@app.cell
def __(Punnett_Options, Punnett_Square_Chooser):
    Punnett_Square = Punnett_Options[Punnett_Square_Chooser.value]
    return (Punnett_Square,)


@app.cell
def __(Most_Probable_Offspring, mo):
    mo.stat(
        value=str(Most_Probable_Offspring),
        label='Most probable outcome(s):',
        caption='Trait',
        bordered=True
    ).style({'border-width':'4px','background-color':'navy','border-color':'crimson'})
    return


@app.cell
def __(pd):
    #Restructure the punnett squares to turn them into either bar plots or pie charts, I'm not sure yet. 

    #AaxAa
    Heterozygous_Aa = pd.DataFrame(
        {
            'Genotype':['Aa','AA','aa'],
            'Probability':[2/4,1/4,1/4]
        }
    ) 

    #AAxAA 
    Homozygous_AA = pd.DataFrame(
        {
            'Genotype':['AA'],
            'Probability':[4/4]
        }
    )

    ##aaxaa
    Homozygous_aa = pd.DataFrame(
        {
            'Genotype':['aa'],
            'Probability':[4/4]
        }
    )

    #AaxBb 
    Heterozygous_Aa_Bb = pd.DataFrame(
        {
            'Genotype': ['AaBb','AABb','AaBB','Aabb','aaBb','AABB','AAbb','aaBB','aabb'],
            'Probability': [4/16,2/16,2/16,2/16,2/16,1/16,1/16,1/16,1/16]
        }  
    )

    #AABBxaaBb
    Heterozygous_AA_BB = pd.DataFrame(
        {
            'Genotype': ['AaBB','AaBb'],
            'Probability': [8/16,8/16]
        }
    )

    #AbbbxBaAA
    Heterozygous_Ab_Ba = pd.DataFrame(
        {
            'Genotype':['AbbA','bBbA','AabA','babA'],
            'Probability':[1/4,1/4,1/4,1/4]
        }
    )

    #AbBbxAbBb
    Heterozygous_Ab_Bb = pd.DataFrame(
        {
            'Genotype':['bAbB','AAbB','baBB','bAbb','bbbB','AABB','AAbb','bbBB','bbbb'],
            'Probability':[4/16,2/16,2/16,2/16,2/16,1/16,1/16,1/16,1/16]
        }
    )
    return (
        Heterozygous_AA_BB,
        Heterozygous_Aa,
        Heterozygous_Aa_Bb,
        Heterozygous_Ab_Ba,
        Heterozygous_Ab_Bb,
        Homozygous_AA,
        Homozygous_aa,
    )


@app.cell
def __(
    Heterozygous_AA_BB,
    Heterozygous_Aa,
    Heterozygous_Aa_Bb,
    Heterozygous_Ab_Ba,
    Heterozygous_Ab_Bb,
    Homozygous_AA,
    Homozygous_aa,
    px,
):
    #Return bar charts to corresponding crosses 
    def Allele_Bar_Plot(Zygosity):
        if Zygosity == 'AaxAa':
            return px.bar(Heterozygous_Aa,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
        if Zygosity == 'AAxAA':
            return px.bar(Homozygous_AA,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
        if Zygosity == 'aaxaa':
            return px.bar(Homozygous_aa,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
        if Zygosity == 'AaBbxAaBb':
            return px.bar(Heterozygous_Aa_Bb,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
        if Zygosity == 'AABBxaaBb':
            return px.bar(Heterozygous_AA_BB,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
        if Zygosity == 'AbbbxBaAA':
            return px.bar(Heterozygous_Ab_Ba,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
        if Zygosity == 'AbBbxAbBb':
            return px.bar(Heterozygous_Ab_Bb,x='Genotype',y='Probability',title='Bar Plot of Genotype Probabilities')
    return (Allele_Bar_Plot,)


@app.cell
def __(Allele_Bar_Plot, Punnett_Square_Chooser):
    Zygosity = Punnett_Square_Chooser.value
    Allele_Bar_Chart = Allele_Bar_Plot(Zygosity)
    return Allele_Bar_Chart, Zygosity


@app.cell
def __(Allele_Bar_Chart, Punnett_Heat_Map, mo):
    mo.md(
        f"""
        {mo.hstack([Allele_Bar_Chart,Punnett_Heat_Map])}
        """
    ).style({'background-color':'crimson','border-color':'navy','border-width':'15px'}).center()
    return


@app.cell
def __():
    import duckdb as db
    return (db,)


@app.cell
def __(db):
    Aa_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Heterozygous_Aa GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    AA_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Homozygous_AA GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    aa_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Homozygous_aa GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    Aa_Bb_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Heterozygous_Aa_Bb GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    AA_BB_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Heterozygous_AA_BB GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    Ab_Ba_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Heterozygous_Ab_Ba GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    Ab_Bb_Max = db.sql("SELECT Genotype,MAX(Probability) AS Max_Probability FROM Heterozygous_Ab_Bb GROUP BY Genotype ORDER BY Max_Probability DESC").df()
    return (
        AA_BB_Max,
        AA_Max,
        Aa_Bb_Max,
        Aa_Max,
        Ab_Ba_Max,
        Ab_Bb_Max,
        aa_Max,
    )


@app.cell
def __(AA_BB_Max, AA_Max, Aa_Bb_Max, Aa_Max, Ab_Ba_Max, Ab_Bb_Max, aa_Max):
    def Likely_Offspring(Zygosity):
        if Zygosity == 'AaxAa':
            return Aa_Max.Genotype[0]
        if Zygosity == 'AAxAA':
            return AA_Max.Genotype[0]
        if Zygosity == 'aaxaa':
            return aa_Max.Genotype[0]
        if Zygosity == 'AaBbxAaBb':
            return Aa_Bb_Max.Genotype[0]
        if Zygosity == 'AABBxaaBb':
            return [AA_BB_Max.Genotype[0],AA_BB_Max.Genotype[1]]
        if Zygosity =='AbbbxBaAA':
            return [Ab_Ba_Max.Genotype[0],Ab_Ba_Max.Genotype[1],Ab_Ba_Max.Genotype[2],Ab_Ba_Max.Genotype[3]]
        if Zygosity == 'AbBbxAbBb':
            return Ab_Bb_Max.Genotype[0]
    return (Likely_Offspring,)


@app.cell
def __(Likely_Offspring, Zygosity):
    Most_Probable_Offspring = Likely_Offspring(Zygosity)
    return (Most_Probable_Offspring,)


@app.cell
async def __():
    import micropip 
    await micropip.install("plotly")
    import plotly.express as px
    return micropip, px


@app.cell
def __(Punnett_Square, px):
    Punnett_Heat_Map = px.imshow(Punnett_Square,text_auto=True,title='Heatmap of Punnett Square')
    return (Punnett_Heat_Map,)


if __name__ == "__main__":
    app.run()
