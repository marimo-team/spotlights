import marimo

__generated_with = "0.7.13"
app = marimo.App(width="medium")


@app.cell
def __():
    import numpy as np
    return np,


@app.cell
def __():
    import cvxpy as cp
    return cp,


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""This notebook is based on $\S3$ of [Geometric Programming for Aircraft Design Optimization](https://people.eecs.berkeley.edu/~pabbeel/papers/2012_gp_design.pdf), by Warren Hoburg and Pieter Abbeel. It accompanies [Lecture 5](https://www.cvxgrp.org/nasa/pdf/lecture6.pdf) of the Convex Optimization Short Course, which was held at NASA in the summer of 2024.""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Our goal is to size a wing with total area $S$, span $b$, and aspect ratio $A =
        b^2/S$. These parameters should be chosen to minimize the total drag $D = 1/2
        \rho V^2 C_D S$.

        The drag coefficient $C_D$ is modeled as the sum of the fuselage parasite drag, wing parasite drag, and induced drag:

        \[
        C_D = (\text{CDA}_0)/S + kC_f + S_{\text{wet}}/S + \frac{C^2_{L}}{\pi A e},
        \]

        where $(\text{CDA}_0)/S$ is the fuselage drag area, $k$ is a form factor for pressure drag, $S_{wet}/S$ is the wetted area ratio, and $e$ is the Oswald efficiency factor.

        The skin friction $C_f$ can be approximated as

        \[
        C_f = 0.074/\text{Re}^2
        \]

        where $Re = \rho V / \mu \sqrt(S/A)$ is the Reynolds number at mean cord $c = \sqrt{S/A}$.

        The total aircraft weight $W$ is the sum of a fixed weight $W_0$ and the wing weight $W_w$:

        \[
        W = W_0 + W_w.
        \]

        The wing weight is

        \[
        W_w = 45.42S + 8.71 \cdot 10^{-5} N_\text{ult} A^{3/2}\sqrt{W_0 W} / \tau,
        \]

        where $N_\text{ult}$ is the ultimate load factor for structural sizing, and $\tau$ is the airfoil thickenss to chord ratio.

        The weight equations are coupled to the drag equations by the constraint that lift equals weight,

        \[
        W = 1/2 \rho V^2 C_L S.
        \]

        Finally, for a safe landing, the aircraft should be capable of flying at a reduced speed $V_{\text{min}}$ subject to a stall constraint,

        \[
        \frac{2W}{\rho V_\text{min}^2 S} \leq C_{L, \max}.
        \]
        """
    )
    return


@app.cell
def __():
    # Problem data

    # form factor
    k = 1.2

    # Oswald efficiency factor
    e = 0.95

    # viscosity of air, kg/m/s
    mu = 1.78e-5

    # density of air, kg/m^3
    rho = 1.23

    # airfoil thickness to chord ratio
    tau = 0.12

    # ultimate load factor
    N_ult = 3.8

    # m/s, takeoff speed
    V_min = 22

    # max CL with flaps down")
    C_Lmax = 1.5 

    # wetted area ratio
    S_wetratio = 2.05 

    # 1/m, Wing Weight Coefficent 1
    W_W_coeff1 = 8.71e-5, 

    # Pa, Wing Weight Coefficent 2
    W_W_coeff2 = 45.24

    # m^2 fuselage drag area
    CDA0 = 0.031 

    # N, aircraft weight excluding wing
    W_0 = 4940.0
    return (
        CDA0,
        C_Lmax,
        N_ult,
        S_wetratio,
        V_min,
        W_0,
        W_W_coeff1,
        W_W_coeff2,
        e,
        k,
        mu,
        rho,
        tau,
    )


@app.cell
def __(cp):
    # Design Variables

    # aspect ratio
    A = cp.Variable(pos=True, name="A")
    # m^2, total wing area
    S = cp.Variable(pos=True, name="S")
    # m/s, cruising speed
    V = cp.Variable(pos=True, name="V")
    # N, total aircraft weight
    W = cp.Variable(pos=True, name="W")
    # Reynold's number
    Re = cp.Variable(pos=True, name="Re")
    # drag coefficient of wing
    C_D = cp.Variable(pos=True, name="C_D")
    # lift coefficient of wing
    C_L = cp.Variable(pos=True, name="C_L")
    # skin friction coefficient
    C_f = cp.Variable(pos=True, name="C_f")
    # "N", "wing weight"
    W_w = cp.Variable(pos=True, name="W_w")
    return A, C_D, C_L, C_f, Re, S, V, W, W_w


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""The **total drag** is $1/2 \rho V^2 C_D S$. Express this as a CVXPY expression below, using the problem data and defined variables.""")
    return


@app.cell
def __():
    drag = ...
    return drag,


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Next, specify the constraints.

        Tip: many of the constraints (such as the drag coefficient model for $C_D$) are **posynomial equalities**, which are not compatible with geometric programming. However, you can **relax** these constraints to inequalities because minimizing the objective guarantees that they will be tight at a solution.
        """
    )
    return


@app.cell
def __():
    # Add constraints to this list
    constraints = []

    # Drag model

    # Wing weight model

    # and the rest of the models involving Re, C_f, and W
    return constraints,


@app.cell
def __(constraints, cp, drag, mo):
    problem = cp.Problem(cp.Minimize(drag), constraints)
    print(problem)
    problem.solve(gp=True)
    mo.md(f"The **minimum achievable drag** is {problem.value:0.2f} N.")
    return problem,


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""The **optimal design variables** are""")
    return


@app.cell
def __(problem):
    {var: problem.var_dict[var].value for var in problem.var_dict}
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        The **sensitivities** of the objective to each constraint are listed below.

        Which constraint is the objective most sensitive to? Which constraint is it the least sensitive to?
        """
    )
    return


@app.cell
def __():
    # TODO: Get the sensitivities of the objective value to the constraints
    return


if __name__ == "__main__":
    app.run()
