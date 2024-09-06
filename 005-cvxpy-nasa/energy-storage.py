# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "cvxpy",
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.8.11"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md("""_This notebook accompanies [lecture 7](https://www.cvxgrp.org/nasa/pdf/lecture7.pdf) of the Convex Optimization Short Course, held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        # Energy storage trade-offs

        We consider the use of a storage device (say, a battery) to reduce the total cost of electricity consumed over one day. We divide the day into $T$ time periods, and let $p_t$ denote the (positive, time-varying) electricity price, and $u_t$ denote the (nonnegative) usage or\n    consumption, in period $t$, for $t = 1,\\ldots, T$. Without the use of a battery, the total cost is $p^Tu$.

        Let $q_t$ denote the (nonnegative) energy stored in the battery in period $t$. For simplicity, we neglect energy loss (although this is easily handled as well), so we have $q_{t+1} = q_t + c_t$, $t = 1, \\ldots, T − 1$, where $c_t$ is the charging of the battery in period $t$; $c_t < 0$ means the battery is discharged. We will require that $q_1 = q_T + c_T$, i.e., we finish with the same battery charge that we start with.

        With the battery operating, the net consumption in period $t$ is $u_t + c_t$ ; we require this to be nonnegative\n    (i.e., we do not pump power back into the grid). The total cost is then $p^T(u + c)$.

        The battery is characterized by three parameters: The capacity $Q$, where $q_t \\leq Q$; the maximum charge rate $C$, where $c_t \\leq C$; and the maximum discharge rate $D$, where $c_t \\geq −D$. (The parameters $Q$, $C$, and $D$ are nonnegative.)
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""**(a).** Explain how to find the charging profile $c \\in \\mathbf{R}^T$\n    (and associated stored energy profile $q \\in \\mathbf{R}^T$)\n    that minimizes the total cost, subject to the constraints.\n""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""**(b) **Solve the problem instance with data $p$ and $u$, $Q = 35$,\n    and $C = D = 3$. Plot $u_t$, $p_t$, $c_t$, and $q_t$ versus $t$.\n""")
    return


@app.cell
def __():
    import numpy as np
    import matplotlib.pyplot as plt


    np.random.seed(1)
    T = 96
    t = np.linspace(1, T, num=T).reshape(T)
    p = np.exp(-np.cos((t - 15) * 2 * np.pi / T) + 0.01 * np.random.randn(T))
    u = 2 * np.exp(-0.6 * np.cos((t + 40) * np.pi / T) - 0.7 * np.cos(t * 4 * np.pi / T) + 0.01 * np.random.randn(T))
    plt.figure(1)
    plt.plot(t / 4, p, 'g', label='$p$')
    plt.plot(t / 4, u, 'r', label='$u$')
    plt.ylabel('$')
    plt.xlabel('t')
    plt.legend()
    plt.gcf()
    return T, np, p, plt, t, u


@app.cell
def __(T):
    import cvxpy as cp
    Q = 35
    (C, D) = (5, 5)
    q = cp.Variable(T)
    c = cp.Variable(T)

    # TODO solve an optimization problem to get the optimal q and c.
    prob = ...
    return C, D, Q, c, cp, prob, q


@app.cell
def __(T, c, np, p, plt, q, u):
    plt.figure(2)
    ts = np.linspace(1, T, num=T) / 4
    plt.subplot(3, 1, 1)
    plt.plot(ts, u, 'r')
    plt.plot(ts, c.value, 'b')
    plt.xlabel('t')
    plt.ylabel('uc')
    plt.legend(['u', 'c'])
    plt.subplot(3, 1, 2)
    plt.plot(ts, p, 'b')
    plt.xlabel('t')
    plt.ylabel('pt')
    plt.subplot(3, 1, 3)
    plt.plot(ts, q.value, 'b')
    plt.xlabel('t')
    plt.ylabel('qt')
    plt.ylim((0, 40))
    return ts,


@app.cell(hide_code=True)
def __(mo):
    mo.md("""**(c)** Storage trade-offs. Plot the minimum total cost versus the storage capacity $Q$, using $p$ and\n    $u$ below, and charge/discharge limits $C = D = 3$. Repeat for\n    charge/discharge limits $C = D = 1$. (Put these two trade-off curves on the same plot.) Give\n    an interpretation of the endpoints of the trade-off curves.\n""")
    return


@app.cell
def __(T, cp, np, plt, prob):
    def plot_trade_offs():
        N = 31
        Qs = np.linspace(0, 150, num=N)
        q = cp.Variable(T)
        c = cp.Variable(T)
        Q = cp.Parameter()
        (C, D) = (cp.Parameter(), cp.Parameter())
        C.value = 1
        D.value = 1
        cost1 = np.zeros(N)
        for i in range(N):
            Q.value = Qs[i]
            cost1[i] = prob.solve()
        C.value = 3
        D.value = 3
        cost2 = np.zeros(N)
        for i in range(N):
            Q.value = Qs[i]
            cost2[i] = prob.solve()
        plt.figure(3)
        plt.plot(Qs, cost2, 'g--', label='C = D = 3')
        plt.plot(Qs, cost1, 'b.-', label='C = D = 1')
        plt.xlabel('Q')
        plt.ylabel('cost')
        plt.legend()
        return plt.gcf()

    plot_trade_offs()
    return plot_trade_offs,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
