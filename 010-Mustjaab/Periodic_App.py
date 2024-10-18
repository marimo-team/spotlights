# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas==2.2.3",
#     "periodictable==1.7.1",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""<h1> Periodic Table App </h1>""")
    return


@app.cell
def __():
    import marimo as mo 
    # pip install periodictable first before importing library
    import periodictable
    import pandas as pd
    return mo, pd, periodictable


@app.cell
def __(mo):
    Form = mo.ui.text(label="Atomic Number:").form()
    Form
    return (Form,)


@app.cell
def __(Form):
    Element = Form.value
    E = int(Element)
    return E, Element


@app.cell
def __(E, periodictable):
    element = periodictable.elements[E] 

    Property_Table = {
        'Property': [
            'Name',
            'Symbol',
            'Mass'
        ], 

        'Value': [
            element.name,
            element.symbol,
            element.mass
        ]
    }
    return Property_Table, element


@app.cell
def __(Property_Table, mo, pd):
    Dynamic_Table = pd.DataFrame(Property_Table)
    mo.ui.table(Dynamic_Table)
    return (Dynamic_Table,)


if __name__ == "__main__":
    app.run()
