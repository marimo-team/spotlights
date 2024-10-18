# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "scikit-learn==1.5.2",
#     "marimo",
#     "pandas==2.2.3",
#     "plotly==5.24.1",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""<h1> <center> Warning Letter Classification Model </center> </h1>""")
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    import micropip
    return (
        MultinomialNB,
        TfidfVectorizer,
        micropip,
        mo,
        pd,
        train_test_split,
    )


@app.cell
async def __(micropip):
    await micropip.install('plotly')
    import plotly.express as px
    return (px,)


@app.cell
def __(pd):
    #Get data from the github repository as WASM doesn't load locally stored files
    Warning_Letter_Data = pd.read_csv("https://raw.githubusercontent.com/Mustjaab/warning-letter-analysis/main/warning-letters.csv")
    Subject = pd.DataFrame(Warning_Letter_Data['Issuing Office'].unique())
    return Subject, Warning_Letter_Data


@app.cell
def __(Warning_Letter_Data, train_test_split):
    X_train, X_test, y_train, y_test = train_test_split(Warning_Letter_Data['Issuing Office'], Warning_Letter_Data['Subject'], test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train


@app.cell
def __(TfidfVectorizer, X_test, X_train):
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    return X_test_tfidf, X_train_tfidf, vectorizer


@app.cell
def __(MultinomialNB, X_train_tfidf, y_train):
    nb_classifier = MultinomialNB()
    nb_classifier.fit(X_train_tfidf, y_train)
    return (nb_classifier,)


@app.cell
def __(nb_classifier, vectorizer):
    def issuing_office(office):
        office_tfidf = vectorizer.transform([office])
        predicted_office = nb_classifier.predict(office_tfidf)
        return predicted_office[0]
    return (issuing_office,)


@app.cell
def __(Offices):
    Office_Option = Offices.value
    return (Office_Option,)


@app.cell
def __(mo):
    Offices = mo.ui.dropdown(
        options = [
            'Center for Tobacco Products',
            'Center for Drug Evaluation and Research | CDER',
            'Division of West Coast Imports',
            'Division of Southwest Imports',
            'Division of Human and Animal Food Operations East III',
            'Center for Devices and Radiological Health'
        ],
        value = 'Division of West Coast Imports',
        label='Office:'
    )
    Offices
    return (Offices,)


@app.cell
def __(Office_Option, issuing_office, mo):
    Predicted_Subject = issuing_office(Office_Option)
    Predicted_Subject = mo.md(f"{Predicted_Subject}").style({'border-width':'2px','border-color':'crimson','background-color':'navy','font-size':'16px'})
    mo.md(rf"Predicted Subject of Letter: {Predicted_Subject}").center()
    return (Predicted_Subject,)


@app.cell
def __(Warning_Letter_Data, pd):
    Offices_of_Interst = [
            'Center for Tobacco Products',
            'Center for Drug Evaluation and Research | CDER',
            'Division of West Coast Imports',
            'Division of Southwest Imports',
            'Division of Human and Animal Food Operations East III',
            'Center for Devices and Radiological Health'
        ]

    Selected_Offices_Data = Warning_Letter_Data[Warning_Letter_Data['Issuing Office'].isin(Offices_of_Interst)]

    Selected_Offices_Data['Letter Issue Date'] = pd.to_datetime(Selected_Offices_Data['Letter Issue Date'])

    Selected_Offices_Data['Month'] = Selected_Offices_Data['Letter Issue Date'].dt.strftime('%Y-%m')
    return Offices_of_Interst, Selected_Offices_Data


@app.cell
def __(Selected_Offices_Data):
    Office_Counts = Selected_Offices_Data.groupby(['Month', 'Issuing Office']).size().reset_index(name='Count')
    return (Office_Counts,)


@app.cell
def __(Office_Counts, Offices, px):
    fig = px.line(Office_Counts, x='Month', y='Count', color='Issuing Office', title='Issuing Office Count')

    for trace_name in fig.data:
        if trace_name.name != Offices.value:
            trace_name.visible = 'legendonly'

    fig
    return fig, trace_name


if __name__ == "__main__":
    app.run()
