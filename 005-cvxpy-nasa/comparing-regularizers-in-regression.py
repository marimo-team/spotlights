# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "cvxpy",
#     "numpy",
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.8.11"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md("""# Regularization and Sparsity""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""_This notebook accompanies [Lecture 5](https://www.cvxgrp.org/nasa/pdf/lecture5.pdf) of the Convex Optimization Short Course, which was held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        This notebook shows how the choice of regularization in a least squares regression
        problem can affect the sparsity of solutions.

        We will use CVXPY to solve the problem

        \[
        \begin{equation*}
        \begin{array}{ll}
        \text{minimize} & \|A x - b\|_2^2 + \lambda \|x \|_p \\
        \end{array}
        \end{equation*}
        \]

        where $A \in \mathbf{R}^{m \times n}$ and $b \in \mathbf{R}^{m}$ are problem
        data, $x \in \mathbf{R}^n$ is the optimization variable, and
        $\lambda > 0$ is
        a scalar that controls the strength of the regularization.

        Let's experiment how solutions to this problem differ for $p=1$,

        \[
        \|x\|_1 = |x_1| + |x_2| + \cdots + |x_n|, 
        \]

        and $p=2$,

        \[
        \|x\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}. 
        \]
        """
    )
    return


@app.cell
def __(np):
    # Problem data
    m = 100
    n = 20

    np.random.seed(0)
    A = np.random.randn(m, n)
    b = np.random.randn(m)
    return A, b, m, n


@app.cell
def __(mo):
    mo.md("""**TODO**: Implement the `create_problem` function below.""")
    return


@app.cell
def __(cp):
    def create_problem(A, b, p):
        # create the optimization variable x
        x = ...
        # lambd is the regularization hyperparameter lambda
        lambd = cp.Parameter(nonneg=True)
        # create the objective: minimize the sum squares of the residuals plus the
        # regularization
        objective = cp.Minimize(...)
        # don't change the next line
        return cp.Problem(objective), x, lambd
    return create_problem,


@app.cell(hide_code=True)
def __():
    def solver(problem, x, lambd):
        def solve(v):
            lambd.value = v
            problem.solve()
            return x.value

        return solve
    return solver,


@app.cell(hide_code=True)
def __(A, b, create_problem, solver):
    l2_solver = solver(*create_problem(A, b, p=2))
    l1_solver = solver(*create_problem(A, b, p=1))
    return l1_solver, l2_solver


@app.cell(hide_code=True)
def __(functools, l1_solver, l2_solver, np, sparsity_parameter):
    x_min_max = [np.inf, -np.inf]


    @functools.cache
    def solve(lambd):
        return l2_solver(lambd), l1_solver(lambd)


    x_l2, x_l1 = solve(sparsity_parameter.value)
    return solve, x_l1, x_l2, x_min_max


@app.cell
def __(mo):
    mo.md("""## Parameter selection""")
    return


@app.cell(hide_code=True)
def __(mo):
    sparsity_parameter = mo.ui.slider(0, 10, step=0.1)
    mo.md(
        f"""
        Choose the regularization strength $\lambda$: {sparsity_parameter}
        """
    )
    return sparsity_parameter,


@app.cell(hide_code=True)
def __(mo, n, number_of_zeros, sparsity_parameter, x_l1, x_l2):
    (
        mo.md(
            """
            **$\lambda$ = 0.**

            No regularization is applied. The solutions are the same.
            """
        )
        if sparsity_parameter.value == 0
        else mo.md(
            f"""
            **$\lambda$ = {sparsity_parameter.value}.**

            Watch how the fraction of entries of $x$ near $0$ changes as $\lambda$ 
            increases.

            **$p=1$**: {number_of_zeros(x_l1) / n * 100:.02f}% of the entries of 
            $x$ are extremely close to $0$.

            **$p=2$**: {number_of_zeros(x_l2) / n * 100:.02f}% of the entries of 
            $x$ are extremely close to $0$.
            """
        )
    )
    return


@app.cell(hide_code=True)
def __(cdf, plt, x_l1, x_l2):
    cdf_figure, cdf_axs = plt.subplots(2, 1, sharex=True)
    cdf(x_l1, cdf_axs[0]).set_title("$p=1$")
    cdf(x_l2, cdf_axs[1]).set_title("$p=2$")
    plt.tight_layout()
    cdf_figure
    return cdf_axs, cdf_figure


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        ## Sparsity

        The $\ell_1$ norm, when used as a regularizer, encourages solutions
        to be _sparse_: to have many zeros and only a few nonzeros.

        A sparse regressor (if it is a good model) encodes which featuers
        are important for making predictions, and which are not: If a component
        of $x$ is $0$, then the corresponding feature or measurement
        must not be important in making predictions.
        """
    )
    return


@app.cell(hide_code=True)
def __(np):
    def number_of_zeros(x):
        return np.isclose(x, 0).sum()
    return number_of_zeros,


@app.cell(hide_code=True)
def __(np, x_min_max):
    def cdf(x, ax):
        heights = np.arange(1, x.size + 1) / x.size
        xs = np.sort(x)
        if np.min(xs) < x_min_max[0]:
            x_min_max[0] = np.min(xs)
        if np.max(xs) > x_min_max[1]:
            x_min_max[1] = np.max(xs)
        ax.set_xlim(-0.2, 0.2)
        ax.step(xs, heights)
        ax.set_xlabel("$x_i$")
        ax.set_ylabel("fraction of components")
        return ax
    return cdf,


@app.cell
def __():
    import cvxpy as cp
    import matplotlib.pyplot as plt
    import numpy as np
    return cp, np, plt


@app.cell
def __():
    import functools
    return functools,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
