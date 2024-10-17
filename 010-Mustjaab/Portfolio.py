# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
import marimo

__generated_with = "0.9.7-dev1"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        """
        <h1> <center> Muhammad Mustjaab </center> </h1>
        <h2> <center> Portfolio </center> </h2>
        """
    ).center()
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md("""<h2> Projects </h2>""")
    return


@app.cell
def __(mo):
    mo.hstack([
    mo.md(
        """
        <h3> 
        <a href='https://marimo.app/l/9srgey'> Post Approval Study Recommender </a>
        </h3>

        Description: 
        <ul>
            <li> Recommends Post Approval Studies based on medical specialties </li> 
            <li> Selected number of recommended studies to display </li>
        </ul>
        """
    ).style({"border-width":'2px','border-color':'crimson','overflow':'auto'}),
        mo.md(
        """
        <h3> <a href='https://marimo.app/l/2vxkys'> Differential Privacy and GC Content </a> </h3>
        Description: 
    <ul>
        <li> Determine the GC content of user generated nucleotide sequences </li> 
        <li> Compare normal GC content with application of differential privacy </li>
    </ul>
        """).style({'border-width':'2px','border-color':'gold','overflow':'auto'}),
        mo.md(
        """
        <h3> <a href='https://marimo.app/l/1hl9um'> Warning Letter Classifier </a> </h3>
        Description: 
    <ul>
        <li> Classifies warning letters to different offices issuing the letter </li> 
        <li> Predicts subject of the warning letter based on the office </li>
    </ul>
        """).style({'border-width':'2px','border-color':'violet','overflow':'auto'})
    ]
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        <h2> Github: </h2>
        <a href="https://github.com/Mustjaab"> https://github.com/Mustjaab </a>
        <h2> Education </h2>
        """
    )
    return


@app.cell
def __(mo):
    mo.carousel(
        [
            mo.md(
            """
        <h1> BSc|General Sciences|University of Waterloo </h1>
        <ul>
            <li> Biostatistics </li>
            <li> Computational Biology </li>
            <li> Genomics </li> 
            <li> Ecological Consequences of Climate Change </li> 
            <li> Human Physiolgy </li>
        </ul> 
            """
            ),
            mo.md(
            """
        <h1>Graduate Certificate|Regulatory Affairs|Humber College</h1>
        <ul>
            <li> Medical Devices </li>
            <li> Emerging Biotechnology</li>
            <li> Management of Regulatory Submissions (and Management of Global Regulatory Submission) </li>
            <li> Pharmacology and Pathophysiology</li>
        </ul>
            """)
        ]
    ).style({"border-width":'4px','border-color':'seagreen'})
    return


if __name__ == "__main__":
    app.run()
