import marimo

__generated_with = "0.7.13"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        r"""_This notebook accompanies [Lecture 1, Introduction to Convex Optimization](https://www.cvxgrp.org/nasa/pdf/lecture1.pdf), of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._"""
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        **Fuel use as function of distance and speed.** A vehicle uses fuel at a rate 
        $f(s)$, which is a function of the vehicle speed $s$.
        We assume that $f : \mathbb{R} \to \mathbb{R}$ is a positive increasing convex function, with dom 
        $f = \mathbb{R}_+$. he physical units of $s$
        are m/s (meters per second), and the physical units of $f(s)$
        are kg/s (kilograms per second). Let 
        $g(d,t)$ be the total fuel used (in kg) when the vehicle moves a distance 
        $d \geq 0$ (in meters) in time 
        $t > 0$ (in seconds) at a constant speed. Write $g$ in DCP form. Hint: Check out the “perspective” atom.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.accordion(
        {
            "Solution": mo.md(
                """
        Since $g$ is the total fuel in kg when moving a distance $d$ in time $t$, we have $g(d,t) = t f(d/t)$.
        The function is known as the perspective function of $f$, and is convex when $f$ is convex (see Boyd and Vandenberghe, §3.2.6).
        """
            )
        }
    )
    return


if __name__ == "__main__":
    app.run()
