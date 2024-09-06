import marimo

__generated_with = "0.7.21-dev18"
app = marimo.App()


@app.cell(hide_code=True)
def __():
    from typing import Tuple

    import cvxpy as cp
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm
    return Tuple, cm, cp, np, plt


@app.cell(hide_code=True)
def __(mo):
    mo.md("""# Optimal trajectory planning""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""_This notebook accompanies [Lecture 3, Landing a rocket using model predictive control](https://www.cvxgrp.org/nasa/pdf/lecture3.pdf), of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""### Initial position and velocity""")
    return


@app.cell(hide_code=True)
def __(mo):
    p0_x = mo.ui.slider(0, 100, value=50, show_value=True, label="$p_0 \mid x$")
    p0_y = mo.ui.slider(0, 100, value=50, show_value=True, label="$p_0 \mid y$")
    p0_z = mo.ui.slider(0, 200, value=100, show_value=True, label="$p_0 \mid z$")
    v0_x = mo.ui.slider(-20, 20, value=-10, show_value=True, label="$v_0 \mid x$")
    v0_y = mo.ui.slider(-20, 20, value=0, show_value=True, label="$v_0 \mid y$")
    v0_z = mo.ui.slider(-20, 20, value=-10, show_value=True, label="$v_0 \mid z$")

    mo.hstack([mo.vstack([p0_x, p0_y, p0_z]), mo.vstack([v0_x, v0_y, v0_z])])
    return p0_x, p0_y, p0_z, v0_x, v0_y, v0_z


@app.cell
def __(np, p0_x, p0_y, p0_z, v0_x, v0_y, v0_z):
    # Test data
    h = 1  # discretization step in s
    g = 0.1  # gravity in m/s^2
    m = 10.0  # mass in kg
    F_max = 10.0  # maximum thrust in Newton
    alpha = np.pi / 8  # glide angle in rad
    p0 = np.array([50, 50, 100])  # initial position in m
    v0 = np.array([-10, 0, -10])  # initial velocity in m/s
    p0 = np.array([p0_x.value, p0_y.value, p0_z.value])  # initial position in m
    v0 = np.array([v0_x.value, v0_y.value, v0_z.value])  # initial velocity in m/s
    p_target = np.array([0, 0, 0])  # target position in m
    gamma = 1.0  # fuel consumption coefficient
    K = 35  # number of discretization steps
    return F_max, K, alpha, g, gamma, h, m, p0, p_target, v0


@app.cell
def __(Tuple, cp, np):
    # Formulate the optimization problem


    def optimize_fuel(
        p_target: np.ndarray,
        g: float,
        m: float,
        p0: np.ndarray,
        v0: np.ndarray,
        K: int,
        h: float,
        F_max: float,
        alpha: float,
        gamma: float,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """

        Minimize fuel consumption for a rocket to land on a target

        :param p_target: landing target in m
        :param g: gravitational acceleration in m/s^2
        :param m: mass in kg
        :param p0: position in m
        :param v0: velocity in m/s
        :param K: Number of discretization steps
        :param h: discretization step in s
        :param F_max: maximum thrust of engine in kg*m/s^2 (Newton)
        :param alpha: Glide path angle in radian
        :param gamma: converts fuel consumption to liters of fuel consumption
        :return: position and thrust over time
        """

        P_min = p_target[2]

        # Variables
        V = cp.Variable((K + 1, 3))  # velocity
        P = cp.Variable((K + 1, 3))  # position
        F = cp.Variable((K, 3))  # thrust

        # Constraints
        # Match initial position and initial velocity
        constraints = [
            V[0] == v0,
            P[0] == p0,
        ]

        # Keep height above P_min
        constraints += [P[:, 2] >= P_min]

        # Match final position and 0 velocity
        constraints += [
            V[K] == [0, 0, 0],
            P[K] == p_target,
        ]

        # Physics dynamics for velocity
        constraints += [V[1:, :2] == V[:-1, :2] + h * (F[:, :2] / m)]
        constraints += [V[1:, 2] == V[:-1, 2] + h * (F[:, 2] / m - g)]

        # Physics dynamics for position
        constraints += [P[1:] == P[:-1] + h / 2 * (V[:-1] + V[1:])]

        # Maximum thrust constraint
        constraints += [cp.norm(F, 2, axis=1) <= F_max]

        # Glide path constraint
        constraints += []

        fuel_consumption = gamma * cp.sum(cp.norm(F, axis=1))

        problem = cp.Problem(cp.Minimize(fuel_consumption), constraints)
        problem.solve()
        return P.value, F.value, V.value
    return optimize_fuel,


@app.cell
def __(F_max, K, alpha, g, gamma, h, m, optimize_fuel, p0, p_target, v0):
    # Solve the problem

    P_star, F_star, V_star = optimize_fuel(
        p_target, g, m, p0, v0, K, h, F_max, alpha, gamma
    )
    return F_star, P_star, V_star


@app.cell
def __(mo):
    mo.md(r"""### Plot the trajectory""")
    return


@app.cell(hide_code=True)
def __(mo):
    azim_slider = mo.ui.slider(-180, 180, label="azim", show_value=True, value=160)
    azim_slider
    return azim_slider,


@app.cell(hide_code=True)
def __(F_star, P_star, alpha, azim_slider, cm, np, plt):
    _fig = plt.figure()
    _ax = _fig.add_subplot(projection="3d")
    X = np.linspace(P_star[:, 0].min() - 10, P_star[:, 0].max() + 10, num=30)
    Y = np.linspace(P_star[:, 1].min() - 10, P_star[:, 1].max() + 10, num=30)
    X, Y = np.meshgrid(X, Y)
    Z = np.tan(alpha) * np.sqrt(X**2 + Y**2)
    _ax.plot_surface(
        X,
        Y,
        Z,
        rstride=1,
        cstride=1,
        cmap=cm.autumn,
        linewidth=0.1,
        alpha=0.7,
        edgecolors="k",
    )

    _ax = plt.gca()
    _ax.view_init(azim=azim_slider.value)
    _ax.plot(
        xs=P_star[:, 0], ys=P_star[:, 1], zs=P_star[:, 2], c="b", lw=2, zorder=5
    )

    _ax.quiver(
        P_star[:-1, 0],
        P_star[:-1, 1],
        P_star[:-1, 2],
        F_star[:, 0],
        F_star[:, 1],
        F_star[:, 2],
        zorder=5,
        color="black",
        length=2,
    )

    _ax.set_xlabel("x")
    _ax.set_ylabel("y")
    _ax.set_zlabel("z")
    return X, Y, Z


@app.cell
def __(mo):
    mo.md(r"""### Plot the Position, Velocity and Thrust over time""")
    return


@app.cell(hide_code=True)
def __(F_star, P_star, V_star, plt):
    _fig, _ax = plt.subplots(3, 1, sharex=True)

    _ax[0].plot(P_star[:, 0], label="x")
    _ax[0].plot(P_star[:, 1], label="y")
    _ax[0].plot(P_star[:, 2], label="z")
    _ax[0].set_ylabel("Position")
    _ax[0].legend()

    _ax[1].plot(F_star[:, 0], label="x")
    _ax[1].plot(F_star[:, 1], label="y")
    _ax[1].plot(F_star[:, 2], label="z")
    _ax[1].set_ylabel("Thrust")
    _ax[1].legend()

    _ax[2].plot(V_star[:, 0], label="x")
    _ax[2].plot(V_star[:, 1], label="y")
    _ax[2].plot(V_star[:, 2], label="z")
    _ax[2].set_ylabel("Velocity")
    _ax[2].legend()
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
