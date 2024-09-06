# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "cvxpy",
#     "numpy",
# ]
# ///
import marimo

__generated_with = "0.7.21-dev18"
app = marimo.App(width="medium")


@app.cell
def __():
    import cvxpy as cp
    import numpy as np
    import marimo as mo
    return cp, mo, np


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""_This notebook accompanies [Lecture 2, Disciplined Convex Programming](https://www.cvxgrp.org/nasa/pdf/lecture2.pdf), of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        **Diet problem.** We are going to solve a simple diet problem. We are choosing nonnegative amounts 
        $x_1, \ldots, x_n$ of $n$ different foods. One unit of food 
        $j$ has cost 
        $c_j$ and contains 
        $A_{ij}$
        units of nutrient 
        $i$. We want to minimize the total cost of the food, while ensuring that we get at least 
        $b_i$ units of nutrient $i$.

        Write down the optimization problem for the diet problem and solve it using the data in the notebook
        """
    )
    return


@app.cell
def __(np):
    # cost vector (dollars per kg of food)
    c = np.array([6, 5, 2, 15])

    # Nutrient content matrix
    # Rows corresponding to grams of protein, carbohydrates, and fat per kg of food.
    # The food types in the columns are lentils, broccoli, rice, and almonds.
    A = np.array([[250, 28, 20, 210], [600, 60, 780, 200], [10, 3, 10, 500]])

    # Minimum required nutrients vector (grams per day).
    b = np.array([50, 300, 70])
    return A, b, c


@app.cell
def __():
    x = ...
    return x,


if __name__ == "__main__":
    app.run()
