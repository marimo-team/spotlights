import marimo

__generated_with = "0.7.21-dev18"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    import cvxpy as cp
    return cp, np


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""_This notebook accompanies [Lecture 2, Disciplined Convex Programming](https://www.cvxgrp.org/nasa/pdf/lecture2.pdf), of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        **Portfolio optimization** Imagine we have a budget 
        $B$ (dollars). We can purchase 
        $n$ different assets (e.g. stocks, bonds) with current prices 
        $p$ (dollars per unit), expected returns 
        $\mu$ (dollars per unit), and covariance 
        $\Sigma$ (dollars squared per unit squared). Your goal is to ensure the standard deviation of your portfolio to be less than 
        $S$ (dollars). We are only buying assets, not borrowing them, so we cannot “short” stocks and have a “long”-only portfolio. Lastly, we don’t want to end up over-invested in a single asset, so, let’s ensure we never put more than 
        $5%$ of our budget into a single asset.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo, np):
    # Define constants, B, n, p, mu, Sigma, S

    rng = np.random.default_rng(0xEE364A)

    B = 100
    n = 100
    p = rng.uniform(0, 2, n) ** 2 + 0.5
    mu = rng.normal(0.01, 1, n)
    Sigma = (Z := rng.normal(0, 1 / np.sqrt(n), (n, n))).T @ Z + 0.1 * np.eye(n)
    S = 15

    mo.md("This cell defines constants `B`, `n`, `p`, `mu`, `Sigma`, `S`")
    return B, S, Sigma, Z, mu, n, p, rng


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Define your optimization variables.

        *Hint: it should be cp.Variable*
        """
    )
    return


@app.cell
def __():
    x = ...
    return x,


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Define the objective. 

        *Hint: it should be either cp.Maximize or cp.Minimize*
        """
    )
    return


@app.cell
def __():
    obj = ...
    return obj,


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Create a standard deviation constraint""")
    return


@app.cell
def __():
    stddev_constraint = ...
    return stddev_constraint,


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Add your budget constraint""")
    return


@app.cell
def __():
    budget_constraint = ...
    return budget_constraint,


@app.cell
def __(mo):
    mo.md(rf"Add your long only constraint")
    return


@app.cell
def __():
    long_only_constraint = ...
    return long_only_constraint,


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Add your asset diversity constraint""")
    return


@app.cell
def __():
    asset_diversity_constraint = ...
    return asset_diversity_constraint,


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Make and run your CVXPY problem!""")
    return


@app.cell
def __(
    asset_diversity_constraint,
    budget_constraint,
    cp,
    long_only_constraint,
    obj,
    stddev_constraint,
):
    constr = [
        stddev_constraint,
        budget_constraint,
        long_only_constraint,
        asset_diversity_constraint,
    ]

    prob = cp.Problem(obj, constr)
    prob.solve()
    return constr, prob


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
