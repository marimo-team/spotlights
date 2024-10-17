# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas==2.2.3",
#     "scikit-learn==1.5.2",
#     "marimo",
#     "plotly==5.24.1",
#     "pyodide-py==0.26.2",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""<h1> Post Approval Study Recommender</h1>""")
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import micropip
    import pyodide
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel
    return TfidfVectorizer, linear_kernel, micropip, mo, pd, pyodide


@app.cell
async def __(micropip):
    await micropip.install("plotly")
    import plotly.express as px
    return (px,)


@app.cell
def __(pd):
    PAS_FDA = "https://raw.githubusercontent.com/Mustjaab/PAS-Recommender/main/Post_Approval_Studies.csv" # csv file also exists under assets folder
    PAS_FDA = pd.read_csv(PAS_FDA, header=0)
    return (PAS_FDA,)


@app.cell
def __(mo):
    Speciality_Selection = mo.ui.dropdown(
        options=['Cardiovascular', 'Clinical Chemistry', 'Neurology', 'Ophthalmic',
           'General & Plastic Surgery', 'Orthopedic', 'General Hospital',
           'Toxicology', 'Obstetrics/Gynecology', 'Radiology',
           'Ear Nose & Throat', 'Pathology', 'Anesthesiology',
           'Gastroenterology/Urology'],
        value='Cardiovascular',
        label='Medical Specialty'
    )

    Top_Results = mo.ui.slider(2,11,1,label='Top Results:')
    return Speciality_Selection, Top_Results


@app.cell
def __(Speciality_Selection, Top_Results):
    top_results = Top_Results.value
    Medical_Specailty = Speciality_Selection.value
    return Medical_Specailty, top_results


@app.cell
def __(Speciality_Selection, Top_Results, mo):
    mo.hstack([Speciality_Selection,Top_Results]).center()
    return


@app.cell
def __(PAS_FDA, TfidfVectorizer):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(PAS_FDA['Study_Name'])
    return tfidf, tfidf_matrix


@app.cell
def __(linear_kernel, tfidf_matrix):
    cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)
    return (cosine_sim,)


@app.cell
def __(PAS_FDA, cosine_sim):
    def get_recommendations(Medical_Specialty,top_results,cosine_sim=cosine_sim):
        idx = PAS_FDA.index[PAS_FDA['Medical_Specialty'] ==
        Medical_Specialty].tolist()[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_results]
        Study_indices = [i[0] for i in sim_scores]
        return PAS_FDA['Study_Name'].iloc[Study_indices]
    return (get_recommendations,)


@app.cell
def __(Medical_Specailty, get_recommendations, mo, pd, top_results):
    Study_Recommendation = get_recommendations(Medical_Specailty,top_results)
    Study_Recommendation = pd.DataFrame(Study_Recommendation)
    Study_Recommendation = Study_Recommendation.rename(columns={'Study_Name':'Recommended Study'})
    mo.ui.table(Study_Recommendation)
    return (Study_Recommendation,)


@app.cell
def __(mo):
    mo.md("""<footer> Data obtained from the <a href="https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas.cfm"> FDA </a>""")
    return


if __name__ == "__main__":
    app.run()
