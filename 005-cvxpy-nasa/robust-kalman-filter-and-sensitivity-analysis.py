import marimo

__generated_with = "0.7.13"
app = marimo.App(width="medium")


@app.cell
def __():
    import cvxpy as cp
    import numpy as np
    import matplotlib.pyplot as plt
    import marimo as mo
    return cp, mo, np, plt


@app.cell
def __(mo):
    mo.md(r"""_This notebook accompanies [Lecture 4](https://www.cvxgrp.org/nasa/pdf/lecture4.pdf) of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Robust Kalman Filter

        Consider the following linear dynamical system: 

        $$                                                                                  
        \begin{array}{ll}                                                                   
        x_{t+1} &= A x_t + B w_t \\                                                         
        y_t &= C x_t + v_t,                                                              
        \end{array}                                                                      
        $$                                                                               

        where $x_t \in \reals^n$ is the vehicle's state at time $t \in \{0, \ldots, N-1\}$,
        $y_t \in \reals^r$ are the measurements, and $w_t \in \reals^m$ are unobserved inputs, and 
        $v_t \in \reals^r$ is noise.                                                     

        The matrices $A$, $B$, and $C$ determining the system are fixed.                 

        Because we suspect outliers in the measurements, we want to use a robust Kalman filter to estimate the state $x_t$.

        Implement the robust Kalman filter below, where


        $$                                                                                  
        \begin{array}{ll}                                                                   
        \text{minimize} & \sum_{t=0}^{N-1} \|w_t\|_2^2 + \tau \phi(v_t) \\                  
        \text{subject to} & x_{t+1} = A x_t + B w_t \\                                   
        & y_t = C x_t + v_t,                                                             
        \end{array}                                                                      
        $$        

        where $\phi$ is the Huber loss function ("cp.huber"), parameterized by $M$.
        """
    )
    return


@app.cell
def __(np, plt):
    # Problem data

    n = 1000  # number of timesteps
    T = 50  # time will vary from 0 to T with step delt
    ts, delt = np.linspace(0, T, n, endpoint=True, retstep=True)
    gamma = 0.05  # damping, 0 is no damping

    A = np.zeros((4, 4))
    B = np.zeros((4, 2))
    C = np.zeros((2, 4))

    A[0, 0] = 1
    A[1, 1] = 1
    A[0, 2] = (1 - gamma * delt / 2) * delt
    A[1, 3] = (1 - gamma * delt / 2) * delt
    A[2, 2] = 1 - gamma * delt
    A[3, 3] = 1 - gamma * delt

    B[0, 0] = delt**2 / 2
    B[1, 1] = delt**2 / 2
    B[2, 0] = delt
    B[3, 1] = delt

    C[0, 0] = 1
    C[1, 1] = 1

    sigma = 5
    p = 0.20
    np.random.seed(6)

    _x = np.zeros((4, n + 1))
    _x[:, 0] = [0, 0, 0, 0]
    y = np.zeros((2, n))

    # generate random input and noise vectors
    _w = np.random.randn(2, n)
    _v = np.random.randn(2, n)

    # add outliers to v
    np.random.seed(0)
    inds = np.random.rand(n) <= p
    _v[:, inds] = sigma * np.random.randn(2, n)[:, inds]

    # simulate the system forward in time
    for _t in range(n):
        y[:, _t] = C.dot(_x[:, _t]) + _v[:, _t]
        _x[:, _t + 1] = A.dot(_x[:, _t]) + B.dot(_w[:, _t])

    x_true = _x.copy()
    w_true = _w.copy()

    plt.figure()
    plt.plot(y[0], y[1], "bo", alpha=0.1, label="Observed")
    plt.plot(x_true[0], x_true[1], "ro", alpha=0.1, label="True")
    plt.legend()
    return A, B, C, T, delt, gamma, inds, n, p, sigma, ts, w_true, x_true, y


@app.cell(hide_code=True)
def __(mo):
    tau_slider = mo.ui.slider(0, 5, 0.1, value=2, label=r"$\tau$", show_value=True)
    M_slider = mo.ui.slider(0, 5, 0.1, value=2, label=r"M", show_value=True)

    mo.vstack([tau_slider, M_slider])
    return M_slider, tau_slider


