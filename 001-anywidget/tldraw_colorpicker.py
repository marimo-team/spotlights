# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "numpy",
#     "tldraw",
# ]
# ///

import marimo

__generated_with = "0.8.9"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    plt.style.use('_mpl-gallery')
    return mo, np, plt


@app.cell
def __(mo):
    from tldraw import ReactiveColorPicker

    widget = mo.ui.anywidget(ReactiveColorPicker())
    return ReactiveColorPicker, widget


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        This example by [Jan-Hendrik Muller](https://x.com/kolibril13?lang=en) uses [anywidget](https://anywidget.dev) to make
        a reactive colorpicker! Drag the arrow across the boxes, and watch the scatterplot change colors.

        anywidget is a Python library that makes it easy to make portable widgets; marimo has standardized on anywidget
        for its plugin API. Learn more at [our docs](https://docs.marimo.io/guides/integrating_with_marimo/custom_ui_plugins.html#custom-widget).
        """
    )
    return


@app.cell
def __(np):
    # make the data
    np.random.seed(3)
    x = 4 + np.random.normal(0, 2, 24)
    y = 4 + np.random.normal(0, 2, len(x))
    # size and color:
    sizes = np.random.uniform(15, 80, len(x))
    opacity = np.random.uniform(0, 1, len(x))
    return opacity, sizes, x, y


@app.cell
def __(mo, np, opacity, plt, sizes, widget, x, y):
    fig, ax = plt.subplots()
    fig.set_size_inches(3, 3)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    ax.scatter(x, y, s=sizes*5, color=widget.color or None, alpha=opacity)
    mo.hstack([widget, plt.gca()], justify="start", widths=[1, 1])
    return ax, fig


if __name__ == "__main__":
    app.run()
