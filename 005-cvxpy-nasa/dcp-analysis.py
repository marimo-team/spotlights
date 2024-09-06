import marimo

__generated_with = "0.7.21-dev18"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # DCP analysis

        In this exercise, you will learn how to use the DCP ruleset to write convex functions in a DCP-compatible way.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""_This notebook accompanies [Lecture 1, Introduction to Convex Optimization](https://www.cvxgrp.org/nasa/pdf/lecture1.pdf), of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._""")
    return


@app.cell
def __():
    import cvxpy as cp
    import numpy as np
    return cp, np


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Problem 1:
        \[
            f(x) = \exp(\sqrt{x})
        \]

        - Why is this function not DCP?
        - Which property would the inner function, here $\sqrt{x}$, need, to make $f$ DCP-compliant?
        """
    )
    return


@app.cell
def __(cp):
    _x = cp.Variable()

    _g = cp.sqrt(_x)
    _f = cp.exp(_g)

    _f.is_dcp()

    # TODO replace _g with a different CVXPY function to make _f DCP compliant
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Problem 2:
        \[
            f(x) = \sqrt{x^2}
        \]

        - Why is this function not DCP?

        _Hint: This function has a special name._
        """
    )
    return


@app.cell
def __(cp):
    _x = cp.Variable()

    _f = cp.sqrt(_x**2)

    _f.is_dcp()

    # TODO explain why the function isn't DCP and rewrite it to satisfy DCP.
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Problem 3:
        \[
            f(x) = \sqrt{x^2 + 1}
        \]

        - Why is this function not DCP?

        _Hint: `Use cp.hstack([a, b])` to create a vector (a, b)_
        """
    )
    return


@app.cell
def __(cp):
    _x = cp.Variable()

    _f = cp.sqrt(_x**2 + 1)

    _f.is_dcp()

    # TODO explain why the function isn't DCP and rewrite it to satisfy DCP.
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Problem 4:
        \[
            f(x) = \left( \max(x, 4) -3 \right)^2
        \]

        - Why is this function not DCP?

        _Hint: Can we rewrite the inner expression so CVXPY can infer the sign?_
        """
    )
    return


@app.cell
def __(cp):
    _x = cp.Variable()

    _f = (cp.maximum(_x, 4) - 3) ** 2

    _f.is_dcp()

    # TODO explain why the function isn't DCP and rewrite it to satisfy DCP.
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Problem 5:
        \[
            f(x) = \frac{cx}{u - x}
        \]

        - Why is this function not DCP?

        _Hint: Add_ $\text{ }cu - cu\text{ }$_ to the numerator._
        """
    )
    return


@app.cell
def __(cp):
    _x = cp.Variable()
    _c = 1
    _u = 2

    # a / b is written as a * cp.inv_pos(b) in CVXPY

    _f = _c * _x * cp.inv_pos(_u - _x)

    _f.is_dcp()

    # TODO explain why the function isn't DCP and rewrite it to satisfy DCP.
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
