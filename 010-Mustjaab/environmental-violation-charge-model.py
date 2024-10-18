# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "plotly==5.24.1",
#     "pandas==2.2.3",
#     "marimo",
#     "altair==5.4.1",
#     "scikit-learn==1.5.2",
#     "statsmodels==0.14.4",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("<h1> <center> Environmental Violation Charge Model </center></h1>").style({'background-color':'seagreen'})
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import altair as alt
    from statsmodels.formula.api import ols
    from statsmodels.stats.anova import anova_lm
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.feature_extraction.text import TfidfVectorizer
    import plotly.express as px
    return (
        RandomForestRegressor,
        TfidfVectorizer,
        alt,
        anova_lm,
        mo,
        ols,
        pd,
        px,
        train_test_split,
    )


@app.cell
def __(pd):
    Environmental_Violation_Data = pd.read_csv("https://raw.githubusercontent.com/Mustjaab/Environmental-Protection-Model/main/Environmental_Protection_Data.csv")
    Environmental_Violation_Data.columns = Environmental_Violation_Data.columns.str.strip()
    return (Environmental_Violation_Data,)


@app.cell
def __(Environmental_Violation_Data, alt):
    Sectors_Boxplot = alt.Chart(Environmental_Violation_Data).mark_boxplot(extent='min-max').encode(
        alt.X('Sector'),
        alt.Y('Order Amount of Environmental Penalty per Violation')
    ) 

    Municipalities_Boxplot = alt.Chart(Environmental_Violation_Data).mark_boxplot(extent='min-max').encode(
        alt.X('Municipality'),
        alt.Y('Order Amount of Environmental Penalty per Violation')
    )
    return Municipalities_Boxplot, Sectors_Boxplot


@app.cell
def __(Environmental_Violation_Data, anova_lm, ols):
    Feature_Model = ols(
    'Q("Order Amount of Environmental Penalty per Violation") ~ Q("Region") + Q("Sector") + Q("Municipality") + Q("District")', Environmental_Violation_Data).fit()
    Feature_ANOVA_Table = anova_lm(Feature_Model, typ=2)
    return Feature_ANOVA_Table, Feature_Model


@app.cell
def __(Environmental_Violation_Data, TfidfVectorizer):
    Features = Environmental_Violation_Data[['Sector', 'Municipality']]
    Features_text = Features.astype(str).apply(lambda row: ' '.join(row), axis=1)
    vectorizer = TfidfVectorizer()
    vectorizer.fit(Features_text)
    Features_tfidf = vectorizer.transform(Features_text)
    return Features, Features_text, Features_tfidf, vectorizer


@app.cell
def __(Environmental_Violation_Data, Features_tfidf, train_test_split):
    X_train, X_test, y_train, y_test = train_test_split(
        Features_tfidf,
        Environmental_Violation_Data['Order Amount of Environmental Penalty per Violation'],
        test_size=0.2, random_state=42
    )
    return X_test, X_train, y_test, y_train


@app.cell
def __(RandomForestRegressor, X_train, y_train):
    Violation_Classifier = RandomForestRegressor(random_state=42)
    Violation_Classifier.fit(X_train, y_train)
    return (Violation_Classifier,)


@app.cell
def __():
    def Predict_Violation(feature1, feature2, Violation_Classifier, vectorizer):
        # Convert the features into text format
        features_text = ' '.join([str(feature1), str(feature2)])

        # Convert text data into TF-IDF representation
        features_tfidf = vectorizer.transform([features_text])

        # Make predictions using the RandomForestRegressor model
        predicted_value = Violation_Classifier.predict(features_tfidf)

        return predicted_value[0]
    return (Predict_Violation,)


@app.cell
def __(mo):
    Sectors_Dropdown = mo.ui.dropdown(
        options = ['Iron & Steel', 'Metal Mining', 'Petroleum', 'Industrial Minerals',
           'Inorganic Chemical', 'Electric Power', 'Inorganic Chemicals',
           'Pulp & Paper', 'Organic Chemical'],
        value = 'Industrial Minerals',
        label = 'Sector:'
    )

    Municipality_Dropdown = mo.ui.dropdown(
        options = ['Sault Ste Marie','South Porcupine, Timmins',
           'Township of Cochrane', 'Sarnia', 'Haldimand County',
           'Reeves Township', 'St. Clair Township', 'Kearney',
           'Unorganized Township of Reeves',
           'Unorganized, District of Thunder Bay', 'Matachewan',
           'Port Colborne', 'Espanola', 'St. Marys', 'Kincardine',
           'Town of Kearney', 'District of Algoma', 'District of Thunder Bay',
           'South Porcupine', 'Tully Township', 'Black River – Matheson',
           'Zorra', 'Hamilton', 'Kapuskasing', 'Timmins', 'Quinte West',
           'Niagara Falls'],
        value = 'Hamilton',
        label = 'Municipality:'
    )
    mo.hstack([
        Sectors_Dropdown,
        Municipality_Dropdown
    ])
    return Municipality_Dropdown, Sectors_Dropdown


@app.cell
def __(Municipality_Dropdown, Sectors_Dropdown):
    Sector = Sectors_Dropdown.value
    Municipality = Municipality_Dropdown.value
    return Municipality, Sector


@app.cell
def __(
    Municipality,
    Predict_Violation,
    Sector,
    Violation_Classifier,
    mo,
    vectorizer,
):
    Predicted_Violation = Predict_Violation(Sector,Municipality,Violation_Classifier, vectorizer)

    mo.md(rf"Predicted Violation Charge ($): {round(Predicted_Violation,2)}").style({'background-color':'purple','border-width':'2px','border-color':'white'}).center()
    return (Predicted_Violation,)


@app.cell
def __(Feature_ANOVA_Table, mo):
    mo.hstack([
        mo.vstack([
        mo.md("<h2> ANOVA Table </h2>").style({'background-color':'brown'}),
        mo.ui.table(Feature_ANOVA_Table)
    ])
    ]).center()
    return


@app.cell
def __(Municipalities_Boxplot, Sectors_Boxplot, mo):
    mo.hstack([    
        mo.vstack([
        mo.md("<h2> Boxplot of Violation Charges by Sector </h2>")
            .style({'background-color':'maroon'}),
        mo.ui.altair_chart(Sectors_Boxplot)
    ]),
        mo.vstack([
        mo.md("<h2> Boxplot of Violation Charges by Municipality </h2>")
            .style({'background-color':'teal'}),
        mo.ui.altair_chart(Municipalities_Boxplot)
    ])
    ]).center()
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        <footer> Data trained using <a href="https://data.ontario.ca/dataset/environmental-penalty-annual-report">
        Ontario's Environmental Protection Reports</a>.
        </footer>
        """
    ).style({'font-size':'18px'})
    return


if __name__ == "__main__":
    app.run()