@app.cell
def __(M_slider, cp, n, np, tau_slider):
    # Task: Implement the robust Kalman filter

    tau = tau_slider.value
    M = M_slider.value

    x = cp.Variable(...)
    w = cp.Variable(...)
    v = cp.Variable(...)

    obj = ...

    constraints = []
    for t in range(n):
        constraints += ...

    cp.Problem(obj, constraints).solve()

    x_robust = np.array(x.value)
    w_robust = np.array(w.value)
    return M, constraints, obj, t, tau, v, w, w_robust, x, x_robust


@app.cell(hide_code=True)
def __(constraints, cp, n, np, tau, v, w, x):
    # Non-robust for comparison

    obj_non_robust = cp.sum_squares(w) + cp.sum(
        [tau * cp.sum_squares(v[:, t]) for t in range(n)]
    )
    obj_non_robust = cp.Minimize(obj_non_robust)

    cp.Problem(obj_non_robust, constraints).solve()

    x_non_robust = np.array(x.value)
    w_non_robust = np.array(w.value)
    return obj_non_robust, w_non_robust, x_non_robust


@app.cell(hide_code=True)
def __(plt, x_non_robust, x_robust, x_true, y):
    # Plot comparison

    plt.figure()
    plt.plot(y[0], y[1], "bo", alpha=0.1, label="Observed")
    plt.plot(x_true[0], x_true[1], "ro", alpha=0.1, label="True")
    plt.plot(x_non_robust[0], x_non_robust[1], "yo", alpha=0.1, label="Non-robust")
    plt.plot(x_robust[0], x_robust[1], "go", alpha=0.1, label="Robust")
    plt.legend()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Sensitivity Analysis

        Task: Find the dual variable associated with the risk constraint to complete the code.
        """
    )
    return


@app.cell
def __(np):
    # Define constants

    rng = np.random.default_rng(0xEE364A)

    Budget = 100
    n_assets = 100
    prices = rng.uniform(0, 2, n_assets) ** 2 + 0.5
    mu = rng.normal(0.01, 1, n_assets)
    Sigma = (
        Z := rng.normal(0, 1 / np.sqrt(n_assets), (n_assets, n_assets))
    ).T @ Z + 0.1 * np.eye(n_assets)
    return Budget, Sigma, Z, mu, n_assets, prices, rng


@app.cell
def __(Budget, Sigma, cp, mu, n_assets, np, prices):
    # Helpers
    def minimum_volatility():
        x = cp.Variable(n_assets, nonneg=True)
        problem = cp.Problem(
            cp.Minimize(cp.quad_form(x, Sigma)), [prices @ x == Budget]
        )
        problem.solve()
        assert problem.status == cp.OPTIMAL
        return np.sqrt(problem.value)


    def max_return_volatility():
        x = cp.Variable(n_assets, nonneg=True)
        problem = cp.Problem(cp.Maximize(mu @ x), [prices @ x == Budget])
        problem.solve()
        assert problem.status == cp.OPTIMAL
        return np.sqrt(x.value @ Sigma @ x.value)


    mv = minimum_volatility()
    mr = max_return_volatility()
    return max_return_volatility, minimum_volatility, mr, mv


@app.cell
def __(Budget, Sigma, cp, mr, mu, mv, n_assets, np, prices):
    means = []
    volatilities = []
    duals = []

    for i, _S in enumerate(np.linspace(mv, mr, 100)):
        _x = cp.Variable(n_assets, nonneg=True)
        constr = [cp.quad_form(_x, Sigma) <= _S**2, prices @ _x == Budget]
        problem = cp.Problem(cp.Maximize(mu @ _x), constr)
        problem.solve()
        assert problem.status in {
            cp.OPTIMAL,
            cp.OPTIMAL_INACCURATE,
        }, problem.status

        # TASK: Get dual variables for variance constraint as a single float
        duals.append(...)

        means.append(problem.value)
        volatilities.append(np.sqrt(cp.quad_form(_x, Sigma).value))
    return constr, duals, i, means, problem, volatilities


@app.cell
def __(duals, means, np, plt, volatilities):
    fig = plt.figure()
    plt.plot(volatilities, means)
    for _i in range(10, 99, 10):
        _x = [volatilities[_i], volatilities[_i + 9]]
        _d = duals[_i] if isinstance(duals[_i], float) else np.squeeze(duals[_i])
        _y = [
            means[_i],
            means[_i] + _d * (volatilities[_i + 9] ** 2 - volatilities[_i] ** 2),
        ]
        plt.plot(_x, _y, c="r")
    plt.legend(["Efficient frontier", "Local approximations"])
    plt.ylabel("Expected return")
    plt.xlabel("Volatility")
    fig
    return fig,


if __name__ == "__main__":
    app.run()
