# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "nltk==3.9.1",
#     "marimo",
#     "pandas==2.2.3",
#     "matplotlib==3.9.2",
#     "wordcloud==1.9.3",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""<h1> Word Clouds of Different Markets </h1>""")
    return


@app.cell
def __():
    import marimo as mo
    from wordcloud import WordCloud
    import nltk
    from nltk.corpus import stopwords
    import matplotlib.pyplot as plt
    import pandas as pd
    return WordCloud, mo, nltk, pd, plt, stopwords


@app.cell
def __(pd):
    #Currently a local csv file with pretend data on skills reflecting experiences for different stages in regulatory affairs
    Markets = pd.read_csv("Skills_for_Markets.csv")
    return (Markets,)


@app.cell
def __(stopwords):
    #Allows the word clouds to built using English vocabularoy 
    Stop = stopwords.words("english")
    return (Stop,)


@app.cell
def __(Markets, Stop, WordCloud):
    #Prepare word clouds so they can be linked with the slider options
    Entry_Skills = Markets['Entry Level'].values
    Entry_WC = WordCloud(stopwords = Stop).generate(str(Entry_Skills))

    Middle_Skills = Markets['Middle Level'].values
    Middle_WC = WordCloud(stopwords = Stop).generate(str(Middle_Skills))

    Senior_Skills = Markets['Senior Level'].values
    Senior_WC = WordCloud(stopwords = Stop).generate(str(Senior_Skills))
    return (
        Entry_Skills,
        Entry_WC,
        Middle_Skills,
        Middle_WC,
        Senior_Skills,
        Senior_WC,
    )


@app.cell
def __(mo):
    Levels = mo.ui.slider(1,3)
    return (Levels,)


@app.cell
def __(Levels):
    Skill_Level = Levels.value
    return (Skill_Level,)


@app.cell
def __(Levels, mo):
    mo.md(rf"Market: {Levels}")
    return


@app.cell
def __(Skill_Level):
    #"Translates" the numerical slider option into what experience level the word cloud is showing 
    def Market_Level(Skill_Level):
        if Skill_Level == 1: 
            return ('Entry Level Regulatory Affairs')
        if Skill_Level == 2:
            return ('Middle Level Regulatory Affairs')
        if Skill_Level == 3:
            return ('Senior Level Regulatory Affairs') 
    Experience = Market_Level(Skill_Level)
    return Experience, Market_Level


@app.cell
def __(Experience, mo):
    mo.md(rf"<strong> <center> {Experience} </center> </strong>")
    return


@app.cell
def __(Entry_WC, Middle_WC, Senior_WC, Skill_Level, plt):
    def Market_Word_Cloud(Skill_Level):
        if Skill_Level == 1:
            return plt.imshow(Entry_WC)
        if Skill_Level == 2:
            return plt.imshow(Middle_WC)
        if Skill_Level == 3:
            return plt.imshow(Senior_WC)

    Market_Word_Cloud(Skill_Level)
    return (Market_Word_Cloud,)


if __name__ == "__main__":
    app.run()
