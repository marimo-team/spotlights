import marimo

__generated_with = "0.7.13"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""_This notebook accompanies [lecture 7](https://www.cvxgrp.org/nasa/pdf/lecture7.pdf) of the Convex Optimization Short Course, held at NASA in the summer of 2024._""")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Flux balance analysis in systems biology 
        Flux balance analysis is based on a very simple model of
        the reactions going on in a cell, keeping track only of the gross rate of consumption and production
        of various chemical species within the cell. Based on the known stoichiometry of the reactions, and
        known upper bounds on some of the reaction rates, we can compute bounds on the other reaction
        rates, or cell growth, for example.

        We focus on m metabolites in a cell, labeled $M_1, \ldots, M_m$. There are $n$ reactions going on, labeled
        $R_1, \ldots, R_n$, with nonnegative reaction rates $v_1, \ldots, v_n$. Each reaction has a (known) stoichiometry,
        which tells us the rate of consumption and production of the metabolites per unit of reaction rate.
        The stoichiometry data is given by the *stoichiometry matrix* $S \in \mathbf{R}^{m \times n}$, defined as follows: $S_{ij}$
        is the rate of production of $M_i$ due to unit reaction rate $v_j = 1$. Here we consider consumption
        of a metabolite as negative production; so $S_{ij} = −2$, for example, means that reaction $R_j$ causes
        metabolite $M_i$ to be consumed at a rate $2v_j$.

        As an example, suppose reaction $R_1$ has the form $M_1 \rightarrow M_2 + 2M_3$. The consumption rate of $M_1$,
        due to this reaction, is $v_1$; the production rate of $M_2$ is $v_1$; and the production rate of $M_3$ is $2v_1$.
        (The reaction $R_1$ has no effect on metabolites $M_4, \ldots, M_m$.) This corresponds to a first column of
        $S$ of the form $(−1, 1, 2, 0, \ldots, 0)$.

        Reactions are also used to model flow of metabolites into and out of the cell. For example, suppose
        that reaction $R_2$ corresponds to the flow of metabolite $M_1$ into the cell, with $v_2$ giving the flow
        rate. This corresponds to a second column of $S$ of the form $(1, 0, \ldots, 0)$.

        The last reaction, $R_n$, corresponds to biomass creation, or cell growth, so the reaction rate $v_n$ is
        the cell growth rate. The last column of $S$ gives the amounts of metabolites used or created per
        unit of cell growth rate.

        Since our reactions include metabolites entering or leaving the cell, as well as those converted
        to biomass within the cell, we have conservation of the metabolites, which can be expressed as
        $Sv = 0$. In addition, we are given upper limits on some of the reaction rates, which we express as
        $v \preceq v^\mathrm{max}$, where we set $v^\mathrm{max}_j = \infty$ if no upper limit on reaction rate $j$ is known. The goal is to
        find the maximum possible cell growth rate (i.e., largest possible value of $v_n$) consistent with the
        constraints

        \[
        Sv = 0, \quad v \succeq 0, \quad v \preceq v^\mathrm{max}.
        \]
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## (a) Maximum growth rate
        Find the maximum possible cell growth rate $G^\star$, using the data provided below.
        """
    )
    return


@app.cell
def __():
    # data file for flux balance analysis in systems biology
    # From Segre, Zucker et al "From annotated genomes to metabolic flux
    # models and kinetic parameter fitting" OMICS 7 (3), 301-316.
    import numpy as np

    # Stoichiometric matrix
    #    columns are M1    M2    M3    M4    M5    M6
    # For your interest, the rows correspond to the following equations
    #    R1:  extracellular -->  M1
    #    R2:  M1 -->  M2
    #    R3:  M1 -->  M3
    #    R4:  M2 + M5 --> 2 M4
    #    R5:  extracellular -->  M5
    #    R6:  2 M2 -->  M3 + M6
    #    R7:  M3 -->  M4
    #    R8:  M6 --> extracellular
    #    R9:  M4 --> cell biomass
    S = np.array(
        np.matrix(
            """
        1,0,0,0,0,0;
        -1,1,0,0,0,0;
        -1,0,1,0,0,0;
        0,-1,0,2,-1,0;
        0,0,0,0,1,0;
        0,-2,1,0,0,1;
        0,0,-1,1,0,0;
        0,0,0,0,0,-1;
        0,0,0,-1,0,0
        """
        ).T
    )
    m, n = S.shape

    vmax = np.array(
       [10.10,
        100,
        5.90,
        100,
        3.70,
        100,
        100,
        100,
        100]
    )
    return S, m, n, np, vmax


@app.cell
def __(Gstar, n):
    import cvxpy as cp

    v = cp.Variable(n)
    # TODO: your code here


    print(Gstar)
    return cp, v


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## (b) Essential genes and synthetic lethals

        For simplicity, we'll assume that each reaction is controlled
        by an associated gene, i.e., gene $G_i$ controls reaction $R_i$. Knocking out a set of genes
        associated with some reactions has the effect of setting the reaction rates (or equivalently, the
        associated $v^\mathrm{max}$ entries) to zero, which of course reduces the maximum possible growth rate.
        If the maximum growth rate becomes small enough or zero, it is reasonable to guess that
        knocking out the set of genes will kill the cell. An *essential gene* is one that when knocked
        out reduces the maximum growth rate below a given threshold $G^\mathrm{min}$. (Note that $G_n$ is always
        an essential gene.) A *synthetic lethal* is a pair of non-essential genes that when knocked out
        reduces the maximum growth rate below the threshold. Find all essential genes and synthetic
        lethals for the given problem instance, using the threshold $G^\mathrm{min} = 0.2G^\star$.
        """
    )
    return


@app.cell
def __(Gstar, n, np):
    # Check essential genes and synthetic lethals
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            # Taking out genes i and j (i can equal j)
            # TODO: your code here
            pass

    print(G < 0.2*Gstar)
    return G, i, j


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
